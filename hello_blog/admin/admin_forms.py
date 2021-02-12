from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


# Form to add a category.
class AddCategoryForm(FlaskForm):
    category_name = StringField("Add Category",
                                validators=[DataRequired(),
                                            length(min=3, max=20)])
    submit = SubmitField("Add")


# Form to delete the category
class EditCategoryForm(FlaskForm):
    category_name = StringField("Edit Category",
                                validators=[DataRequired(),
                                            length(min=3, max=20)])
    submit = SubmitField("Update")


# Form to delete category
class DeleteCategoryForm(FlaskForm):
    submit = SubmitField("Delete")
