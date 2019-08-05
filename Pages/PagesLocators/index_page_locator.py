
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class IndexPageLocator():
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((MobileBy.ID, "com.lemon.lemonban:id/navigation_my")
                                         ))
    driver.find_element_by_id("com.lemon.lemonban:id/navigation_my").click()