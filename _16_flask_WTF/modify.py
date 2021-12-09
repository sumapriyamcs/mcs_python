from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "any-string-you-want-just-keep-it-secret"


class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Log In")


@app.route("/", methods=["GET", "POST"])
def home():
    cform = contactForm()
    if cform.validate_on_submit():
        print(f"Name:{cform.name.data}, E-mail:{cform.email.data}, message:{cform.message.data}")
    return render_template("boot_contact.html", form=cform)


if __name__ == '__main__':
    app.run(debug=True)
