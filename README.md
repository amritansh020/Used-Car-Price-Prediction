# 🚗 Used Car Price Prediction & Analysis

A practical **data analysis and machine learning project** focused on
understanding the Indian used-car market and predicting used-car prices
from vehicle specifications.

**Project by Amritansh**

> This repository is maintained as a personal learning and portfolio
> project. The codebase covers web scraping, data cleaning, exploratory
> analysis, feature selection, and machine-learning-based price
> prediction.

------------------------------------------------------------------------

## 📌 Project Overview

The project works with used-car listings collected from **CarWale**
across multiple Indian cities and car brands.

The overall workflow is:

``` text
Web Scraping
     ↓
Raw Used-Car Data
     ↓
Data Cleaning & Validation
     ↓
Exploratory Data Analysis
     ↓
Feature Selection
     ↓
Machine Learning
     ↓
Used-Car Price Prediction
```

The project is designed to demonstrate practical skills in:

-   Data collection
-   Data cleaning
-   Exploratory Data Analysis (EDA)
-   Feature engineering and selection
-   Regression modelling
-   Python and Jupyter Notebook workflows
-   Working with large tabular datasets

------------------------------------------------------------------------

## 🎯 Objectives

1.  Collect used-car listing data from multiple Indian cities.
2.  Clean and prepare the raw dataset for analysis.
3.  Identify useful vehicle and market features.
4.  Explore relationships between car specifications and price.
5.  Train regression models for price prediction.
6.  Evaluate model performance using standard regression metrics.
7.  Build a foundation for a future interactive prediction application.

------------------------------------------------------------------------

## 📊 Dataset

The project contains data collected from approximately **44,000+
used-car listings/URLs**, followed by several stages of cleaning.

### Coverage

-   **Cities:** Ahmedabad, Bangalore, Chennai, Dehradun, Delhi, Gurgaon,
    Hyderabad, Kanpur, Lucknow, Mumbai, Pune
-   **Brands:** Maruti Suzuki, Hyundai, Tata, Mahindra, Toyota, Honda,
    Ford, Renault, Kia, BMW, Mercedes-Benz, MG, Volkswagen, Audi, Škoda,
    Land Rover, Volvo, Nissan, Jeep, Chevrolet, Jaguar, Fiat, Datsun and
    MINI
-   **Raw features:** hundreds of vehicle and listing attributes
-   **Final cleaned dataset:** approximately 30,000 records after
    cleaning

### Important vehicle information

Examples of features used or investigated include:

-   Brand
-   Model
-   Variant
-   Price
-   Manufacturing Year
-   Registration Year
-   Car Age
-   Kilometres Driven
-   Ownership
-   Fuel Type
-   Transmission
-   City
-   Engine
-   Mileage
-   Max Power
-   Torque
-   Airbags
-   ABS
-   ESP
-   Cruise Control
-   Parking Sensors
-   Sunroof
-   Wheelbase
-   Ground Clearance
-   Boot Space

------------------------------------------------------------------------

## 🕷️ Web Scraping

The scraping pipeline uses:

-   **Python**
-   **Playwright**
-   **BeautifulSoup**
-   **Requests**

### Main scraping files

``` text
scraping-data/
├── scrape-urls-new.py
├── scrape-car-details.py
├── scrape-urls-old.py
├── convert-jsonl-to-df.ipynb
├── carwale-urls/
└── output/
```

The URL collection scripts gather vehicle listing URLs, while the detail
scraper extracts information from individual vehicle pages.

Progress files are stored by city so that long scraping jobs can be
resumed.

------------------------------------------------------------------------

## 🧹 Data Cleaning

Several Jupyter notebooks are used to progressively clean and validate
the dataset.

``` text
data-cleaning/
├── cleaning-1.ipynb
├── cleaning-2.ipynb
├── cleaning-3.ipynb
├── cleaning-4.ipynb
├── cleaning-5.ipynb
├── cleaning-6.ipynb
├── cleaning-7.ipynb
├── all_col_name.json
└── columns-info.json
```

The cleaning workflow includes:

-   Duplicate detection and removal
-   Missing-value analysis
-   Column inspection
-   Removing low-information/constant columns
-   Combining or cleaning duplicate information
-   Checking categorical values
-   Preparing the dataset for modelling

------------------------------------------------------------------------

## 📈 Exploratory Data Analysis

The analysis explores how used-car prices vary with factors such as:

