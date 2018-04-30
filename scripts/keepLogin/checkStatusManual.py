from splinter import Browser
import datetime
import time

if __name__ == "__main__":
    while True: 
        now = datetime.datetime.now()
        nowString = now.strftime('%s'); # Using Epoch time
        with Browser('firefox', headless=True) as browser:
            # Visit URL
            url = "http://login.psu.ac.th"
            resultString = nowString
            browser.visit(url)
            with open('/home/tanwa/psuPortal/scripts/keepLogin/logManual.csv','a+') as logFile:
                if browser.is_text_present('This computer has been authenticated'):
                    statusString = ',True\n'
                else:
                    statusString = ',False\n'
                logFile.write(resultString+statusString)
        print(resultString+statusString)
        time.sleep(60)
            
