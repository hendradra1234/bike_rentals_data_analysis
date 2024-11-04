def get_total_count_by_hour_df(hour_df):
  hours_rent_count_df =  hour_df.groupby(by="hours").agg({"count_cr": ["sum"]})
  return hours_rent_count_df

def count_by_days_bike_rent_df(days_bike_rent_df):
    days_bike_rent_df_count = days_bike_rent_df.query(str('dteday >= "2011-01-01" and dteday < "2012-12-31"'))
    return days_bike_rent_df_count

def total_registered_df(days_bike_rent_df):
   registered_rent_df =  days_bike_rent_df.groupby(by="dteday").agg({
      "registered": "sum"
    })
   registered_rent_df = registered_rent_df.reset_index()
   registered_rent_df.rename(columns={
        "registered": "register_sum"
    }, inplace=True)
   return registered_rent_df

def total_casual_rent_type_df(days_bike_rent_df):
   casual_rent_df =  days_bike_rent_df.groupby(by="dteday").agg({
      "casual": ["sum"]
    })
   casual_rent_df = casual_rent_df.reset_index()
   casual_rent_df.rename(columns={
        "casual": "casual_sum"
    }, inplace=True)
   return casual_rent_df

def sum_order(hour_df):
    sum_order_items_df = hour_df.groupby("hours").count_cr.sum().sort_values(ascending=False).reset_index()
    return sum_order_items_df

def groupby_season(days_bike_rent_df):
    rent_by_season_df = days_bike_rent_df.groupby(by="season").count_cr.sum().reset_index() 
    return rent_by_season_df