from flask import redirect, flash, url_for, request
from flask_login import login_user
from app.auth import register_service

from app.models.principal import Principal
from ..webapp import config

from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.github import make_github_blueprint, github

ggbp = make_google_blueprint(
    client_id=config.GOOGLE_OAUTH_CLIENT_ID,
    client_secret=config.GOOGLE_OAUTH_CLIENT_SECRET,
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile"],
    redirect_to='auth.profile')

ghbp = make_github_blueprint(
    client_id=config.GITHUB_OAUTH_CLIENT_ID,
    client_secret=config.GITHUB_OAUTH_CLIENT_SECRET,
    redirect_to='auth.profile'
)


@ggbp.route("/oauth")
def google_oauth():
    return oauth_authorize(provider_name='google',
        provider=google,
        login_url='google.login',
        userinfo_url='/oauth2/v1/userinfo')


@ghbp.route("/oauth")
def github_oauth():
    return oauth_authorize(provider_name='github',
        provider=github,
        login_url='github.login',
        userinfo_url='/user')


def oauth_authorize(provider_name, provider,
                           login_url, userinfo_url):
    if not provider.authorized:
        return redirect(url_for(login_url))

    userinfo = None
    principal:Principal = None
    try:
        resp = provider.get(userinfo_url)
        userinfo = resp.content
        principal = register_service.locate_user(provider_name, userinfo)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for(login_url))

    if not principal:
        principal = register_service.register_from_oauth(provider_name, userinfo)
        flash(f'Welcome ${principal.me.name}!', 'success')
    else:
        flash(
        'Logged in as name=%s using Google login' % (
           principal.username), 'success')

    login_user(principal)
    return redirect(request.args.get('next', url_for('home')))
