from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# ------------------------- CONFIGURATION -------------------------
FORM_CONFIG = {
    "url": "GOOGLE_FORM_LINK_HERE",  # Replace with your Google Form link
    "fields": {
        "address": "value-goes-here",  # Replace with actual XPath (must enclose XPath in single qoutes '')
        "price": "value-goes-here",  # Replace with actual XPath
        "link": "value-goes-here",  # Replace with actual XPath
        "submit": "value-goes-here",  # Replace with actual XPath
    },
}

ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}


# ------------------------- SCRAPING -------------------------
def scrape_properties():
    # Use our Zillow-Clone website (instead of Zillow.com)
    response = requests.get(ZILLOW_CLONE_URL, headers=header)
    response.raise_for_status()  # fail fast if page doesn’t load
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract links
    all_links = [
        link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")
    ]

    # Extract addresses
    all_addresses = [
        address.get_text().replace(" | ", " ").strip()
        for address in soup.select(".StyledPropertyCardDataWrapper address")
    ]

    # Extract prices
    all_prices = [
        price.get_text().replace("/mo", "").split("+")[0]
        for price in soup.select(".PropertyCardWrapper span")
        if "$" in price.text
    ]

    # Ensure data consistency
    min_length = min(len(all_links), len(all_addresses), len(all_prices))
    return (
        all_addresses[:min_length],
        all_prices[:min_length],
        all_links[:min_length],
    )


# ------------------------- FORM FILLING -------------------------
def fill_form(addresses, prices, links):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)

    for address, price, link in zip(addresses, prices, links):
        try:
            driver.get(FORM_CONFIG["url"])
            time.sleep(2)

            # Use the xpath to select the "short answer" fields in your Google Form.
            driver.find_element(By.XPATH, FORM_CONFIG["fields"]["address"]).send_keys(
                address
            )
            driver.find_element(By.XPATH, FORM_CONFIG["fields"]["price"]).send_keys(
                price
            )
            driver.find_element(By.XPATH, FORM_CONFIG["fields"]["link"]).send_keys(link)
            driver.find_element(By.XPATH, FORM_CONFIG["fields"]["submit"]).click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"⚠️ Skipping entry due to error: {e}")
            continue

    driver.quit()


# ------------------------- MAIN -------------------------
if __name__ == "__main__":
    addresses, prices, links = scrape_properties()
    fill_form(addresses, prices, links)
    print("✅ Form filling complete.")
