import os, configparser
from os import path

currentPath = os.path.dirname(os.path.realpath(__file__))
propertiesFileName = currentPath + "/ghPR.properties"

def setupConfig():
    if path.exists(propertiesFileName):
        print("Properties file already exists, skipping setup")
        return

    config = configparser.ConfigParser()    

    githubUsername = input("Please enter your github username: ")

    closeLRQA = ''
    while closeLRQA not in ['y', 'n']:
        closeLRQA = input("Do you want to autoclose LRQA tickets submitted to BChan? y/n: ")

    config['default'] = {
        'githubUsername' : githubUsername,
        'closeLRQA' : closeLRQA }

    with open(propertiesFileName, 'w') as configfile:
        config.write(configfile)

def readConfig():
    config = configparser.ConfigParser()
    return config.read(propertiesFileName)