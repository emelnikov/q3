'''
Created on Feb 4, 2017

@author: Eugene Melnikov
'''
from ConfigParser import RawConfigParser

class Confreader(object):
    '''
    Class provides simplified functions to access config values.
    '''
    def __init__(self):
        self.config = RawConfigParser()
        self.filename = 'config/bot.conf'
    
    def get_config(self):
        '''
        Provides config reader object.
        
        Accepts: nothing
        Returns: config reader object (RawConfigParser instance)
        '''
        
        readerObj = self.config
        readerObj.read(self.filename)
        return readerObj
        
    def get_address_port(self):
        address = self.get_config().get('Connection', 'address')
        port = self.get_config().get('Connection', 'port')
        result = {'address': address, 'port': port}
        return result
    
    def get_val(self, section, value):
        result = self.get_config().get(section, value)
        return result