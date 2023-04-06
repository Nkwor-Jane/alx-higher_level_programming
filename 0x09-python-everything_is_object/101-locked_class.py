#!/usr/bin/python3

class LockedClass:
    """"class with no class or object attribute, that prevents a user
   from dynamically creating new instance attributes excpt if the new
   instance attribute is called first_name"""

    __slots__ = 'first_name'
