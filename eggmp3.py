import os, json
from dotenv import load_dotenv
import requests

load_dotenv()

API_Key = os.getenv('API_KEY')


def queryYoutube(string):
    url = "https://www.googleapis.com/youtube/v3/search"

    query = {
    'key': API_Key,
    'q': string
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    return json.loads(response.text)


print(queryYoutube()["items"])