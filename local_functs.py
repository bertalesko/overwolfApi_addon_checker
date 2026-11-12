from classes import *
import os

def get_top_level_folders(path):
    folders = []
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                try:
                    if entry.is_dir(follow_symlinks=False):
                        folders.append(Path(entry.path))
                except OSError as error:
                    print(error)
    except OSError as error:
        print(error)

    return sorted(folders, key=lambda folder: folder.name.casefold())

def find_addons(mod_path) -> list[Addon] :
    addons = []
    allowed_extensions = '.toc'
    for top_folder in get_top_level_folders(mod_path):
        for root, directories, files in os.walk(top_folder, followlinks=False):
            current_directory = Path(root)
            for filename in files:
                full_path = current_directory / filename
                if full_path.suffix.casefold() not in allowed_extensions:  # not in allowed_extensions:
                    continue

                addons.append(parse_toc(full_path))

    print(f"Found {sum(not addon.is_dependency for addon in addons)} standalone addons")
    return addons

def parse_toc(toc_path :Path) -> Addon :

    data = {}
    with open(toc_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    file.close()

    for a, line in enumerate(lines):
        if line.strip() == '':
            continue
        split = line.split(':')
        if len(split) > 1:
            data[line.split(':')[0].replace('## ', '')] = line.split(':')[1].strip('\n').lstrip()

    if 'RequiredDeps' not in data:
        #print('standalone')
        data['is_dependency'] = False
    else:
        data['is_dependency'] = True


    return Addon(data['Title'],
                 data['Version'],
                 data['Interface'],
                 toc_path,
                 data['is_dependency'])

