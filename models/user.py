#!/usr/bin/python3
"""
This module defines the User class herited from BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):

    """User class for Airbnb clone project"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
