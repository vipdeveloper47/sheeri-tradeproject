
Django Deployment Guide for Sheeri
----------------------------------

"""
      Acha baat suunn, deploy krne se pehle mujhe se puch wageera bh lei, aur yahan wala
      message parhne ke baad, mujhe whatsapp message krin... see you there buddy!
"""

This guide will help you set up and run the Trader system online.

1. Install Requirements:
   - Python 3.x
   - MySQL (already installed)
   - Django

2. Setup Database:
   - Open MySQL Workbench
   - Run the 'trader_db.sql' file (double-click on it and execute all)

3. Setup Environment:
   - Create a file named '.env' with the following:

     DB_NAME=trader_db
     DB_USER=trader_user
     DB_PASSWORD=mysql@123 # tuu yahan par apna secure password bh laga sakta he, right?
     DB_HOST=127.0.0.1
     DB_PORT=3306
     SECRET_KEY=any_random_secret_key
     DEBUG=False

4. Start the Project:
   - Open VS Code terminal
   - Run:

     pip install -r requirements.txt
     python manage.py makemigrations
     python manage.py migrate
     python manage.py runserver

5. Access Website:
   - Open browser and go to: http://127.0.0.1:8000/

Date: 2025-06-17
Prepared by: Faizan
