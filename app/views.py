# views.py
import ipdb
from flask import (Flask, flash, redirect, render_template, request, session,
    url_for)

from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from functools import wraps

# config
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from forms import QueryChakras

# import the models
from models import ChakraAttribute


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text, error), 'error')



@app.route('/',  methods=['GET', 'POST'])
def chakra_table():
    form = QueryChakras(request.form)

    current_view = db.session.query(ChakraAttribute)
    if request.method == 'GET':
        print form.chakra_number.data
        return render_template('chakras.html', form=form,
                               current_view=current_view)

    if request.method == 'POST':

        current_view = db.session.query(ChakraAttribute)

        if form.chakra_number.data != 'All':
            current_view = current_view.filter_by(
                chakra_number=form.chakra_number.data)

        if form.attribute_type.data != 'ALL':
            current_view = current_view.filter_by(
                attribute_type=form.attribute_type.data)

        return render_template('chakras.html',
            form=form,
            current_view=current_view)

