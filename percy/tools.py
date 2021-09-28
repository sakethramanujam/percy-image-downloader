import os
import math
import requests
import pandas as pd
from .settings import STATS_URL
from .state import State
from datetime import datetime as dt


def give_me_time() -> str:
    """
    Creates and returns datetime timestamp string
    """
    return dt.strftime(dt.now(), '%Y-%m-%d-%H_%M_%S')


def _checkfromfile(filepath: str):
    state = State()
    if not os.path.isfile(filepath):
        print("Oopsie, you sure the file path is right?")
        return None
    else:
        df = pd.read_csv(filepath)
        n = math.ceil(len(df)/50)
        state.create_new()
        ts = give_me_time()
        state.update({"last_updated": ts,
                      "n_scraped": n})
        return n


def n_pages(mode: str = "url") -> int:
    """
    Finds total number of available pages

    Arguments
    ---
    mode: string
        url/file
        - 'url' mode returns total number of available pages on website
        - 'file' mode counts total number of rows in existing/downloaded 
           metadata csv file.

    Returns
    ---
    n:  Returns the number of pages downloaded
    """
    try:
        if mode == "url":
            r = get(STATS_URL)
            stats = r.json()
            n = math.ceil(stats["total"]/50)
            return n
        elif mode == "file":
            filepath = input("Path to existing Persevarance metadata file: ")
            n = _checkfromfile(filepath=filepath)
            if not n:
                n_pages(mode="file")
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


def get(url: str, **kwargs) -> requests.Response:
    """
    Wrapper for requests.get
    """
    try:
        r = requests.get(url, **kwargs)
        status = r.status_code
        return r
    except Exception as e:
            print(f"Network Exception, failed to fetch\
                requested page {url} \n status")
        
