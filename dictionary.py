# dictionary example
# {"days": 20, "unit": "hours", "message": "all good"}
# import dicthelper
# import modulename import all the available functions
# instead do this - from modulename import funcName
# from modulename import *
# import modulename as abc
# abc.
# built-in modules eg import math
# from datetime import datetime, timezone
# import os
# import logging
# package vs modules = module is a python file having func varibles etc
# while package is collection of modules
# PyPI = The Python Package Index is a repository [storage] for third party packages
# people can publish packages to this repo , so it becomes available for everyone to use
# pip is a package manager tool that helps to install packages
# pip install Django

from dicthelper import validate, input_msg

user_input = ""
while user_input != "exit":
    user_input = input(input_msg)
    formatted_input = user_input.split(":")
    print(formatted_input)
    dict1 = {"days": formatted_input[0], "unit": formatted_input[1]}
    print(dict1)
    # dicthelper.validate(dict1) if importing whole module and not particular func , variables
    # from modulename import * if using this then also no need to use modulename again while accessing variables and functionName with .
    validate(dict1)
