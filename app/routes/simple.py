from flask import Blueprint, render_template, redirect
from ..forms import NewInstrument
from ..models import Instrument, db

bp = Blueprint('simple', __name__, '')

@bp.route('/')
def main_page():
    return render_template('main_page.html')

@bp.route('/new_instrument')
def get_simple_form():
    form = NewInstrument()
    return render_template('simple_form.html', form=form)


@bp.route('/new_instrument', methods=["POST"])
def post_simple_form():
    form = NewInstrument()
    if form.validate_on_submit():
        new_instrument = Instrument(
            date_bought=form.data['date_bought'],
            nickname=form.data['nickname'],
            year=form.data['year'],
            maker=form.data['maker'],
            type=form.data['type'],
            used=form.data['used']
        )
        db.session.add(new_instrument)
        db.session.commit()
        return redirect('/instrument_data')
    return "Bad Data"


@bp.route('/instrument_data')
def get_simple_form_data():
    instruments = Instrument.query.filter(Instrument.nickname.like('M%')).all()
    return render_template('simple_form_data.html', instruments=instruments)
