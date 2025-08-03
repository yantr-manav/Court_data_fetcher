import time
import pytesseract
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# If tesseract is not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def solve_captcha(driver):
    captcha_img = driver.find_element(By.XPATH, '//*[@id="captcha_image"]')
    captcha_screenshot = captcha_img.screenshot_as_png
    image = Image.open(BytesIO(captcha_screenshot))
    captcha_text = pytesseract.image_to_string(image).strip()
    captcha_text = ''.join(filter(str.isalnum, captcha_text))  # Remove noise
    return captcha_text

def fetch_case_details(case_type="W.P.(C)", case_number="5562", filing_year="2023"):
    url = "https://delhihighcourt.nic.in/app/get-case-type-status"
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # Open portal
        driver.get(url)

        # Click on "Case Type" tab
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Case Type")]'))).click()

        # Select "Court Complex"
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Court Complex"]'))).click()

        # Fill Court Complex
        court_complex_dropdown = wait.until(EC.presence_of_element_located((By.ID, 'court_complex_code')))
        court_complex_dropdown.send_keys("HIGH COURT, DELHI")

        # Case Type
        driver.find_element(By.ID, 'case_type').send_keys(case_type)

        # Year
        driver.find_element(By.ID, 'case_year').send_keys(filing_year)

        # Case Status: Pending
        driver.find_element(By.ID, 'rad_statusP').click()

        # Solve CAPTCHA
        captcha_text = solve_captcha(driver)
        driver.find_element(By.ID, 'captcha').send_keys(captcha_text)

        # Submit
        driver.find_element(By.XPATH, '//input[@value="Search"]').click()

        # Wait for result
        wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="View"]')))

        # Click “View”
        driver.find_element(By.XPATH, '//input[@value="View"]').click()

        # Wait for case detail page
        wait.until(EC.presence_of_element_located((By.XPATH, '//td[contains(text(), "Case Type")]')))

        # Parse full case details
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        data = {
            "case_type": soup.find(text="Case Type").find_next('td').text.strip(),
            "filing_date": soup.find(text="Filing Date").find_next('td').text.strip(),
            "first_hearing": soup.find(text="First Hearing Date").find_next('td').text.strip(),
            "next_hearing": soup.find(text="Next Hearing Date").find_next('td').text.strip(),
            "case_stage": soup.find(text="Case Stage").find_next('td').text.strip(),
            "court_judge": soup.find(text="Court Number and Judge").find_next('td').text.strip(),
            "cnr_number": soup.find(text="CNR Number").find_next('td').text.strip()
        }

        return data, None, None

    except Exception as e:
        return None, str(e), "Failed to fetch details. Verify input or portal structure."

    finally:
        driver.quit()
