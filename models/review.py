#!/usr/bin/python3
"""
Created by
@author: Jenaide Sibolie
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel
    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """
    place_id = ""
    user_id = ""
    text = ""
