from playwright.sync_api import sync_playwright
import json

def load_data():
    all_urls_set = set()
    FILE_NAME = "urls_carwale_lucknow.json"

    makes = [
        "maruti-suzuki", "hyundai", "tata", "mahindra", "toyota", "honda",
        "ford", "renault", "kia", "bmw", "mercedes-benz", "mg",
        "volkswagen", "audi", "skoda", "land-rover", "volvo", "nissan",
        "jeep", "chevrolet", "jaguar", "fiat", "datsun", "mini"
    ]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for make in makes:
            url = f"https://www.carwale.com/used/lucknow/{make}/"
            print(f"\n{make}...", end=" ", flush=True)
            page.goto(url, wait_until="networkidle")
            page.wait_for_timeout(2000)

            prev_count = 0
            for i in range(40):
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(1500)

                cars = page.query_selector_all("a.o-C")
                for car in cars:
                    link = car.get_attribute("href")
                    if link:
                        all_urls_set.add(link)

                if len(all_urls_set) == prev_count and i > 3:
                    break
                prev_count = len(all_urls_set)

            print(f"{len(all_urls_set)}")

        browser.close()

    with open(FILE_NAME, "w") as f:
        json.dump(sorted(all_urls_set), f, indent=2)

    print(f"\n{len(all_urls_set)} Unique URLs Saved in {FILE_NAME}")

load_data()
