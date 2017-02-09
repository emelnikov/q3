#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Dec 14, 2016

@author: Eugene Melnikov
'''
import socket

class ServerChecker (object):
    
    def getStatus(self, host, port):
        sock = socket.socket(socket.AF_INET,  # Internet
        socket.SOCK_DGRAM) # SOCK_DGRAM for UDP connection, SOCK_STREAM for TCP
        sock.connect((host, port)) # Connectiong to q3 UDP server 
        sock.sendto('\xff\xff\xff\xffgetinfo',(host, port)) # Server i whoud like to inspect
        data, addr = sock.recvfrom(7000) # Waiting for Replay.
        return str(data).split("\\")
    
    def getPlayers(self, host, port):
        status = self.getStatus(host, port)
        players_section = 'g_humanplayers'
        try:
            players_index = status.index(players_section)
        except ValueError as e:
            print str(e) + ": server does not support g_humanvalue"
        except Exception as e:
            print str(e)
        return status[players_index+1]