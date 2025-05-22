# Log URL Generator

This script takes a log identifier in the format:
BUG-<instance_id>-<timestamp>-<session_id>

And generates a URL to the internal logging system with a ±15 minute window around the timestamp.

python url.py BUG-<instance_id>-<timestamp>-<session_id>

Example:
python url.py BUG-5e1d00bcc51bcd-20250520113149Z-abc123

This will open the corresponding URL in your default browser.
