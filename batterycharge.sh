#!/bin/bash

# Laptop battery info
timeout 30s upower --monitor-detail > /home/tanay/automationScripts/file1
if cat /home/tanay/automationScripts/file1 | grep -q "fully"; then
    paplay /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg
    paplay /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg
    paplay /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg
fi

