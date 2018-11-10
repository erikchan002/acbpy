# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='acbpy',
    version='0.0.1',
    description='simple extract library for acb.',
    long_description=readme,
    author='Cryptomelone',
    author_email='cryptomelone@users.noreply.github.com',
    url='https://github.com/Cryptomelone/acbpy',
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': [
            'acbpy = acbpy.cmd:main',
        ],
    }
)
