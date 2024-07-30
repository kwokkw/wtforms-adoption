from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    BooleanField,
    IntegerField,
    SelectField,
)
from wtforms.validators import InputRequired, Optional, URL, NumberRange


# Add Validation
class PetForm(FlaskForm):
    """Form to add or edit a pet."""

    # The species should be either “cat”, “dog”, or “porcupine”
    name = StringField(
        "Pet Name",
        validators=[InputRequired(message="Pet name is required.")],
    )
    species = SelectField(
        "Species",
        choices=[
            ("dog", "Dog"),
            ("cat", "Cat"),
            ("porcupine", "Porcupine"),
        ],
    )

    # The photo URL must be a URL (but it should still be able to be optional!)
    photo_url = StringField(
        "URL", validators=[Optional(), URL(message="Must be a valid URL.")]
    )

    notes = StringField("Notes")

    # the age should be between 0 and 30, if provided
    age = IntegerField(
        "Age",
        validators=[
            Optional(),
            NumberRange(min=0, max=30, message="Age should be between 0 and 30."),
        ],
    )

    is_available = BooleanField("Available to adopt")
