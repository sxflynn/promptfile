from setuptools import setup, find_packages

setup(
    name='promptfile',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'promptfile = promptfile.__main__:main',
        ],
    },
)