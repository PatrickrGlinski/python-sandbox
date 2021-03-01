try:
    from setuptools import setup
except: ImportError:
    from distutils.core import setup


config = {
    'description': 'Project Description',
    'author': 'Patrick Glinski',
    'url': 'url to get project',
    'download_url': 'Where to download',
    'author_email': 'patrickrglinski@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectName'
}

setup(**config)