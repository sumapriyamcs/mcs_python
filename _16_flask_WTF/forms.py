from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(
        label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Log In")


@app.route("/", methods=["GET", "POST"])
def home():
    form = contactForm()
    if form.validate_on_submit():
        print(f"Name:{form.name.data}, E-mail:{form.email.data},message:{form.message.data}")
    return render_template("new_contact.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)