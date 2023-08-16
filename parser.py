import requests


page = requests.get("https://teacherofrussia.ru/api/competitors?year=2023")


if __name__ == '__main__':
    for element in page.json():
        print(element)
        print(element['user']['full_name'])
        with open(f"photos/{element['user']['full_name']}_{element['avatar']['filename']}", "wb") as file:
            photo = requests.get(f"{element['avatar']['file_path']}")
            file.write(photo.content)
