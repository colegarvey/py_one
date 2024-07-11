# Used to install project 
# 'pip list' to check all packages

try: # DEFAULT SETUP
    from setuptools import setup
except:
    from distutils.core import setup

config = {
    'description':'Python Software Development Project',
    'author':'Cole Garvey',
    'url':'website url here',
    'download_url':'download url here',
    'author_email':'colemiester19@outlook.com',
    'version':'0.1',
    'install_requires':['pytest'],
    'packages':['src'],
    'scripts':[],
    'name':'py_one'
}

setup(**config)