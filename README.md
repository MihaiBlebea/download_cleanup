This script watches the /Downloads folder and moves files to their specific folder once saved here.

For the moment it works for:
- images "png", "jpg", "jpeg", "gif", "bmp" are saved to /Pictures
- ebooks "epub", "pdf", "mob", "azw", "azw3" are saved to /Ebooks folder

Install the script by running the `install.sh` script. This creates a crontab `/etc/cron.d/download_cleanup_cron` to start the script on reboot.

Uninstall the script by running the `uninstall.sh` script. This removes the crontab file `/etc/cron.d/download_cleanup_cron`. You can manually uninstall by removing this file.