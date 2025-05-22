import sys
import webbrowser
from datetime import datetime, timedelta
import urllib.parse

def parse_input(input_str):
    parts = input_str.split('-')
    if len(parts) < 4 or not parts[2].endswith('Z'):
        raise ValueError("Input must be in the format: BUG-<instance_id>-<timestamp>-<session_id>")
    
    instance_id = parts[1]
    timestamp = parts[2]
    return instance_id, timestamp

def build_log_url(instance_id, timestamp_str, delta_minutes=15):
    dt = datetime.strptime(timestamp_str, "%Y%m%d%H%M%SZ")
    start_dt = dt - timedelta(minutes=delta_minutes)
    end_dt = dt + timedelta(minutes=delta_minutes)

    # Format timestamps in ISO 8601
    start_str = start_dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_str = end_dt.strftime("%Y-%m-%dT%H:%M:%SZ")

    # URL encode the timestamps
    start_encoded = urllib.parse.quote(start_str, safe='')
    end_encoded = urllib.parse.quote(end_str, safe='')

    url = (
        f"http://logz0.corp.ts.net:9431/logs"
        f"?start={start_encoded}"
        f"&end={end_encoded}"
        f"&instances={instance_id}"
        f"&json=false&service=&match="
    )
    return url

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_log_url.py <BUG-input-string> [delta_minutes]")
        sys.exit(1)

    input_str = sys.argv[1]
    delta = int(sys.argv[2]) if len(sys.argv) > 2 else 15

    try:
        instance_id, timestamp = parse_input(input_str)
        url = build_log_url(instance_id, timestamp, delta)
        print("Opening URL:", url)
        webbrowser.open(url)
    except ValueError as e:
        print(f"Error: {e}")

