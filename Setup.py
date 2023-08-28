from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

#Function to get the list of required packages
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='Student Performance Prediction ML Project',
version='0.0.1',
author='Aravind S',
author_email='aravind.14may93@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)