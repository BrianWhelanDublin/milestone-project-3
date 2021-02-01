from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtf.validators import Datarequired, length


class AddCategoryForm(FlaskForm):
    category_name = StringField("Add Category",
                                validators=[Datarequired(),
                                            length(min=3, max=20)])
    submit = SubmitField("Add Category")
