from flask import redirect, flash, url_for, request
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import login_user

from ..models.user import User, from_oath_google
from ..webapp import db, config


google_blueprint = make_google_blueprint(
    client_id=config.GOOGLE_OAUTH_CLIENT_ID,
    client_secret=config.GOOGLE_OAUTH_CLIENT_SECRET,
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile"],
    redirect_to='.google_login')


@google_blueprint.route("/google-login")
@google_blueprint.route("/google/authorized")
def google_login():
    if not google.authorized:
        return redirect(url_for("google.login"))

    resp = google.get("/oauth2/v1/userinfo")

    user = User.query.filter_by(username=resp.json()["email"]).first()
    if not user:
        user = from_oath_google(resp.content)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome ${user.username}!', 'success')

    login_user(user)
    flash(
        'Logged in as name=%s using Google login' % (
           user.given_name), 'success')
    return redirect(request.args.get('next', url_for('home')))

