
#  Final Submission Data Analytics with Bike Rentals Dataset

## 1. Project Structures
### Notebook
1. Data Wrangling:
 - Gathering data
 - Assessing data
 - Cleaning data
2. Exploratory Data Analysis:
 - Defined business questions for data exploration
 - Create Data exploration
3. Data Visualization:
 - Create Data Visualization that answer business questions

### Dashboard:
 - Set up the DataFrame which will be used
 - Make filter components on the dashboard
 - Add data visualizations to Dashboard


## 2. File Structures
```
.
├── dashboard
│   ├── handler
│   │   ├── DataHandler.py
│   ├── views
│   │   ├── charts.py
│   │   ├── columns.py
│   |   └── sidebar.py
│   ├── dashboard.py
│   ├── days_bike_rent_clean.csv
|   └── hours_bike_rent_clean.csv
├── dataset
│   ├── day.csv
|   └── hour.csv
├── README.md
├── .gitignore
├── bike_rent_data_preps_and_visualization.ipynb
├── requirements.txt
└── url.txt
```

## 3. Getting Started
### `bike_rent_data_preps_and_visualization.ipynb`
1. Open Google Colab in browser.
2. Klik **Open Colab** then klik Browse, choose this .ipynb file then klik *Open*.
4. Connect to runtime then run this code.
5. Then download cleaned dataset.

### `dashboard/dashboard.py`
1. Install all Requirement modules with `pip install -r requirements.txt`.
2. Don't move or delete .csv file in both dataset and dashboard directory, that csv file is an data source for notebook and dashboard.
3. Open Code Editor or Terminal and run the file by write it `streamlit run ./dashboard/dashboard.py`.
4. then open url in url.txt to browser.