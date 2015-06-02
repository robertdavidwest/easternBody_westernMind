# forms.py


from flask_wtf import Form
from wtforms import (TextField, DateField, IntegerField, SelectField,
                     PasswordField)
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QueryChakras(Form):


    attribute_type = SelectField('Attribute',
                           validators=[DataRequired()],
                           choices=[('ALL', 'ALL'),
                                ('ELEMENT', 'ELEMENT'),
                                ('NAME', 'NAME'),
                                ('PURPOSE', 'PURPOSE'),
                                ('ISSUES', 'ISSUES'),
                                ('COLOR', 'COLOR'),
                                ('LOCATION', 'LOCATION'),
                                ('IDENTITY', 'IDENTITY'),
                                ('ORIENTATION', 'ORIENTATION'),
                                ('DEMON', 'DEMON'),
                                ('DEVELOPMENT STAGE', 'DEVELOPMENT STAGE'),
                                ('DEVELOPMENTAL TASKS', 'DEVELOPMENTAL TASKS'),
                                ('BASIC RIGHTS', 'BASIC RIGHTS'),
                                ('BALANCED CHARACTERISTICS', 'BALANCED CHARACTERISTICS'),
                                ('DEFICIENCY', 'DEFICIENCY'),
                                ('EXCESS', 'EXCESS'),
                                ('PHYSICAL MALFUNCTIONS', 'PHYSICAL MALFUNCTIONS'),
                                ('HEALING PROCESS', 'HEALING PROCESS'),
                                ('AFIRMATIONS', 'AFIRMATIONS'),
                                ('DEVELOPMENTAL STAGE', 'DEVELOPMENTAL STAGE'),
                                ('TRAUMAS AND ABUSES', 'TRAUMAS AND ABUSES'),
                                ('HEALING PRACTICES', 'HEALING PRACTICES'),
                                ('AFFIRMATIONS', 'AFFIRMATIONS'),
                                ('ORENTATION', 'ORENTATION'),
                                ('DEVELOPMENT TASK', 'DEVELOPMENT TASK'),
                                ('DEVELOPMENTAL  STAGE', 'DEVELOPMENTAL  STAGE'),
                                ('DEVELOPMENTAL TASK', 'DEVELOPMENTAL TASK'),
                                ('HEALING PRACTISES', 'HEALING PRACTISES')
                                ])

    chakra_number = SelectField('Chakra',
                           validators=[DataRequired()],
                           choices=[('All', 'All'),
                                    ('First', 'First'), ('Second', 'Second'),
                                    ('Third', 'Third'), ('Fourth', 'Fourth'),
                                    ('Fifth', 'Fifth'), ('Sixth', 'Sixth'),
                                    ('Seventh', 'Seventh')
                               ]
                           )
