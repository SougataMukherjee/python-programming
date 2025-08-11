import requests  # python -m pip install --user requests


def fetch_sync(url):
    response = requests.get(url)
    return response.json()


data = fetch_sync("https://jsonplaceholder.typicode.com/todos/1")
print(data)
