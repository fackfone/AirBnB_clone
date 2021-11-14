#!/usr/bin/python3
"""
This module defines the Amenity class herited from BaseModel
"""

from models.base_model import BaseModel
import json


class Amenity(BaseModel):

    """Amenity class for Airbnb clone project"""
    name = ""
