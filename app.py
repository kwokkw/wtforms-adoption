from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import PetForm

# TODO: import forms

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:Kwok17273185@localhost:5432/adopt"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = "secret_key"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.debug = True
debug = DebugToolbarExtension(app)

connect_db(app)
# db.drop_all()
db.create_all()


# The homepage list the pets
@app.route("/")
def home_page():
    """List all pets."""

    pets = Pet.query.all()
    return render_template("home.html", pets=pets)


# Add pet
@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """A form to add a pet."""

    form = PetForm()

    if form.validate_on_submit():

        data = {key: value for key, value in form.data.items() if key != "csrf_token"}
        pet = Pet(**data)
        db.session.add(pet)
        db.session.commit()
        flash(f"New pet {pet.name} Added!")
        return redirect("/")
    else:
        return render_template("add-pet-form.html", form=form)


@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_pet_form(id):
    """A form to edit a pet"""

    pet = Pet.query.get_or_404(id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        print("Form is valid, proceeding with submission.")

        # Update pet.
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.is_available = form.is_available.data

        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect("/")
    else:
        return render_template("edit-pet-form.html", pet=pet, form=form)
