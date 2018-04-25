from splinter import Browser

if __name__ == "__main__":
    with Browser() as browser:
        # Visit URL
        url = "login.psu.ac.th"
        browser.visit(url)
        button.click()
        if browser.is_text_present('splinter.readthedocs.io'):
            print("Yes, the official website was found!")
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")
