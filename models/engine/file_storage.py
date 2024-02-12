#!/usr/bin/python3
"""A module that defines a class FileStorage"""
import json


class FileStorage:
    """A class FileStorage that serializes and deserializes instances"""
    __file_path = "./file.json"
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        """A method that sets obj in __object"""
        self.__objects[self.__class__.__name__.id] = obj

    def save(self):
        """A method thats serializes the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as dan:
            dan = json.dump(self.__objects)

    def reload(self):
        """A method that deserializes the JSON file"""
        with open(FileStorage.__file_path, "r") as guv:
            self.__object = json.load(guv)
