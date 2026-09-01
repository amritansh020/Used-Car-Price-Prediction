from playwright.sync_api import sync_playwright
import json

def load_data():
    WEB_LINK = "https://www.carwale.com/used/lucknow/"
    TOTAL_PAGES = 88
    all_urls = []
    FILE_NAME = "urls_carwale_lucknow.json"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for curr_page in range(1, TOTAL_PAGES + 1):
            page.goto(f"{WEB_LINK}page-{curr_page}/")
            page.wait_for_selector("a.o-C")
            all_cars = page.query_selector_all("a.o-C")
            for car in all_cars:
                url = car.get_attribute("href")
                all_urls.append(url)
            if curr_page % 10 == 0:
                with open(FILE_NAME, "w") as f:
                    json.dump(all_urls, f)
                    print("Urls Saved")
            print(f"{curr_page} Done")
    with open(FILE_NAME, "w") as f:
        json.dump(all_urls, f)
        print(f"{len(all_urls)} Urls Loaded and Saved in File {FILE_NAME}")


load_data()
# cardekho
# 50 88

# Kanpur
# Delhi
# Mumbai
# Banglore
# Chennai
# Dehradun
# Hyderabad
# Kolkata
# Ahemdabad
# Pune
