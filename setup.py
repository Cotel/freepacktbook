# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='freepacktbook',
    version='0.0.2',
    description='Claim Your Free PacktPub eBook, fork from https://github.com/bogdal/freepacktbook',
    author='Miguel Coleto',
    author_email='miguelcoletomunoz@hotmail.com',
    url='https://github.com/Cotel/freepacktbook',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4',
        'requests'],
    entry_points={
        'console_scripts': [
            'claim_free_ebook = freepacktbook:claim_free_ebook']},
    zip_safe=False)
