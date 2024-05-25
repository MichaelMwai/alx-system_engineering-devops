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
    # Test with an existing subreddit
    subreddit_name = "learnpython"
    result = number_of_subscribers(subreddit_name)
    if result > 0:
        print("OK")
    else:
        print("Error: Expected subscribers > 0, got", result)

    # Test with a non-existing subreddit
    invalid_subreddit = "thissubredditdoesnotexist12345"
    result = number_of_subscribers(invalid_subreddit)
    if result == 0:
        print("OK")
    else:
        print("Error: Expected 0 for invalid subreddit, got", result)

