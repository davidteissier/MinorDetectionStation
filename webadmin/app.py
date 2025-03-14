from flask import Flask, render_template, request, flash, redirect, url_for
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.sun_calculator import SunCalculator
import datetime
import configparser
from pathlib import Path
import secrets
import pytz

app = Flask(__name__)
# Add secret key for session management
app.secret_key = secrets.token_hex(16)

# Load configuration
config = configparser.ConfigParser()
config.read('../config.ini')

# Ensure admin data directory exists
admin_data_path = Path('../' + config['WebAdmin']['data_folder'])
admin_data_path.mkdir(parents=True, exist_ok=True)

@app.route('/')
def home():
    sun_calc = SunCalculator()
    next_event = sun_calc.time_until_next_event()
    
    info = {
        'name': 'Minor Detection Station',
        'version': '1.0.0',
        'station_id': config['System']['station_id'],
        'description': config['System']['description'],
        'next_session': {
            'event': next_event['event'],
            'time_until': next_event['time_until'],
            'timestamp': next_event['timestamp'].strftime('%Y-%m-%d %H:%M:%S %Z')
        }
    }
    return render_template('home.html', info=info)

def save_config(config):
    with open('../config.ini', 'w') as configfile:
        config.write(configfile)

def validate_parameters(form):
    errors = []
    # Validate latitude (-90 to 90)
    try:
        lat = float(form['latitude'])
        if not -90 <= lat <= 90:
            errors.append("Latitude must be between -90 and 90 degrees")
    except ValueError:
        errors.append("Latitude must be a number")

    # Validate longitude (-180 to 180)
    try:
        lon = float(form['longitude'])
        if not -180 <= lon <= 180:
            errors.append("Longitude must be between -180 and 180 degrees")
    except ValueError:
        errors.append("Longitude must be a number")

    # Validate altitude (positive number)
    try:
        alt = float(form['altitude'])
        if alt < 0:
            errors.append("Altitude must be a positive number")
    except ValueError:
        errors.append("Altitude must be a number")

    return errors

@app.route('/parameters', methods=['GET', 'POST'])
def parameters():
    if request.method == 'POST':
        errors = validate_parameters(request.form)
        if not errors:
            try:
                config['System']['station_id'] = request.form['station_id']
                config['System']['latitude'] = request.form['latitude']
                config['System']['longitude'] = request.form['longitude']
                config['System']['altitude'] = request.form['altitude']
                config['Capture']['camera_model'] = request.form['camera_model']
                config['Capture']['exposure_time'] = request.form['exposure_time']
                
                save_config(config)
                flash('Parameters saved successfully!', 'success')
            except Exception as e:
                flash(f'Error saving parameters: {str(e)}', 'error')
        else:
            for error in errors:
                flash(error, 'error')
        
    return render_template('parameters.html', config=config)

if __name__ == '__main__':
    app.run(
        host=config['WebAdmin']['host'],
        port=int(config['WebAdmin']['port']),
        debug=True
    )