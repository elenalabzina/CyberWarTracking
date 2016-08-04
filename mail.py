#!/usr/bin/python

import smtplib
import base64
import glob,os

def mail():
   sender = 'len4ick@gmail.com'
   receivers = ['len4ick@gmail.com']

   message = """From: My Ubuntu server <Python the Great>
   To: To Person <len4ick@gmail.com>
   Subject: The extraction for IPS done for today: Hooray!


   """

   try:
      smtpObj = smtplib.SMTP('localhost')
      smtpObj.sendmail(sender, receivers, message)         
      print "Successfully sent email"
   except:
      print "Error: unable to send email"