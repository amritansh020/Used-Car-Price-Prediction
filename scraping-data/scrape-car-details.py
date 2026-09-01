from playwright.sync_api import sync_playwright, Page
import json
import os


def load_data(url):
    with open(url, "r") as f:
        data = json.load(f)
        return data


def fetch_data(page: Page):
    data = {}
    page.wait_for_selector("h1.o-j7", timeout=5000)
    try:
        title = page.query_selector("h1.o-j7").text_content()
    except:
        title = ""
    data["title"] = title
    try:
        new_car_price_div = page.query_selector("div.o-j0")
        new_car_price = new_car_price_div.query_selector("div").text_content()
    except:
        new_car_price = ""
    data["new_car_price"] = new_car_price
    try:
        car_image_url = page.query_selector("img.B6hlWy").get_attribute("src")
    except:
        car_image_url = ""
    data["car_img_url"] = car_image_url
    car_overview = page.query_selector_all("div.o-hT")[1:-1]
    for overview in car_overview:
        try:
            label = overview.query_selector(".o-jK").text_content()
            value = overview.query_selector("div.o-f5").text_content()
            # print(label, value)
            data[label] = value
        except Exception as e:
            print(e)
            continue

    # For fetching specifications of car
    spec_container = page.query_selector_all("div.kgwwPb>div>ul>li")
    # print(spec_container)
    for spec in spec_container:
        try:
            label = spec.query_selector(".o-jK").text_content()
            value = spec.query_selector(".o-jJ").text_content()
            # print(label,value)
            data[label] = value
        except:
            continue

    return data


# Function that takes a data and file path and save that data to that file_path
def save_data(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file)


def load_progress(path):
    is_exist = os.path.exists(path)
    if not is_exist:
        return set()
    with open(path, "r") as file:
        data = json.load(file)
        return set(data)


CITY = "lucknow"
BASE_PATH = "./carwale-urls/"
FILE_NAME = f"urls_{CITY}.json"
OUTPUT_PATH = f"./output/{CITY}-data.json"
PROGRESS_PATH = f"./output/{CITY}-progress.json"
URL_PATH = BASE_PATH + FILE_NAME  # "./carwale-urls/urls_lucknow.json"
data = load_data(URL_PATH)
WEB_BASE_URL = "https://www.carwale.com"
all_car_details = []
done_cars_urls = load_progress(PROGRESS_PATH)
done_cars = len(done_cars_urls)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    for car_url in data:
        if car_url in done_cars_urls:
            continue
        final_car_url = WEB_BASE_URL + car_url
        page.goto(final_car_url)
        try:
            car_data = fetch_data(page)
            all_car_details.append(car_data)  # Append car details to an array
            done_cars_urls.add(car_url)  # Save completed url to a set
            done_cars += 1
            print(f"{done_cars} Done...")
            if done_cars % 20 == 0:
                print("=" * 50)
                save_data(all_car_details, OUTPUT_PATH)  # Saving data to a file
                save_data(
                    list(done_cars_urls), PROGRESS_PATH
                )  # Saving progress to a file
                print("Data Saved!!")
                print("=" * 50)
        except Exception as e:
            done_cars_urls.add(car_url)
            print(e)
            continue

# 10K DataFrame
# Ahemdabad
# Banglore
# Chennai
# Dehradun
# Delhi
# Gurgoan
# Hyderabad
# Kanpur
# Lucknow
#  Mumbai
# Pune
