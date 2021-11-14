#!/usr/bin/python3
"""
This module contains the implementation
of the FileStorage class which serializes
instances to a JSON file and deserializes
JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    The class FileStorage serializes and deserializes
    json file
    """
    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """Return dictionary of <class>.<id>: object instance"""
        return self.__objects

    def new(self, obj):
        """Add a new object to existing dictionary of instances"""
        if obj:
            key = '{}.{}'.format(obj.__class__.name, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save object dictionaries to json files"""
        my_dict = {}
        for key, obj in self.__objects.items():
            if type(obj) is dict:
                my_dict[key] = obj
            else:
                my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Convert obj dictionaries in the json file to
        instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for key, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
