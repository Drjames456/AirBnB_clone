#!/usr/bin/python3
"""
A module that defines a base class called BaseModel that
defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A class called BaseModel that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """A constructor for the instance of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                elif key == 'created_at':
                    self.key = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.key = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.key = value
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A method that returns a string representation of an object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A method that updates the instance time of creation"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """A method that create an instance dictionary"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
