# 🚗 Used Car Price Prediction & Analysis

An end-to-end data science project that scrapes **44,000+ used car listings** from [CarWale](https://www.carwale.com) across **11 Indian cities** and **24 car brands**, performs comprehensive data cleaning, and builds a **price prediction system** with a **Streamlit web application**.

---

## ✨ Features

- **📊 Data Analysis** — Explore trends, distributions, and insights across makes, models, cities, and fuel types
- **💰 Price Prediction** — ML models to predict used car prices based on specifications and condition
- **🔍 Recommendation System** — Suggest similar cars based on user preferences
- **⚖️ Car Comparison** — Side-by-side comparison of multiple cars
- **🌐 Streamlit App** — User-friendly web interface for all the above

---

## 🛠 Tech Stack

| Component            | Tools / Libraries                           |
| -------------------- | ------------------------------------------- |
| **Web Scraping**     | Python, Playwright, BeautifulSoup, Requests |
| **Data Processing**  | Pandas, NumPy                               |
| **Machine Learning** | scikit-learn (planned)                      |
| **Web App**          | Streamlit                                   |
| **Environment**      | Jupyter Notebooks, Python 3.12+             |

---

## 📈 Dataset

### Scope

| Dimension                  | Count        |
| -------------------------- | ------------ |
| **Total listings scraped** | ~44,000 URLs |
| **Final cleaned records**  | ~30,000      |
| **Features (raw)**         | 679 columns  |
| **Features (cleaned)**     | 638 columns  |
| **Cities**                 | 11           |

### Cities Covered

Ahmedabad · Bangalore · Chennai · Dehradun · Delhi · Gurgaon · Hyderabad · Kanpur · Lucknow · Mumbai · Pune

### Car Makes (24)

Maruti Suzuki · Hyundai · Tata · Mahindra · Toyota · Honda · Ford · Renault · Kia · BMW · Mercedes-Benz · MG · Volkswagen · Audi · Škoda · Land Rover · Volvo · Nissan · Jeep · Chevrolet · Jaguar · Fiat · Datsun · MINI

### Fuel Type Distribution

| Fuel Type   | Approx. Share |
| ----------- | ------------- |
| ⛽ Petrol   | ~60%          |
| ⛽ Diesel   | ~35%          |
| ⚡ Electric | ~1.6%         |
| 🔋 CNG      | ~2%           |
| 🌿 Hybrid   | ~1%           |

---

## 🔄 Pipeline

```
Web Scraping (Playwright + BS4)
        ↓
   44,000+ raw listings
        ↓
Data Cleaning (Pandas)
        ↓
   ~30,000 cleaned records
        ↓
Exploratory Data Analysis
        ↓
Feature Selection (per fuel type)
        ↓
ML Models (Price Prediction)
        ↓
Streamlit Web Application
```

### 1. Web Scraping

- **URL Collection** (`scrape-urls-new.py`) — Uses Playwright to scrape infinite-scroll listing pages for each city + make combination, collecting all car detail page URLs
- **Detail Scraping** (`scrape-car-details.py`) — Visits each car's detail page and extracts title, price, images, overview fields, and **650+ specification features**
- **Resumable** — Progress is saved per city (`*-progress.json`), so scraping can be safely interrupted and resumed

### 2. Data Cleaning

- **Cleaning v1** — Removes ~1,845 duplicate rows, analyzes null counts and fuel type distribution
- **Cleaning v2** — Drops constant columns (29 with only 1 unique value), merges duplicate overview columns, final shape: **29,946 rows × 638 columns**
- **Column Info** — `columns-info.json` documents null counts and unique value counts for every column

### 3. Modeling (WIP)

Models are trained **per fuel type** with carefully selected feature sets:

- **Petrol** — Engine, Mileage, Max Power, Torque, Transmission, ABS, Airbags, Sunroof, etc.
- **Diesel** — Engine, Turbocharger, Mileage, Torque, Hill Hold, etc.
- **Electric (EV)** — Battery, Driving Range, Charging Options, Regenerative Braking, etc.
- **CNG** — Engine, CNG Tank Capacity, Fuel Change Over Switch, etc.
- **Hybrid** — Engine, Battery, Electric Motor, Regenerative Braking, etc.

### 4. Web Application

A Streamlit app that provides:

- 📊 Interactive data visualizations and insights
- 💰 Used car price estimator
- 🔍 Smart car recommendation engine
- ⚖️ Car comparison tool

---

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- pip

### Installation

```bash
# Clone the repository
git clone
cd used-car-price-prediction

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

### Usage

```bash
# Run the Streamlit app
streamlit run app.py

# Or explore the data in Jupyter
jupyter notebook
```

---

## 📁 Project Structure

```
├── scraping-data/
│   ├── scrape-urls-new.py         # URL collection script
│   ├── scrape-car-details.py      # Car detail scraping script
│   ├── convert-jsonl-to-df.ipynb  # Consolidate raw data into CSV
│   ├── carwale-urls/              # Collected URLs per city
│   └── output/                    # Scraped data (JSON/JSONL)
│
├── data-cleaning/
│   ├── cleaning-1.ipynb           # Initial cleaning & dedup
│   ├── cleaning-2.ipynb           # Advanced cleaning
│   └── columns-info.json          # Column metadata
│
├── data/
│   ├── data_raw.csv               # Raw scraped data
│   ├── data_cleaned-v1.csv        # After initial cleaning
│   └── data_cleaned-v2.csv        # Final cleaned dataset
│
├── check_data.ipynb               # Data validation notebook
├── index.txt                      # Project notes & planning
└── README.md                      # You are here!
```

---

## 📝 License

This project is for educational and research purposes. Data was scraped from CarWale — please respect their terms of service.

---

## 👥 Team

Built as part of the **Data Science (300526)** course project.
