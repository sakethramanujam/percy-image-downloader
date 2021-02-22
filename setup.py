import os
import sys
from setuptools import setup, find_packages


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "percy", "version.py"
    )
    g = {}
    exec(open(path).read(), g)
    return g["__version__"]


def get_requirements():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
    requirements = open(path, "r").readlines()
    return requirements


setup(name='percy',
      version=get_version(),
      url="https://github.com/sakethramanujam/percy-image-downloader",
      description="Image Downloader for perseverance mission website",
      author="Saketha Ramanujam",
      install_requires=get_requirements(),
      project_urls={},
      packages=find_packages(exclude=("tests")),
      include_package_data=True,
      python_requires=">=3.6",
      entry_points="""
        [console_scripts]
        percy=percy.cli:cli
      """
      )