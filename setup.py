## setup.py file

from setuptools import find_packages, find_namespace_packages, setup



# Reading the requirements from the "requirements.txt" file
with open("requirements.txt", "r", encoding="Windows-1252") as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

# Setting up the package metadata and dependencies
setup(
    name='car-price_mlops',
    description="Car Prices MLOps",
    version='1.0',
    author="Dimitri MARCHAND",
    install_requires=requirements,
    packages=find_packages() + find_namespace_packages(),
)