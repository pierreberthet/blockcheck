#!/usr/bin/env python
from setuptools import setup, find_packages
setup(
    name='checkblock',
    version='0.1',
    entry_points={
        'console_scripts': [
            'checkblock=blockjob:run'
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
