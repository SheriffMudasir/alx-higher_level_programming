#!/usr/bin/python3
"""This module contain a base class"""
import json


class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This function returns a dictionary as a json file"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """This function writes the JSON string representation of list_objs to a file"""
        if list_objs:
            result = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            with open(f'{cls.__name__}.json', 'w') as file:
                file.write(result)
        else:
            with open(f'{cls.__name__}.json', 'w') as file:
                file.write("[]")


    @staticmethod
    def from_json_string(json_string):
        """ This function returns the list of the JSON string representation json_string:"""
        if not json_string:
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary): 
        """This function returns an instance with all attributes already set:"""
        obj = cls(1, 1)

        obj.update(**dictionary)
        return obj

    def load_from_file(cls):
        """This method load a json file and return list of instances"""
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj) for obj in json_list] if json_list else []
                return instances
        except FileNotFoundError:
            return []

        





