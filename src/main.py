from config_manager import create_or_load_config
from paths import DATA_DIR, LOGS_DIR

def main():
    # Load configuration
    config = create_or_load_config()

    # Print the base directory and log directory as an example
    print(f"Base directory: {DATA_DIR}")
    print(f"Log directory: {LOGS_DIR}")

    # Example: Access configuration parameters
    station_id = config["System"]["station_id"]
    print(f"Station ID: {station_id}")

if __name__ == "__main__":
    main()
