#!/usr/bin/python3
"""
This module defines the Review class herited from BaseModel
"""

from models.base_model import BaseModel
import json


class Review(BaseModel):

    """Review class for Airbnb clone project"""
    place_id = ""
    user_id = ""
    text = ""
