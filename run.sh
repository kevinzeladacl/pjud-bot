#!/bin/bash
clear
cat << "EOF"
==========================================================================================


  _____          _                  _           _ _      _       _   ____   ____ _______  __      __  __   ___  
 |  __ \        | |                | |         | (_)    (_)     | | |  _ \ / __ \__   __| \ \    / / /_ | / _ \ 
 | |__) |__   __| | ___ _ __       | |_   _  __| |_  ___ _  __ _| | | |_) | |  | | | |     \ \  / /   | || | | |
 |  ___/ _ \ / _` |/ _ \ '__|  _   | | | | |/ _` | |/ __| |/ _` | | |  _ <| |  | | | |      \ \/ /    | || | | |
 | |  | (_) | (_| |  __/ |    | |__| | |_| | (_| | | (__| | (_| | | | |_) | |__| | | |       \  /     | || |_| |
 |_|   \___/ \__,_|\___|_|     \____/ \__,_|\__,_|_|\___|_|\__,_|_| |____/ \____/  |_|        \/      |_(_)___/ 
                                                                                                                
                                                                                             by  @kevinzeladacl
                                                                         
==========================================================================================

SELECT A OPTION (enter number):

============LOCAL/DEV OPTIONS ==========

999 - INSTALL PROJECT LOCAL

0 - RUN WITH DEBUG CONSOLE (DEV)



EOF

read option
case $option in
  999) 
     echo "Installing now ..."
     pip install -r requirements/staging.txt
     
  ;;
  0) 
     echo "RUN WITH DEBUG CONSOLE (DEV)..."
     python bot.py
  ;;
 
  *)
     echo "Select a valid option 77"
  ;;

esac  