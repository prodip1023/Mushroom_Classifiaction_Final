from setuptools import setup,find_packages
from typing import List

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt
    """
    with open("requirements.txt") as f:
        return f.readlines().remove("-e .")


# Declaring Variables for setup functions
PROJECT_NAME = "Mushroom_Classifiaction"
VERSION = "0.0.1"
AUTHOR = "PRODIP SARKAR"
DESCRIPTION = "MUSHROOM CLASSIFICATION"
PACKAGES = ["mushroom"]
REQUIREMENT_FILE_NAME = "requirements.txt"


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), # ['mushroom']
    install_requires=get_requirements_list(),
)