#!/usr/bin/python3
"""
This module defines the City class herited from BaseModel
"""

from models.base_model import BaseModel
import json


class City(BaseModel):

    """City class for Airbnb clone project"""
    state_id = ""
    name = ""
