from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='Babylon End User Documentation',
    version='3.0.0',
    author='Cosmo Tech',
    author_email='nibaldo.donoso@cosmotech.com',
    url="https://github.com/Cosmo-Tech/Babylon",
    description='Simple setup.py for the build of the Babylon end user documentation',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=required,
)
