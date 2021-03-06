from setuptools import setup, find_packages
import os


README = "README.md"

base = os.path.dirname(__file__)
local = lambda x: os.path.join(base, x)

setup(
    name="jira-yaml",
    version="1.1.1",
    author="Nino Walker",
    author_email="nino.walker@gmail.com",
    description=(""),
    url='https://github.com/ninowalker/jira-yaml',
    license="BSD",
    packages=find_packages(exclude=['tests']),
    long_description="",
    install_requires=['jira==0.35', 'PyYAML>=3.10', 'docopt', 'mock'],
    test_suite='nose.collector',
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={'console_scripts': ['jywriter = jy.writer:main']}
)
