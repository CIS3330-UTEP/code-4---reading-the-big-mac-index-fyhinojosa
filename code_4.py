import csv
import pandas
big_mac_file = './big-mac-full-index.csv'

df = pandas.read_csv('big-mac-full-index.csv')

def get_big_mac_price_by_year(year,country_code):
    filter_df = df[(df['date']== year) & (df['iso_a3'].str.lower() == country_code)]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_big_mac_price_by_country(country_code):
    filter_df = df[df['iso_a3'] == country_code]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    cheapest_row = filter_df.loc[filter_df['dollar_price'].idxmin()]
    country_name = cheapest_row['name']
    country_code = cheapest_row['iso_a3']
    dollar_price = cheapest_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filter_df = df[df['date'] == year]
    expensive_row = filter_df.loc[filter_df['dollar_price'].idxmax()]
    country_name = expensive_row['name']
    country_code = expensive_row['iso_a3']
    dollar_price = expensive_row['dollar_price']
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

if __name__ == "__main__":
    print(get_big_mac_price_by_year(2006,'MEX'))
    print(get_big_mac_price_by_country('MEX'))
    print(get_the_cheapest_big_mac_price_by_year(2008))
    print(get_the_most_expensive_big_mac_price_by_year(2003))

