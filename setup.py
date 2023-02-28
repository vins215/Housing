from setuptools import setup
from typing import List

PROJECT_NAME = "housing_predictor0"
VERSION = "0.0.1"
AUTOR = "Vinay"
DESCRIPTION = "This is my Project"
PACKAGES = ["Housing"]
REQUIREMENT_FILE_NAME = "requirement.txt"


def get_requirement_list()->List[str]:
    """
    This Function returns the Requirement mentioned in the requirement.txt

    """
    with open(REQUIREMENT_FILE_NAME) as reqirement_file:
        return reqirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME ,
version=VERSION ,
author=AUTOR ,
description = DESCRIPTION ,
packages= PACKAGES , 
install_requires =get_requirement_list()


)
