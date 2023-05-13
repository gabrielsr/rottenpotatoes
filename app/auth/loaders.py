from ..models import Principal
from ..webapp import login_manager


@login_manager.user_loader
def load_user(uid):
    if not uid or uid == "None":
        return None
    return Principal.query.get(int(uid))


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get("email")
#     user = User.query.filter_by(email=email).first()
#     if not user:
#         return
#     return user


# @app.before_request
# def session_handler():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(minutes=1)
