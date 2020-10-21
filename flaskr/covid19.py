from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import requests

from werkzeug.exceptions import abort

bp = Blueprint('covid19', __name__)

@bp.route('/')
def index():
    return render_template('covid19/index.html')


@bp.route('/show', methods=('GET', 'POST'))
def show():
    days = request.form['days']
    error = None

    if not days:
        error = 'Days is required.'

    if not days.isnumeric():
        error = 'Days must be a number.'

    if error is not None:
        flash(error)
    else:
        result = requests.get('https://thevirustracker.com/free-api?global=stats')
        data = result.json()

        current_cases = data['results'][0]['total_new_cases_today']
        transmission_factor = 1.03
        balancer = 2551.54

        cases = []
        count = 0
        while count < int(days):                
            x = current_cases
            res = transmission_factor * x + balancer

            cases.append(res)
            current_cases = res
            count += 1
        
        return render_template('covid19/show.html', cases=cases)
            
    return redirect(url_for('covid19.index'))