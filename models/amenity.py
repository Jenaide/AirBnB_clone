#!/usr/bin/python3
"""
Created by
@author: Jenaide Sibolie
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel
    Attribute:
        name (str): Public class attribute for Amenity's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        init method for Amenity class

        Attr:
            args (list): the list of arguments
            kwargs (dict): a dictionary with arguemnts
        """
        super().__init__(*args, **kwargs)
