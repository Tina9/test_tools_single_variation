

from setuptools import setup, find_packages

setup(
    name='data_simulate',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sys',
        'os',
        'docopt',
        'concurrent',
        'subprocess',
        'random',
    ],
)
