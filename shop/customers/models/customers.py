from . import *

class Customers(Base):
    __tablename__ = "customers"
    uid = Column("uid", String, primary_key = True, default = gen_uid)
    username = Column("username", String)
    name = Column("name", String)
    password = Column("password", String)

    created_at = Column("created_at", DateTime, default = datetime.utcnow())
    updated_at = Column("updated_at", DateTime)
    
    #verantwortlich_uid = Column("verantwortlich_uid", ForeignKey('verantwortlich.uid'))
