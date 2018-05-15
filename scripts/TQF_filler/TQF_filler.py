import sys
import time
import random
import pickle

import simplejson
import splinter

# Declare constants here
targetURL = 'https://tqf-phuket.psu.ac.th'

# Frequently used objects
Browser = splinter.Browser

def openNewSession():
    #browser = Browser('chrome',incognito=True,headless=True)
    browser = Browser('chrome')
    return browser

def closeSession(browser):
    browser.quit()

def mainSession(browser,inputFile):
    browser.visit(targetURL)
    # First, get credential
    inputFile.readline()
    credentialLocation = inputFile.readline()[:-1]
    with open(credentialLocation) as credentialFile:
        credentialFile.readline()
        username = credentialFile.readline()[:-1]
        credentialFile.readline()
        password = credentialFile.readline()[:-1]
    print(username, password)
    for line in inputFile:
        if line[0] != '#':
            print(line[:-1])
    browser.fill("ctl00$MainContent$Login1$UserName",username)
    browser.fill("ctl00$MainContent$Login1$Password",password)
    browser.find_by_id('MainContent_Login1_BtnSignin').first.click()
#
#
#        if not(isinstance(name,list)):
#            choice = interact(browser, index,name)
#        else:
#            lastChoice = int(selected[timeCounter][index][1:]) # Assume 0 offset here
#            choiceName = idList[index][lastChoice] #Assume 0 offset here?
#            choice = interact(browser, index,choiceName,lastChoice)
#        selected[timeCounter].append(choice)
#        print(index, name, choice)

if __name__ == "__main__":
    # Taking number of times input from command line
    # If not given, just one time.
    with open('input.txt','r') as inputFile:
        browser = openNewSession()
        mainSession(browser,inputFile)

    # Selected choices, first index of each element is the selection choice
