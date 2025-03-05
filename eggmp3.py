import os, json, sys
from dotenv import load_dotenv
import requests

load_dotenv()

API_Key = os.getenv('API_KEY')


def queryYoutube(string):
    url = "https://www.googleapis.com/youtube/v3/search"

    query = {
    'key': API_Key,
    'q': string,
    'part': "snippet"
    }

    response = requests.request(
    "GET",
    url,
    params=query
    )

    # print(response.text)
    return json.loads(response.text)


def itemize_result(items):

    results = []

    for result in items:
        if result['id']["kind"] == "youtube#video":
            results.append(((result["id"]["videoId"]), result['snippet']['title']))


    return results

def main():
    query = sys.argv[1]
    for item in itemize_result(queryYoutube(query)["items"]):
        print(item[1] + "\n")
        print(item[0] + "\n")

    return itemize_result(queryYoutube(query)["items"])

if __name__ == "__main__":
    main()