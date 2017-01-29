try:
    from setuptools import setup
except:
    from distutils.core import setup


config = {
    'description': 'a project to demonstrate, Project skeleton, py.test, automation',
    'author': 'Hicham Ichkantana',
    'url': 'None',
    'download_url': 'None',
    'author_email': 'hishamo@outlook.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['word_count'],
    'scripts': [],
    'name': 'word_count'
}

setup(**config)
