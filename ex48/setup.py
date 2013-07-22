try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 48 from Learn Python the Hard Way',
    'author': 'auroricshiva',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Exercise 48 - Advanced User Input'
}

setup(**config)
