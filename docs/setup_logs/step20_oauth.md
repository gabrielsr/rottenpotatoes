
# Add Flask-Dance

`poetry add flask-dance`

# Setup Google OAuth

Create a blueprint for handling auth with Google in
`app/oauth.py`.

# Create App on Google Cloud

On https://console.cloud.google.com/apis/credentials

Create a Oauth 2.0 Client
Get Client ID and Secret Key
Setup as an authorized redirect url:
`http://127.0.0.1:5000/auth/google/authorized`


# Create App on Github

On Github > Settings > Developer Settings > OAuth Apps

https://github.com/settings/developers

Create App
Get Client ID and Secret Key
Configure as an authorized redirect url:
`http://127.0.0.1:5000/auth/github/authorized`