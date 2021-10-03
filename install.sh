#!/bin/bash

COMMAND="@reboot root /home/mihaiblebea/Projects/Python/download_cleanup/download_cleanup.py > /dev/null 2>&1"

# Check if this is not already installe
CRON_FILE=/etc/cron.d/download_cleanup_cron
if test -f "$CRON_FILE"; then
	echo "Already installed. Run uninstall.sh first."
	exit
fi

# Run the command with sudo
if [ $EUID != 0 ]; then
    sudo "$0" "$@"
    exit $?
fi

python3 -m venv virtualenv &&\
source virtualenv/bin/activate &&\
pip3 install -r requirements.txt &&\
deactivate &&\
echo "${COMMAND}" > $CRON_FILE