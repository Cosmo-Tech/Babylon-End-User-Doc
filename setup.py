
from setuptools import setup, find_packages
from src import VERSION

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Documentation Template',
    version=VERSION,
    author='Alexis Fossart',
    author_email='alexis.fossart@cosmotech.com',
    url="https://github.com/Cosmo-Tech/Babylon",
    description='Template repository for python with automated documentation',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)