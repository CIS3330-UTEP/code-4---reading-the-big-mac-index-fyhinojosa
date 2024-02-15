import csv
import pandas
big_mac_file = './big-mac-full-index.csv'

df = pandas.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    filter_df = df[(df['date']== year) & (df['iso_a3']== country_code.lower())]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_big_mac_price_by_country(country_code):
    filter_df = df[df['iso_a3'] == country_code]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    min_price = int(filter_df['dollar_price'].min())
    cheapest_row = min_price[filter_df['dollar_price'] == min_price['dollar_price'].iloc[0]]
    return round(cheapest_row,2)

def get_the_most_expensive_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    max_price = filter_df['dollar_price'].max()
    expensive_row = filter_df[filter_df['dollar_price'] == max_price].iloc[0]
    return expensive_row


if __name__ == "__main__":
    print(get_big_mac_price_by_year())
    print(get_big_mac_price_by_country())
    print(get_the_cheapest_big_mac_price_by_year())
    print(get_the_most_expensive_big_mac_price_by_year())

