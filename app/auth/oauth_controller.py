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
    redirect_to='auth.google.oauth')

ghbp = make_github_blueprint(
    client_id=config.GITHUB_OAUTH_CLIENT_ID,
    client_secret=config.GITHUB_OAUTH_CLIENT_SECRET,
    redirect_to='auth.github.oauth'
)


@ggbp.route("/google/oauth", endpoint='oauth')
def google_oauth():
    return oauth_authorize(provider_name='google',
                           provider=google,
                           userinfo_url='/oauth2/v1/userinfo')


@ghbp.route("/github/oauth", endpoint='oauth')
def github_oauth():
    return oauth_authorize(provider_name='github',
                           provider=github,
                           userinfo_url='/user')


def oauth_authorize(provider_name, provider, userinfo_url):
    if not provider.authorized:
        # login route auto created my flask dance
        return redirect(url_for('.login'))

    userinfo = None
    principal: Principal = None
    try:
        resp = provider.get(userinfo_url)
        userinfo = resp.content
        principal = register_service.locate_user(provider_name, userinfo)
    except Exception as e:
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('auth.session.login'))

    if not principal:
        principal = register_service.register_from_oauth(
            provider_name, userinfo)
        flash(f'Welcome ${principal.me.name}!', 'success')
    else:
        flash(
            f'Logged in as {principal.username} using {provider_name} login',
            'success')

    login_user(principal)
    return redirect(request.args.get('next', url_for('home')))
