# Setup

- [ UI `flask` replaced with `stream lint`](https://github.com/streamlit/streamlit)

## 1. Virtual python environment

```sh
python3 -m venv --upgrade-deps venv
source venv/bin/activate
```

```sh
python3 -m pip install flask
python3 -m pip install requests
python3 -m pip install streamlit
```

## 2. Set the environment variables

```sh
cat env_template > .env
```

* Edit the content in the `.env` file.

>Ensure the `redirect_uri` is configured in your `AppID` service

```sh
# AppID
export APPID_CLIENT_ID=
export APPID_CLIENT_SECRET=
export APPID_REDIRECT_URI="http://localhost:5000/auth_route"
export APPID_OAUTH_SERVER_URL=
export APPID_MGMT_TOKEN=

# IBM Cloud
export IBM_CLOUD_APIKEY=

# FlaskApp
export SESSION_SECRET_KEY=YOUR_SESSION_KEY
```

## 3. Set the environment variables

```sh
bash start_app.sh
```

## 4. AppID service configuration

* Set redirect URL (ensure to use the URL in the `AppIDAuthProvider` class)
* Create a role
* Register a user