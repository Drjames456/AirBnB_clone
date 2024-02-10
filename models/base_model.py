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
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dan = self.__dict__.copy()
        dan["created_at"] = self.created_at.isoformat()
        dan["updated_at"] = self.updated_at.isoformat()
        dan["__class__"] = self.__class__.__name__
        return dan
