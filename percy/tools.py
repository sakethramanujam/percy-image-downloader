import os
import requests

def checkpath(*paths: list):
    """
    Checks if a give path exists and,
    creates if it doesn't
    """
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

def get(url:str,**kwargs):
    """
    Wrapper for requests.get
    """
    return requests.get(url,**kwargs)