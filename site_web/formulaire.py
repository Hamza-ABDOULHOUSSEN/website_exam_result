from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required


class IdForm(Form):
    id = IntegerField('ID du candidat', validators = [input_required()])


class NameForm(Form):
    name = StringField('Nom du candidat', validators = [input_required()])
    FirstName = StringField('Prénom du candidat', validators = [input_required()])


class IneForm(Form):
    INE = StringField('INE du candidat', validators = [input_required()])
