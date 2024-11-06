from setuptools import setup, find_packages


setup(
    name='Trello',
    packages=find_packages(),
    install_requires=[
        'pytest==8.3.3',
        'allure-pytest==2.13.5',
        'pytest==8.3.3',
        'requests==2.32.3',
        'setuptools==75.3.0'
    ]
)