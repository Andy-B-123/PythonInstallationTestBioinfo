# setup.py

from setuptools import setup, find_packages

setup(
    name='HelloScript',
    version='1.0.0',
    description='A simple Python script that prints "Hello, world!"',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/yourrepository',
    py_modules=['Hello'],
    install_requires=[
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'hello = Hello:hello',
        ],
    },
)
