import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Load the JSON data
# mention your correct file path 
with open("..//InputParam.json", "r") as f:
    scenarios = json.load(f)
# Initialize the driver outside the scenario loop
driver = webdriver.Chrome()  # Replace with your desired browser driver path



# Function to run a scenario
def run_scenario(scenario,driver):
   # driver = webdriver.Chrome()  # Replace with your desired browser driver path

    for step in scenario['steps']:
        action = step['action']
        locator_type = step.get('locator', None)
        locator_value = step.get('value', None)
        url_value =step.get('url',None)

        if action == "open_url":
            driver.get(url_value)
        elif action == "find_element":
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((getattr(By, locator_type.upper()), locator_value)))                
        elif action == "send_keys":
            element.send_keys(locator_value)
        elif action == "click_element":
            element.click()
        else:
            print(f"Unsupported action: {action}")
        
       # time.sleep(30)

    #driver.quit()

# Run each scenario
# for scenario in scenarios:
#   print(f"Running scenario: {scenario['scenario_name']}")
#   run_scenario(scenario)
    
try:
    # Run each scenario using the same driver instance
    for scenario in scenarios:
        print(f"Running scenario: {scenario['scenario_name']}")
        run_scenario(scenario, driver)  # Pass the driver to the function
        time.sleep(15)

finally:
    # Quit the driver only once, after all scenarios
    driver.quit()
