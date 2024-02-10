# Edge Keyword Search Script

This script automates keyword searches in the Microsoft Edge browser using Selenium.

## Overview

The Edge Keyword Search Script is a Python script that utilizes the Selenium library to automate keyword searches in the Microsoft Edge browser. It takes a list of keywords and performs searches for each keyword in the browser window.

## Features

- Searches for a list of keywords in the Microsoft Edge browser.
- Randomly selects keywords from a predefined list for each search.
- Allows for easy customization of search parameters.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Microsoft Edge browser
- Selenium library (install using `pip install selenium`)
- Microsoft Edge WebDriver executable (download from [here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/))

## Usage

1. Clone this repository:
   ```git clone https://github.com/Abhishekbagdiya01/edge-keyword-search-automation-bot.git```

2. Install all dependencies
3. Place the `msedgedriver.exe` executable in the root directory of the project.

4. Customize the `keywords` list in the `app.py` file with your desired keywords.

5. Run the script: ``` py app.py ```

   ## Acknowledgments

- This project was inspired by the need to automate keyword searches in the Microsoft Edge browser.
- Special thanks to the Selenium community for providing a powerful tool for browser automation.



