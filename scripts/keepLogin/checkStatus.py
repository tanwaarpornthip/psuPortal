from splinter import Browser
import datetime
executable_path={'executable_path':'/usr/local/bin/chromedriver'}

if __name__ == "__main__":
    now = datetime.datetime.now()
    nowString = now.strftime('%s'); # Using Epoch time
    
    with Browser('chrome', headless=True, incognito=True, **executable_path) as browser:
        # Visit URL
        url = "http://login.psu.ac.th"
        resultString = nowString
        browser.visit(url)
        with open('/home/tanwa/psuPortal/scripts/keepLogin/log.csv','a+') as logFile:
            if browser.is_text_present('This computer has been authenticated'):
                logFile.write(resultString+',True\n')
            else:
                logFile.write(resultString+',False\n')
print("Connectivity status checked successfully at %s" %(now))
            
