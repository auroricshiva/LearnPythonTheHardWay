try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 47 from Learn Python the Hard Way',
    'author': 'R. Liang',
    'url': 'http://rickyliang.com',
    'download_url': 'http://rickyliang.com/downloads',
    'author_email': 'rickyliang@rickyliang.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Exercise 47'
}

setup(**config)
