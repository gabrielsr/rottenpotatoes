
from typing import Optional
from . import db
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column
from .principal import Principal

from sqlalchemy.ext.declarative import declarative_base


class Credential(db.Model):
    __tablename__ = "credentials"
    id: Mapped[int] = mapped_column(primary_key=True)
    principal_id: Mapped[int] = mapped_column(ForeignKey("principals.id"))
    principal: Mapped[Principal] = relationship("Principal", lazy='joined')
    type: Mapped[String] = mapped_column(String(20))

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "credential"
    }

class PasswordCredential(Credential):
    password: Mapped[Optional[String]] = mapped_column(String(300))

    __mapper_args__ = {
        "polymorphic_identity": "password"
    }
    def __repr__(self):
        return f'PasswordCredential ({self.id}, {self.principal_id})'

class OauthCredential(Credential):
    oauth_user_id: Mapped[Optional[int]] = mapped_column()
    provider: Mapped[Optional[String]] = mapped_column(String(20))
    token: Mapped[Optional[String]] = mapped_column(String(300))


    __mapper_args__ = {
        "polymorphic_identity": "oauth"
    }
    def __repr__(self):
        return f'OauthCredential ({self.id}, {self.oauth_user_id}, {self.provider})'
    


