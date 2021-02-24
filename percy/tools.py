import os
import requests
from .settings import STATS_URL


def n_pages():
    """
    Finds total number of available pages
    """
    try:
        r = get(STATS_URL)
        stats = r.json()
        n = round(stats["total"]/50)
        return n
    except Exception as e:
        print(f"Error: {e}")


def checkpath(*paths: list):
    """
    Checks if a give path exists
    Creates dirs if doesn't exist
    """
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


def get(url: str, **kwargs):
    """
    Wrapper for requests.get
    """
    r = requests.get(url, **kwargs)
    if r.status_code == 200:
        return r
    else:
        raise Exception(
            f"Network Exception, failed to fetch requested page {url}")
