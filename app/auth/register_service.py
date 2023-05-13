

from typing import Tuple
from app.helpers.get_fields import get_from_json_str
from app.models.credential import OauthCredential, PasswordCredential
from app.models.moviegoer import Moviegoer
from app.models.principal import Principal

from ..webapp import db, bcrypt

def register_from_oauth(provider:str, oauth_resp_content: str) -> Principal:
    try:
        user_id, name, email, picture = get_from_json_str(oauth_resp_content, 
                                                        'id', 'name', 'email', 'picture')
        principal = Principal(username=email)
        credential = OauthCredential(provider=provider, oauth_user_id=user_id, principal=principal)
        moviegoer = Moviegoer(name=name, email=email, principal=principal, picture=picture)
        credential.principal = principal
        db.session.add(credential)
        db.session.add(moviegoer)
        db.session.commit()
        return principal
    except Exception as e:
        raise Exception(f'Failed to register from oauth response {e}')
    
def locate_user(provider, userinfo) -> Principal or None:
    [user_id] = get_from_json_str(userinfo, 'id')
    credential = OauthCredential.query.filter_by(provider=provider, 
                                oauth_user_id=user_id).first()
    if not credential:
        return None
    else:
        return credential.principal

def check_pwd_credential(username, password) -> Tuple[Principal or None, str]:
    err_str = 'User and Password do not match'
    # principal_id = int(db.session.query(Principal.id).filter_by(username=username).first())
    try:
        credential = db.session.query(
            PasswordCredential
        ).join(
            Principal, 
            Principal.id == PasswordCredential.principal_id
        ).filter(Principal.username == username).first()
    except Exception as e:
        from ..webapp import app
        app.logger.error(f'Failed to check password credential {e}')
        return (None, 'Internal Error. Please try again later')

    if not credential:
        return (None, err_str)
    
    if not bcrypt.check_password_hash(credential.password, password):
        return (None, err_str)
    else:
        return (credential.principal, None)


def register_with_pwd(username, email, password):
    try:
        password_hash = bcrypt.generate_password_hash(password)
        principal = Principal(username=username)
        credential = PasswordCredential(
            password=password_hash,
            principal=principal
        )
        moviegoer = Moviegoer(name=username,
                            email=email,
                            principal=principal)
        db.session.add(credential)
        db.session.add(moviegoer)
        db.session.commit()
        return principal
    except Exception as e:
        raise Exception(f'Failed to register {e}')
    
def email_already_registered(email):
    exists = db.session.query(Moviegoer.id).filter_by(email=email).first()
    return exists is not None

def username_already_registered(username):
    exists = db.session.query(Principal.id).filter_by(username=username).first()
    return exists is not None