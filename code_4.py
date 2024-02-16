import csv
import pandas
big_mac_file = './big-mac-full-index.csv'

df = pandas.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    filter_df_year = df[df['date']== year]
    filter_df_country = df[df['iso_a3'].str.lower() == country_code]
    
    mean_price_year = filter_df_year['dollar_price'].mean()
    mean_price_country = filter_df_country['dollar_price'].mean()
    return round(mean_price_year,2), round(mean_price_country, 2)

def get_big_mac_price_by_country(country_code):
    filter_df = df[df['iso_a3'] == country_code]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    if filter_df.empty:
        return "No data available for the specified year."
    else:
        cheapest_row = filter_df.loc[filter_df['dollar_price'].idxmin()]
        country_name = cheapest_row['name']
        country_code = cheapest_row['iso_a3']
        dollar_price = cheapest_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    if filter_df.empty:
        return "No data available for the specified year."
    else:
        expensive_row = filter_df.loc[filter_df['dollar_price'].idxmax()]
        country_name = expensive_row['name']
        country_code = expensive_row['iso_a3']
        dollar_price = expensive_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2000,'ARG'))
    print(get_big_mac_price_by_country('IND'))
    print(get_the_cheapest_big_mac_price_by_year(2012))
    print(get_the_most_expensive_big_mac_price_by_year(2003))

