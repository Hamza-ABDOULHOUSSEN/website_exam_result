#!/bin/bash
source env/bin/activate
export FLASK_APP=site_web/app.py
flask run
