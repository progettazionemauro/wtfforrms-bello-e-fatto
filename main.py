from flask import Flask
# from app import app
from flask import render_template, request
from forms import ContactForm, SignupForm

app = Flask(__name__)
#app.config["EXPLAIN_TEMPLATE_LOADING"] = True
app.config['SECRET_KEY'] = '1234'

@app.route("/")
def home():
    """Landing page."""
    return render_template(
        "indice.html", title="Flask-WTF tutorial"
    )


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Standard `contact` form."""
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "contact.jinja2.html", form=form, title="Contact Form"
    )


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """User sign-up form for account creation."""
    form = SignupForm()
    if form.validate_on_submit():
        return redirect(url_for("success"))
    return render_template(
        "signup.jinja2.html", form=form, title="Signup Form"
    )


@app.route("/success", methods=["GET", "POST"])
def success():
    """Generic success page upon form submission."""
    return render_template("success.jinja2.html")
app.run(host='0.0.0.0', port=81)




