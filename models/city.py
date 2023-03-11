#!/usr/bin/python3
"""
@author: Jenaide Sibolie
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel
    Attributes:
        name (str): Public class attribute for City's name
        state_id (str): Public class attribute for City's state_id
    """
    name = ""
    state_id = ""
