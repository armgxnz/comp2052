from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_mail import Mail, Message

app = Flask(__name__)

app.config["SECRET_KEY"] = "mi_clave_secreta"

class LoginForm(FlaskForm):
    name = StringField("Nombre",
        validators=[DataRequired(), Length(min=3)],
        render_kw={"placeholder": "Your name"})
    
    email = StringField("Email",
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": "Your email"})
    
    password = PasswordField("Password",
        validators=[DataRequired(message="La contraseña es obligatoria"), Length(min=3)],
        render_kw={"placeholder": "Your password"})
    
    submit = SubmitField("Login", 
        render_kw={"class": "btn btn-primary"}) 


@app.route("/", methods=["GET"])
def index():
    return login()

@app.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        message = f"Usuario: {form.email.data}"
        return render_template("home.html", message=message)
    
    return render_template("index.html.jinja2", form=form)

if __name__ == "__main__":
    app.run(debug=True)