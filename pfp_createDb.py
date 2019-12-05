#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Filename: pfp_
    Description: Script gets list of symbols, calls Yahoo Finance API,
        and puts info to Brockmann & Company API for the back end of
        Beyond ETFs iOS app.   After doing this, it will create a
        log message to SLACK. This script will log if there is a
        discrepancy between the CSV and the database, but will not
        adjust the database.  Run Deyond_AddDel.py to do so.
    Author: Paul Brockmann
"""

import requests
import csv

