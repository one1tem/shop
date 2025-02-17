from . import *

class Project(Base):
    __tablename__ = "project"
    uid = Column("uid", String, primary_key = True, default = gen_uid)
    name = Column("name", String)

    created_at = Column("created_at", DateTime, default = datetime.utcnow())
    updated_at = Column("updated_at", DateTime)
    
    #verantwortlich_uid = Column("verantwortlich_uid", ForeignKey('verantwortlich.uid'))
