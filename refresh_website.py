from flask import Flask, jsonify

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/refresh_website', methods=['GET'])
def refresh_youtube():
    # Set the path to the web driver executable
    chromedriver_path = r'web_drivers\chromedriver.exe'
    service = Service(chromedriver_path)

    # Configure Chrome to run in headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # Needed for Windows systems

    # Create a WebDriver instance in headless mode
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open the URL of the web page you want to refresh
    url = 'https://www.youtube.com'
    driver.get(url)

    # Define the number of times to refresh the page
    refresh_count = 10

    for _ in range(refresh_count):
        # Refresh the page
        driver.refresh()

        # Wait for a certain amount of time before the next refresh
        time.sleep(5)  # You can adjust the time interval
        print('Refreshed page')
    # Close the WebDriver
    driver.quit()

    return jsonify({"message": "YouTube page refreshed successfully."})

if __name__ == '__main__':
    app.run(debug=True)