-   Brand
-   City
-   Fuel type
-   Engine specifications
-   Mileage
-   Power
-   Vehicle age
-   Other vehicle features

Correlation analysis and visualizations are used to identify potentially
important predictors of price.

------------------------------------------------------------------------

## 🤖 Machine Learning

The modelling work is contained in:

``` text
traning/model_training.ipynb
```

The notebook uses **scikit-learn** preprocessing pipelines and
regression models.

Models explored include:

-   Linear Regression
-   Decision Tree Regressor
-   Random Forest Regressor
-   Gradient Boosting Regressor
-   XGBoost Regressor

The current modelling workflow includes:

-   Train/test split
-   One-hot encoding
-   Ordinal encoding
-   Target encoding
-   Numerical feature handling
-   Pipeline-based preprocessing
-   Regression prediction
-   Model evaluation

### Evaluation metrics

The project uses:

-   **R² Score**
-   **Mean Absolute Error (MAE)**
-   **Mean Squared Error (MSE)**

------------------------------------------------------------------------

## 🗂️ Project Structure

``` text
Used-Car-Price-Prediction/
│
├── data/
│   ├── data_raw.csv
│   ├── data_cleaned-v1.csv
│   ├── data_cleaned-v2.csv
│   ├── data_cleaned-v3.csv
│   ├── data_cleaned-v4.csv
│   ├── data_cleaned-v5.csv
│   ├── data_cleaned-v6.csv
│   └── data_cleaned-v7.csv
│
├── data-cleaning/
│   ├── cleaning-1.ipynb
│   ├── cleaning-2.ipynb
│   ├── cleaning-3.ipynb
│   ├── cleaning-4.ipynb
│   ├── cleaning-5.ipynb
│   ├── cleaning-6.ipynb
│   ├── cleaning-7.ipynb
│   ├── all_col_name.json
│   └── columns-info.json
│
├── scraping-data/
│   ├── carwale-urls/
│   ├── output/
│   ├── scrape-car-details.py
│   ├── scrape-urls-new.py
│   ├── scrape-urls-old.py
│   └── convert-jsonl-to-df.ipynb
│
├── traning/
│   └── model_training.ipynb
│
├── check_data.ipynb
├── index.txt
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

## 🛠️ Technologies Used

  Area               Technologies
  ------------------ -------------------------------------
  Programming        Python
  Data Analysis      Pandas, NumPy
  Visualization      Matplotlib, Seaborn
  Web Scraping       Playwright, BeautifulSoup, Requests
  Machine Learning   Scikit-learn, XGBoost
  Development        Jupyter Notebook, VS Code
  Version Control    Git & GitHub

------------------------------------------------------------------------

## 🚀 Getting Started

### 1. Clone the repository

``` bash
git clone https://github.com/amritansh020/Used-Car-Price-Prediction.git
cd Used-Car-Price-Prediction
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Install Playwright browsers

``` bash
python -m playwright install chromium
```

### 4. Explore the notebooks

Open the project in VS Code or Jupyter and start with:

``` text
check_data.ipynb
```

Then review the notebooks inside:

``` text
data-cleaning/
```

and the model-training notebook:

``` text
traning/model_training.ipynb
```

------------------------------------------------------------------------

## 💡 What I Learned From This Project

This project gave me practical exposure to an end-to-end data workflow:

-   Collecting real-world web data
-   Handling messy and inconsistent datasets
-   Working with missing values and duplicates
-   Performing EDA
-   Selecting meaningful features
-   Encoding categorical variables
-   Building reproducible ML pipelines
-   Evaluating regression models
-   Managing a data-science project with Git and GitHub

------------------------------------------------------------------------

## 🔮 Future Improvements

Possible next steps include:

-   Improve model accuracy through systematic hyperparameter tuning
-   Compare models using consistent validation
-   Reduce unnecessary features
-   Add stronger outlier handling
-   Build a polished Streamlit prediction interface
-   Add interactive visualizations
-   Add automated data-refreshing pipelines
-   Deploy the final application

------------------------------------------------------------------------

## ⚠️ Data & Usage Note

The project uses data collected from CarWale for educational and
analytical purposes.

If you reuse or extend this project, respect the source website's terms
of service, robots.txt, and applicable laws/policies.

------------------------------------------------------------------------

## 👤 Author

**Amritansh**

GitHub: [@amritansh020](https://github.com/amritansh020)

------------------------------------------------------------------------

## 📄 License

This project is intended primarily for educational and portfolio
purposes.
