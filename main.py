from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect
from login_form import LoginForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.debug = True
# The secret key is needed to keep the client-side sessions secure.
app.config['SECRET_KEY'] = 'any_string_you_want'  
csrf = CSRFProtect(app) 
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run()