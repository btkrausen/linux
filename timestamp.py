#!/usr/bin/env python3

import os
from datetime import datetime

# Define file name with current timestamp
file_name = f"cron_job_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Define the path to the user's home directory
home_dir = os.path.expanduser("~")

# Create the full path to the file
file_path = os.path.join(home_dir, file_name)

# Create the file in the user's home directory
open(file_path, 'a').close()