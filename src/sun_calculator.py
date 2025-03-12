from astral import LocationInfo
from astral.sun import sun
from datetime import datetime, timedelta
import pytz
import configparser

class SunCalculator:
    def __init__(self, config_path='config.ini'):  # Changed from '../config.ini'
        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self.timezone = pytz.UTC
        
        # Get station location from config
        self.latitude = float(self.config['System']['latitude'])
        self.longitude = float(self.config['System']['longitude'])
        self.elevation = float(self.config['System']['elevation'])
        self.station_id = self.config['System']['station_id']
        
        # Create location object
        self.location = LocationInfo(
            name=f"Station_{self.station_id}",
            region="MON Network",
            latitude=self.latitude,
            longitude=self.longitude,
            timezone="UTC"
        )

    def get_sun_times(self, date=None):
        if date is None:
            date = datetime.now(self.timezone)
            
        s = sun(self.location.observer, date=date)
        return {k: v.astimezone(self.timezone) for k, v in s.items()}

    def time_until_next_event(self):
        now = datetime.now(self.timezone)
        times = self.get_sun_times()
        
        if now < times['sunset']:
            return {
                'event': 'sunset',
                'time_until': times['sunset'] - now,
                'timestamp': times['sunset']
            }
        else:
            tomorrow = now + timedelta(days=1)
            tomorrow_times = self.get_sun_times(tomorrow)
            return {
                'event': 'sunrise',
                'time_until': tomorrow_times['sunrise'] - now,
                'timestamp': tomorrow_times['sunrise']
            }

    def is_dark(self):
        """Check if it's currently dark enough for observation"""
        now = datetime.now(self.timezone)
        times = self.get_sun_times()
        return now > times['dusk'] or now < times['dawn']