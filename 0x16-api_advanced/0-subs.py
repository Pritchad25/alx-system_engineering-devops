#!/usr/bin/python3
"""
This Python script contains a function that works
with the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """This method returns the number of subscribers for a
	given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:\
            v1.0.0 (by /u/Pritchad Ncube)'}
    res = requests.get(url, headers=headers).json()
    try:
        subs = res.get('data').get('subscribers')
        return subs
    except Exception:
        return 0
