from pprint import pprint
import requests
import time
from classes import *
a_key = 'nuhuh'



def get_categories() -> list[Category] :
    url = "https://api.curseforge.com/v1/categories"
    cats = []
    headers = {
        "Accept": "application/json",
        "x-api-key": a_key,
    }

    params = {
        "gameId": 1
    }


    response = curseforge_get(url, headers=headers, params=params)
    print(response.status_code)


    resp_json = response.json()

    for data in resp_json['data']:
        #for a in item:
        #    print(a)

        category = Category(
            id=data["id"],
            gameId=data["gameId"],
            name=data["name"],
            slug=data["slug"],
            url=data["url"],
            iconUrl=data["iconUrl"],
            dateModified=datetime.fromisoformat(
                data["dateModified"].replace("Z", "+00:00")
            ),
            isClass=data.get("isClass"),
            classId=data.get("classId"),
            parentCategoryId=data.get("parentCategoryId"),
            displayIndex=data.get("displayIndex"),
        )
        cats.append(category)
        pprint(data['name'])
    response.raise_for_status()
    return cats



def make_call(search_name : str = ''):
    url = "https://api.curseforge.com/v1/mods/search"

    headers = {
        "Accept": "application/json",
        "x-api-key": a_key,
    }

    params = {
        "gameId": 1,
        "classId": 1,
        "index": 0,
        "pageSize": 20,
        "sortField": 3,
        "sortOrder": "desc",
        "gameVersionTypeId": 88568
    }
    if search_name:
        print(f'adding search name "{search_name}"')
        params["searchFilter"] = search_name
    else:
        print('no searchname')

    response = curseforge_get(url, headers=headers, params=params)
    resp_json = response.json()

    for item in resp_json['data']:
        #for a in item:
        #    print(a)

        pprint(item['name'])

    print(resp_json['pagination'])
    response.raise_for_status()



def curseforge_get(url, headers, params, retries=4):
    for attempt in range(retries):
        print(f'Attempt #{attempt}')
        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=30,
        )

        if response.status_code != 429:
            return response

        retry_after = response.headers.get("Retry-After")

        if retry_after and retry_after.isdigit():
            delay = int(retry_after)
        else:
            delay = 2 ** attempt

        time.sleep(delay)

    return response



