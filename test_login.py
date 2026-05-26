from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_setup import get_driver
from config import BASE_URL, INVESTOR
import time

def test_login():
    driver = get_driver()
    wait = WebDriverWait(driver, 15)
    
    try:
        # Step 1: Login page kholo
        driver.get(f"{BASE_URL}/login")
        print("Login page khula")
        time.sleep(2)
        
        # Step 2: Email fill karo — id="email"
        email_field = wait.until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.clear()
        email_field.send_keys(INVESTOR["email"])
        print("✅ Email fill ki")
        
        # Step 3: Password fill karo — type="password"
        password_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
        )
        password_field.clear()
        password_field.send_keys(INVESTOR["password"])
        print("✅ Password fill ki")
        
        # Step 4: Sign In button click karo
        sign_in_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Sign In')]")
            )
        )
        sign_in_btn.click()
        print("✅ Sign In button click kiya")
        
        # Step 5: Dashboard verify karo
        wait.until(EC.url_contains("dashboard"))
        print("✅ Login successful!")
        print(f"Current URL: {driver.current_url}")
        
        time.sleep(2)
        driver.save_screenshot("login_success.png")
        print("📸 Screenshot: login_success.png")
        
        return driver
        
    except Exception as e:
        print(f"❌ Error: {e}")
        driver.save_screenshot("login_error.png")
        raise
        
    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_login()