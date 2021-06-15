from sqlalchemy import (
    Column,
    String,
    Integer,
    Boolean
)

from src.config.database import Base


class Tenant(Base):

    __tablename__ = 'tenants'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String, unique=True)
    domain = Column(String, unique=True)
    is_active = Column(Boolean, unique=True)
