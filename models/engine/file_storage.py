#!/usr/bin/python3
"""FileStorage Class"""
import json
from os import path
from models.base_model import BaseModel


class FileStorage():
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key"""
        (self.__objects)["{}.{}".format(type(obj).__name__, obj.id)] = obj
    
    def save(self):
        new = {}
        for k, v in self.__objects.items():
            new[k] = v.to_dict() 
        with open(self.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new))

    def reload(self):
        if path.exists(self.__file_path):
             with open(self.__file_path, "r", encoding="utf-8") as f:
                 loaded = json.loads(f.read())
             for k, v in loaded.items():
                self.__objects[k] = eval(v["__class__"])(**v)
            
