# Import the dependencies.
import pandas as pd
from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, text

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
def __init__(self):
    self.engine = create_engine("sqlite:///Resources/hawaii.sqlite")
    self.Passenger = self.createPassenger()

# Declare a Base using `automap_base()`

# Use the Base class to reflect the database tables


# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`


# Create a session


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
