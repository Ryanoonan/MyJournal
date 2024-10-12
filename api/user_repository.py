from typing import Optional
from orm_user import ORMUser
from sqlalchemy.orm import Session
from sqlalchemy import select, insert

from user import User

class UserRepository:
    def __init__(self, session : Session):
        self.session = session

    def get_user_by_username(self, username: str) -> Optional[ORMUser]:
        orm_user = self.session.execute(select(ORMUser).where(ORMUser.username == username)).scalars().one_or_none()
        return orm_user

    def add_user(self, user: ORMUser):
        self.session.add(user)
        self.session.commit()