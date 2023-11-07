#!/usr/bin/python3
"""
This Python script queries the Reddit API and prints the titles of
first 10 hot posts for a gven subreddit.
"""
import requests


def top_ten(subreddit):
    """This function queries the Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return print(None)
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Pritchad Ncube/ALX-Api-Advanced'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers, params=params)
        dic = response.json().get('data')
        for i in dic.get('children'):
            print(i.get('data').get('title'))
    except Exception:
        return print(None)
