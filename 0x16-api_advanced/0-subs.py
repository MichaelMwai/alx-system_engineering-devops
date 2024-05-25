#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0


if __name__ == "__main__":
    # Example usage
    subreddit_name = "learnpython"
    print(f"Number of subscribers in '{subreddit_name}': {number_of_subscribers(subreddit_name)}")

