import requests
import json


def get_follower_count(insta_username):
    url = "https://www.instagram.com/" + insta_username
    r = requests.get(url)
    response = r.text

    payload_string = ""

    for line in response.split('\n'):
        if "activity_counts" in line:
            payload_string = line
            break

    # Falls aus Gründen der String nciht gefunden werden kann, gib einfach -1 zurück damit die API Bescheid weiß
    if not payload_string:
        return -1

    # Schneide JSON String aus. Beginne mit dem ersten { und ende mit dem letzen }
    json_substring = payload_string[payload_string.index('{'):payload_string.rindex('}')+1]

    json_payload = json.loads(json_substring)
    follower_count = json_payload['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
    return follower_count

