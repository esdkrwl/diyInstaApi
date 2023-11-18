import requests
import re

followers_re = re.compile(r"^.*?([0-9]+[A-Z])\s*Followers.*")


def get_follower_count(insta_username):
    url = "https://www.instagram.com/" + insta_username
    r = requests.get(url)
    response = r.text
    followers = None

    for line in response.split('\n'):
        if followers_re.match(line):
            followers = followers_re.match(line).group(1)

    # Falls aus Gründen der String nciht gefunden werden kann, gib einfach -1 zurück damit die API Bescheid weiß
    if not followers:
        return -1

    return followers

