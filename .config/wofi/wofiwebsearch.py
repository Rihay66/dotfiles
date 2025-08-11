#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def run_menu():
    option = "\ue745  Firefox"
    search = os.popen("echo -e '\ue745  Firefox' | wofi -d -i -p 'Web Search' -W 700 -H 175 -k /dev/null").readline().strip()
    
    # check search string
    if search and search != option:
        # search through firefox
        os.popen("firefox --search " + "\"" + search + "\"")
    elif search and search == option:
        # open firefox normally
        os.popen("firefox")
        
run_menu()
