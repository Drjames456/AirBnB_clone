#!/usr/bin/python3
"""A module that defines a class FileStorage"""
import json
import importlib


class FileStorage:
    """A class FileStorage that serializes and deserializes instances"""
    __file_path = "file.json"
    __objects = {}
    def all(self):
        return self.__objects

    def new(self, obj):
        """A method that sets obj in __object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """A method thats serializes the JSON file"""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """A method that deserializes the JSON file"""
        try:
            with open(self.__file_path, "r") as guv:
                data = json.load(guv)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                module = importlib.import_module('models.base_model')
                class_ = getattr(module, class_name)
                instance = class_(**value)
                self.__objects[key] = instance
        except FileNotFoundError:
            pass
