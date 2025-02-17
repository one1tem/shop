import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from tools.gen_uid import gen_uid

from config.config import Base, session, engine


# Create DB-Tables

from models.project import Project

Base.metadata.create_all(engine)
