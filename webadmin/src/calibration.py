from astral.sun import sun
from astral import LocationInfo
import pytz
from datetime import datetime, timedelta
import configparser

class CalibrationScheduler:
    def __init__(self, config_path='../config.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        
        # Get location for sun calculations
        self.latitude = float(self.config['System']['latitude'])
        self.longitude = float(self.config['System']['longitude'])
        
        self.location = LocationInfo(
            latitude=self.latitude,
            longitude=self.longitude,
            timezone="UTC"
        )

    def get_calibration_schedule(self, date=None):
        """Calculate optimal calibration times based on sunset"""
        if date is None:
            date = datetime.now(pytz.UTC)
            
        s = sun(self.location.observer, date=date)
        civil_twilight_end = s['dusk']
        sunset = s['sunset']
        
        # Schedule:
        # 1. Flats: During civil twilight (sky still bright enough)
        # 2. Bias/Dark: Just after civil twilight (dark enough)
        schedule = {
            'flat_start': sunset - timedelta(minutes=20),  # Before sunset
            'flat_end': sunset - timedelta(minutes=5),
            'dark_start': civil_twilight_end,
            'dark_end': civil_twilight_end + timedelta(minutes=15),
            'observation_start': civil_twilight_end + timedelta(minutes=20)
        }
        
        return schedule