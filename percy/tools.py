import os

def checkpath(*paths: list):
    """
    Checks if a give path exists and,
    creates if it doesn't
    """
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)

