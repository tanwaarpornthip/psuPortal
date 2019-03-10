from splinter import Browser
import datetime

# User variables. Change these
# Username and password. Clear text for now
username = "YOUR USERNAME HERE"
password = "YOUR PASSWORD HERE"
logLocation = '/home/USER/log.csv'
executable_path={'executable_path':'/usr/local/bin/chromedriver'}
#     End of user-defined variables                            #
################################################################

def logMeIn(browser):
    browser.fill('username',username)
    browser.fill('password',password)
    browser.find_by_name('login')[1].click()
    

if __name__ == "__main__":
    now = datetime.datetime.now()
    nowString = now.strftime('%c'); # Using Epoch time
    
    with Browser('chrome', headless=True, incognito=True, **executable_path) as browser:
        # Visit URL
        url = "http://login.psu.ac.th"
        resultString = nowString
        browser.visit(url)
        with open(logLocation,'a+') as logFile:
            if browser.is_text_present('been authenticated'):
                logFile.write(resultString+',True\n')
            else:
                logFile.write(resultString+',False\n')
                logMeIn(browser)
print("Connectivity status checked successfully at %s" %(now))
            
