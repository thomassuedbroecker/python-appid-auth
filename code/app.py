from flask import redirect, request, render_template

from auth import AppIDAuthProvider

auth = AppIDAuthProvider()
flask = auth.flask

@flask.route("/")
def index():
    print(f"**Log: 'index_route' content!")
    return redirect("/auth_route")

@flask.route("/auth_route", methods=['GET'])
@auth.check
def auth_route():
    print(f"**Log: 'auth_route' content!")
    print(f"**Log: 'auth_route' args {request}!")
    return render_template('auth_route.html')
    #f"This 'auth_route' requires authentication and authorization - Powered by IBM Cloud App ID!"

@flask.route("/noauth_route", methods=['GET'])
def noauth_route():
    print(f"**Log: 'noauth_route' content!")
    print(f"**Log: 'noauth_route' args {request}!")
    return "This route is open to all!"

if __name__ == "__main__":
    #flask.run(host="0.0.0.0")
    flask.run(host="localhost")
