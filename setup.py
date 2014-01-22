import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "rslvr",
    version = "0.0.1",
    author = "Simone C.",
    author_email = "feuer23@autistici.org",
    description = ("An extensible music content resolver"),
    license = "BSD",
    keywords = "content music resolver",
    url = "http://zimok.github.com",
    packages=['rslvr', 'rslvr.resolvers'],
    long_description=read('README.md'),
)