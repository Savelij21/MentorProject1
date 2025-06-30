
from sqlalchemy import Integer, String, Column, BigInteger
from database import Base


class User(Base):
    __tablename__ = "users_customuser"

    id = Column(BigInteger, primary_key=True)
    username = Column(String(150), unique=True)
    phone = Column(String(50), unique=True)
    tg_id = Column(Integer, unique=True, nullable=True)
