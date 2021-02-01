from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class AddCategoryForm(FlaskForm):
    category_name = StringField("Add Category",
                                validators=[DataRequired(),
                                            length(min=3, max=20)])
    submit = SubmitField("Add")


class EditCategoryForm(FlaskForm):
    category_name = StringField("Edit Category",
                                validators=[DataRequired(),
                                            length(min=3, max=20)])
    submit = SubmitField("Update")
