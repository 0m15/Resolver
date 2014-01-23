Resolver
========

A fast and extensible Music Content Resolver in Python.
It essentially lets you search for a track (a string formed by "artist + track" works better) on any Provider you register.

Installation
============

1. `git clone https://github.com/zimok/Resolver.git`
2. `cd Resolver`
3. `python setup.py install`

Dependencies
============

1. Kenneth Reitz's `requests` 
2. Requests oAuth lib

Features
========

- Supports multiple concurrent requests by using python processes
- Supports oAuth authentication (look at Rdio resolver class to see a working implementation)
- Lets you write your Resolver in a few lines of python code
- Supports methods to match strings and get the correct results

Todo
====

- Enhance documentation

Demo
====

Checkout `demo.py` to see a working example or run it:
    python demo.py