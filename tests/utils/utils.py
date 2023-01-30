from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Invoked with context.utils as set in environment.py
class UtilityFunctions(object):
    __TIMEOUT = 10
 
    def __init__(self, driver):
        super(UtilityFunctions, self).__init__()
        self._driver_wait = WebDriverWait(driver, UtilityFunctions.__TIMEOUT)
        self._driver = driver
 
    def open(self, url):
        self._driver.get(url)      
        
    def close(self):
        self._driver.quit()
        
    # Utility shortcuts for web locators (WebDriverWait ensures page loads before all checks)
 
    def select_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        
    def select_css(self, css):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
       
    def wait_until_clickable_xpath(self, xpath):
        return self._driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, xpath)))
        
    def wait_until_clickable_css(self, css):
        return self._driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css)))
    
    def hidden_xpath(self, xpath):
        return self._driver_wait.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        
    def hidden_css(self, css):
        return self._driver_wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, css)))
    
    # These methods test whether the specified element is visible or invisible (will induce a delay if False)
    def check_visible_xpath(self, xpath):
    	try:
    		self.select_xpath(xpath)
    	except NoSuchElementException:
    		return False
    	return True
    	
    def check_visible_css(self, css):
    	try:
    		self.select_css(css)
    	except NoSuchElementException:
    		return False
    	return True
    
    def check_invisible_xpath(self, xpath):
    	try:
    		self.hidden_xpath(xpath)
    	except NoSuchElementException:
    		return False
    	return True
    
    def check_invisible_css(self, css):
    	try:
    		self.hidden_css(css)
    	except NoSuchElementException:
    		return False
    	return True
    