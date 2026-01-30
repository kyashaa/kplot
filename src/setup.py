from setuptools import setup, find_packages

NAME = 'kplot'
DESCRIPTION = "Expanded plotter and optimizer for analysis/paper"
AUTHOR = 'Kjasha (K&K)'
AUTHOR_EMAIL = ''
URL = 'https://github.com/kyashaa/kplot'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/kyashaa/kplot'
PYTHON_REQUIRES = ">=3.9"
VERSION = '1.0.1'

INSTALL_REQUIRES = [
    'matplotlib>=3.3.4',
    'numpy >=1.20.3',
    'pandas>=1.2.4',
    'scipy>=1.6.3',
]

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    description=DESCRIPTION,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES
)