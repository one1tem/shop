import uuid

import os, sys


# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)

#from config.config import Base, session, engine

#from models.user import User

'''gerade nicht in benutzung
def verify_uid(table, uid):
    data = session.query(table).all()
    if uid in data:
        print("uid vergeben")
        return False
    return True
'''

def gen_uid():
    '''
    - generates random unique ID
    - return only the first part
    '''
    uid = str(uuid.uuid4()).split("-")[0]
    '''
    while verify_uid('User', uid) == False:
        uid = str(uuid.uuid4()).split("-")[0]
    '''
    return uid

