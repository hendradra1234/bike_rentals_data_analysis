import pandas as pd
import seaborn as sns

import handler.DataHandler as dh
import views.sidebar as sdb
import views.columns as coll
import views.charts as charts

sns.set_theme(style='dark')

day_dataset = "dashboard/days_bike_rent_clean.csv"
hours_dataset = "dashboard/hours_bike_rent_clean.csv"

# Data Initialization
days_bike_rent_df = pd.read_csv(day_dataset)
hours_bike_rent_df = pd.read_csv(hours_dataset)

datetime_columns = ["dteday"]
days_bike_rent_df.sort_values(by="dteday", inplace=True)
days_bike_rent_df.reset_index(inplace=True)

hours_bike_rent_df.sort_values(by="dteday", inplace=True)
hours_bike_rent_df.reset_index(inplace=True)

for column in datetime_columns:
    days_bike_rent_df[column] = pd.to_datetime(days_bike_rent_df[column])
    hours_bike_rent_df[column] = pd.to_datetime(hours_bike_rent_df[column])

min_date_days = days_bike_rent_df["dteday"].min()
max_date_days = days_bike_rent_df["dteday"].max()

min_date_hour = hours_bike_rent_df["dteday"].min()
max_date_hour = hours_bike_rent_df["dteday"].max()

start_date, end_date = sdb.viewSidebar(min_date_days, max_date_days)

main_df_days = days_bike_rent_df[(days_bike_rent_df["dteday"] >= str(start_date)) & 
                       (days_bike_rent_df["dteday"] <= str(end_date))]

main_df_hour = hours_bike_rent_df[(hours_bike_rent_df["dteday"] >= str(start_date)) & 
                        (hours_bike_rent_df["dteday"] <= str(end_date))]

# Data Processing
hour_count_df = dh.get_total_count_by_hour_df(main_df_hour)
days_bike_rent_count_2011_df = dh.count_by_days_bike_rent_df(main_df_days)
reg_df = dh.total_registered_df(main_df_days)
cas_df = dh.total_casual_rent_type_df(main_df_days)
sum_order_items_df = dh.sum_order(main_df_hour)
season_df = dh.groupby_season(main_df_hour)

# columns
coll.columns(days_bike_rent_count_2011_df, reg_df, cas_df)


# Charts
charts.seasonRentChart(season_df)
charts.sellingHoursRentChart(sum_order_items_df)
charts.rentTypeDistribution()
charts.sellingCharts(days_bike_rent_df)
charts.heatmapCorrelationVIew(hours_bike_rent_df)