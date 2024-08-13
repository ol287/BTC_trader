from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class CoinbaseAutoLogin:
    def __init__(self, email, password, driver_path):
        self.email = email
        self.password = password
        self.driver_path = driver_path
        self.driver = None

    def start_browser(self):
        """
        Initializes the WebDriver and opens the Coinbase login page.
        """
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get("https://www.coinbase.com/signin")
        time.sleep(3)  # Wait for the page to load

    def login(self):
        """
        Logs into Coinbase using the provided credentials.
        """
        # Locate the email input field and enter the email
        email_input = self.driver.find_element_by_name("email")
        email_input.clear()
        email_input.send_keys(self.email)
        time.sleep(1)

        # Locate the password input field and enter the password
        password_input = self.driver.find_element_by_name("password")
        password_input.clear()
        password_input.send_keys(self.password)
        time.sleep(1)

        # Submit the form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login process to complete

    def close_browser(self):
        """
        Closes the browser window.
        """
        if self.driver:
            self.driver.quit()

    def automate_login(self):
        """
        Full automation process: start browser, login, and close browser.
        """
        self.start_browser()
        self.login()
        self.close_browser()

if __name__ == "__main__":
    # Replace with your Coinbase email and password
    email = "your_email@example.com"
    password = "your_password"
    
    # Path to your ChromeDriver
    driver_path = "/Applications/Google Chrome.app"

    # Initialize the automation class
    coinbase_bot = CoinbaseAutoLogin(email, password, driver_path)

    # Start the login process
    coinbase_bot.automate_login()
