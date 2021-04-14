#WHATSAPP BIRTHDAY BOT 
#MESSAGE SENDER
#COPYRIGHT © ADG STUDIOS 2021

import configparser
import os
import pywhatkit
import numpy as np,pandas as pd
import datetime
from datetime import date
from emoji import emojize
print("ADG WHATSAPP BIRTHDAY BOT")

def getTokenAPI(dirpath): 
 config = configparser.ConfigParser()		
 config.read(dirpath)
 api = config['WhatsApp Birthday Bot']
 return api["tokenapi"]

def sendMessage(database,token): 
 df = pd.read_csv(database)
 df1 = df[['Name of Person (Birthday)','Date of Birthday']]
 df1.head()
 datetoday = date.today().strftime('%#m/%#d')
 for index,row in df.iterrows():
  personbdaydate = row['Date of Birthday'].rsplit('/' , 1)
  if personbdaydate[0] == datetoday: 
   nameofperson = row['Name of Person (Birthday)'].replace('birthday', '')
   message = 'Happy birthday'+' '+emojize(':birthday_cake:')+' '+nameofperson+' '+emojize(":partying_face: :party_popper: :party_popper:")
   print(message)
   now = datetime.datetime.now()    
   pywhatkit.sendwhatmsg_to_group(token,'Happy birthday :birthday_cake: to '+nameofperson+' :partying_face: :party_popper: :party_popper:',now.hour,now.minute+1)

def getDatabase(dirpath):
 config = configparser.ConfigParser()		
 config.read(dirpath)
 api = config['WhatsApp Birthday Bot']
 return api["database"]

directory = os.path.dirname(os.path.realpath(__file__))+"\WhatsApp Birthday Bot.ini"
if os.path.exists(directory):
 api = getTokenAPI(directory)
 database = getDatabase(directory)
 if os.path.exists(database):
  print("Using token API:",api)
  print("getting ready to send birthday message ...")
  sendMessage(database,api)      
 else:
  print("database not found, please change path in dashboard")    
else:
 print("config file not found")
 exit(1)



