
import os
import sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)


# ----------8<---------- #
from tools.gen_uid import gen_uid
# ---------->8---------- #

# ----------8<---------- #
from config.config import session, Base, engine
# ---------->8---------- #

# ----------8<---------- #
from models.project import Project
# ---------->8---------- #

print("projects = session.query(Project).all()")

