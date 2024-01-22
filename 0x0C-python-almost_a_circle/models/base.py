#!/usr/bin/python3

class Base():
    _nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base._nb_objects = Base._nb_objects + 1
            self.id = Base._nb_objects
