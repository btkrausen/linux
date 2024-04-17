#!/bin/bash

# This script creates a timestamped file in the user's home directory

# Define file name with current timestamp
file_name="cron_job_$(date +'%Y-%m-%d_%H-%M-%S').txt"

# Create the file in the user's home directory
touch ~/"$file_name"

# End of script