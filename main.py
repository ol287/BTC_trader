from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

class CoinbaseAutoLogin:
    def __init__(self, email, password, driver_path):
        self.email = email  # Store the user's email
        self.password = password  # Store the user's password
        self.driver_path = driver_path  # Store the path to the ChromeDriver executable
        self.driver = None  # Initialize the driver attribute

    def start_browser(self):
        """
        Initializes the WebDriver and opens the Coinbase login page.
        """
        # Create a Service object with the path to the ChromeDriver executable
        service = Service(self.driver_path)
        # Initialize the WebDriver with the Service object
        self.driver = webdriver.Chrome(service=service)
        # Open the Coinbase login page
        self.driver.get("https://www.coinbase.com/signin")
        time.sleep(3)  # Wait for the page to load

    def login(self):
        """
        Logs into Coinbase using the provided credentials.
        """
        # Locate the email input field and enter the email
        email_input = self.driver.find_element_by_name("email")
        email_input.clear()  # Clear any pre-filled data in the email field
        email_input.send_keys(self.email)  # Enter the email
        time.sleep(1)  # Wait for a second

        # Locate the password input field and enter the password
        password_input = self.driver.find_element_by_name("password")
        password_input.clear()  # Clear any pre-filled data in the password field
        password_input.send_keys(self.password)  # Enter the password
        time.sleep(1)  # Wait for a second

        # Submit the form by pressing Enter
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for the login process to complete

    def close_browser(self):
        """
        Closes the browser window.
        """
        if self.driver:
            self.driver.quit()  # Close the browser

    def automate_login(self):
        """
        Full automation process: start browser, login, and close browser.
        """
        self.start_browser()  # Open the browser and go to the login page
        self.login()  # Perform the login
        self.close_browser()  # Close the browser after login

if __name__ == "__main__":
    # Replace with your Coinbase email and password
    email = "your_email@example.com"
    password = "your_password"
    
    # Path to your ChromeDriver executable
    driver_path = "/Applications/Google Chrome.app"

    # Initialize the automation class
    coinbase_bot = CoinbaseAutoLogin(email, password, driver_path)

    # Start the login process
    coinbase_bot.automate_login()
