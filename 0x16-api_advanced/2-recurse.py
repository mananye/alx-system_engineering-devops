#!/usr/bin/python3
""" Script to query a list of all hot posts on a given Reddit subreddit. """
import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"(link unavailable)"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/thapelogoden)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if data["data"]["after"]:
            recurse(subreddit, hot_list, data["data"]["after"])
        return hot_list
    else:
        return None
