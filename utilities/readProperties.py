import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+"\\configurations\\config.ini")

class ReadConfig: #we can static method directly by class
    @staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'base_url')
        return url

    @staticmethod
    def getUseremail():
        email=config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password
