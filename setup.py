from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

version = "4.1.12"

setup(
    name='Babylon End User Documentation',
    version=version,
    author='Cosmo Tech',
    author_email='nibaldo.donoso@cosmotech.com',
    url="https://github.com/Cosmo-Tech/Babylon",
    description='Simple setup.py for the build of the Babylon documentation',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)
