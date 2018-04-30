from splinter import Browser

if __name__ == "__main__":
    with Browser() as browser:
        # Visit URL
        url = "http://login.psu.ac.th"
        browser.visit(url)
        if browser.is_text_present('This computer has been authenticated'):
            print("Perfect. You're on.")
