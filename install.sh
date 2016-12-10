#!/bin/bash

DIR=~/.local/share/gedit/plugins

mkdir -p $DIR
cd $DIR
wget https://raw.githubusercontent.com/meyersbs/gedit-text-stats/master/textstats.plugin
wget https://raw.githubusercontent.com/meyersbs/gedit-text-stats/master/textstats.py
echo "Thank you for installing my gedit plugin! If you have any questions, send me an email at ben@lionlogic.org"
