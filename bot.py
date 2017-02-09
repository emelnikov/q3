#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Dec 14, 2016

@author: Eugene Melnikov
'''
from telepot import Bot
from Tools import Check
from Tools import Confreader
from threading import Thread
from time import sleep
from pprint import pprint

class BotRun(Thread):
    def __init__(self):
        self.config = Confreader.Confreader()
        self.checker = Check.ServerChecker()
        self.token = self.config.get_val('General', 'token')
        self.chat_id = self.config.get_val('General', 'chat_id')
        self.sleep_val = self.config.get_val('General', 'sleep')
        self.addressport = self.config.get_address_port()
        self.bot = Bot(self.token)
        self.messages_enabled = True
        
        Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        self.bot.message_loop(self.handle)
        count = players_prev = 0
        while True:
            if self.messages_enabled:
                getPlayers = int(self.checker.getPlayers(self.addressport['address'], int(self.addressport['port'])))
                #print getPlayers
                if getPlayers > 0 and count == 0:
                    self.bot.sendMessage(self.chat_id, u"Players on the server:" + " " + str(getPlayers))
                    players_prev = getPlayers
                    count += 1
                elif getPlayers > 0 and count > 0 and getPlayers != players_prev:
                    self.bot.sendMessage(self.chat_id, u"Players on the server:" + " " + str(getPlayers))
                    players_prev = getPlayers
                elif players_prev > 0 and getPlayers == 0:
                    self.bot.sendMessage(self.chat_id, u"All players quit")
                    players_prev = 0
            sleep(float(self.sleep_val))
            
    def handle(self,msg):
        #pprint(msg)
        message_body = msg['text'].lower()
        if message_body[0] =="/": #then it's command!
            if message_body[0:5] == "/stop":
                self.messages_enabled = False
                print "messages were disabled"

BotRun()

while True:
   sleep(10)