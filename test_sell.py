from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from driver_setup import get_driver
from config import BASE_URL, INVESTOR
import time

def login(driver, wait):
    driver.get(f"{BASE_URL}/login")
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(INVESTOR["email"])
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))).send_keys(INVESTOR["password"])
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
    wait.until(EC.url_contains("dashboard"))
    print("✅ Login ho gaya")

def test_sell_stock():
    driver = get_driver()
    wait = WebDriverWait(driver, 15)

    try:
        # Step 1: Login
        login(driver, wait)
        time.sleep(2)

        # Step 2: Portfolios page
        driver.get(f"{BASE_URL}/portfolios")
        print("✅ Portfolios page khula")
        time.sleep(2)

        # Step 3: View Details click karo
        view_details_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'View Details')]")
            )
        )
        view_details_btn.click()
        print(f"✅ View Details click kiya")
        time.sleep(2)

        # Step 4: Sell button click karo
        sell_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'btn-outline') and contains(text(), 'Sell')]")
            )
        )
        sell_button.click()
        print("✅ Sell button click kiya")
        time.sleep(2)

        # Step 5: Quantity fill karo — visibility wait
        quantity_field = wait.until(
            EC.visibility_of_element_located((By.ID, "sellQuantity"))
        )
        quantity_field.clear()
        quantity_field.send_keys("1")
        print("✅ Quantity fill ki: 1")
        time.sleep(1)

        # Step 6: Price fill karo
        price_field = wait.until(
            EC.visibility_of_element_located((By.ID, "sellPrice"))
        )
        price_field.clear()
        price_field.send_keys("460")
        print("✅ Price fill ki: 460")
        time.sleep(1)

        # Step 7: Date already filled hai — skip
        print("✅ Date already set hai")

        # Step 8: Screenshot — form filled
        driver.save_screenshot("sell_filled.png")
        print("📸 Form filled screenshot: sell_filled.png")

        # Step 9: Sell Stock button click karo
        sell_stock_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Sell Stock')]")
            )
        )
        sell_stock_btn.click()
        print("✅ Sell Stock button click kiya")
        time.sleep(3)

        # Step 10: Success verify karo
        driver.save_screenshot("sell_success.png")
        print("📸 Screenshot: sell_success.png")
        print("\n✅ WIPRO Stock sell automation complete!")

    except Exception as e:
        print(f"❌ Error: {e}")
        driver.save_screenshot("sell_error.png")
        raise

    finally:
        time.sleep(3)
        driver.quit()

if __name__ == "__main__":
    test_sell_stock()