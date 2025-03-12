from sun_calculator import SunCalculator
import time

def capture_image():
    # Your existing capture code here
    pass

def main():
    sun_calc = SunCalculator()
    
    while True:
        if sun_calc.is_dark():
            # It's dark enough to capture
            capture_image()
        else:
            # Wait for next sunset
            next_event = sun_calc.time_until_next_event()
            print(f"Waiting for {next_event['event']} in {next_event['time_until']}")
            # Sleep for a while before checking again
            time.sleep(300)  # Check every 5 minutes

if __name__ == "__main__":
    main()