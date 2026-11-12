from local_functs import *
from api_functs import *


mod_path = r'../mods'

def main() -> int :
    mv = True
    categories = [] # get_categories()
    for category in categories:
        print(f'name - {category.name} - id {category.id}')

    if mv:
        addons = find_addons(mod_path)
        for addon in addons:
            if not addon.is_dependency:
                make_call(addon.name)
    return 1


if __name__ == "__main__":
    main()