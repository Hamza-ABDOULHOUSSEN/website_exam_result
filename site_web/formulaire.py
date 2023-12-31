from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required


class IdForm(Form):
    id = IntegerField(id = 'ID du candidat', validators = [input_required()])


class NameForm(Form):
    name = StringField(id = 'Nom du candidat', validators = [input_required()])
    FirstName = StringField(id = 'Prénom du candidat', validators = [input_required()])


class IneForm(Form):
    INE = StringField(id = 'INE du candidat', validators = [input_required()])


class IdentityForm(Form):
    INE = StringField(id = 'INE du candidat', validators = [input_required()])
    name = StringField(id = 'Nom du candidat', validators = [input_required()])
    FirstName = StringField(id = 'Prénom du candidat', validators = [input_required()])
