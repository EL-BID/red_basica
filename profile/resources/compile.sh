#!/bin/bash

#install dependencies: sudo apt install pyqt5-dev-tools

pyuic5 profile_widget.ui -o ../views/ui/ProfileWidgetUi.py
echo "\n done!"