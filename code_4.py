import csv
import pandas
big_mac_file = './big-mac-full-index.csv'

df = pandas.read_csv('big-mac-full-index.csv')
# iso_a3_values = df['iso_a3'].unique()
# print(iso_a3_values)



def get_big_mac_price_by_year(year,country_code):
    country_codes = ['ARG' 'AUS' 'BRA' 'CAN' 'CHE' 'CHL' 'CHN' 'CZE' 'DNK' 'EUZ' 'GBR' 'HKG'
 'HUN' 'IDN' 'ISR' 'JPN' 'KOR' 'MEX' 'MYS' 'NZL' 'POL' 'RUS' 'SGP' 'SWE'
 'THA' 'TWN' 'USA' 'ZAF' 'PHL' 'NOR' 'PER' 'TUR' 'VEN' 'EGY' 'COL' 'CRI'
 'LKA' 'PAK' 'SAU' 'UKR' 'URY' 'ARE' 'IND' 'VNM' 'AZE' 'BHR' 'GTM' 'HND'
 'HRV' 'JOR' 'KWT' 'LBN' 'MDA' 'NIC' 'OMN' 'QAT' 'ROU']
    filter_df = df[(df['date'].str.startswith(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]
    mean_price = filter_df['dollar_price'].mean()
    # filter_df = df[df[country_codes].str.lower() == country_code] & df[(df['date'] == year)]
    return round(mean_price,2)
    

    # filter_df_year = df[df['date'] == year]
    # filter_df = df[df['iso_a3'].str.lower() == country_code]
    # mean_price = filter_df['dollar_price'].mean()
    # return round(mean_price,2), filter_df_year
    # filter_df_country = df[df['iso_a3'].str.lower() == country_code]
    
    # mean_price_year = filter_df_year['dollar_price'].mean()
    # mean_price_country = filter_df_country['dollar_price'].mean()
    # return round(mean_price_year,2), round(mean_price_country, 2)

def get_big_mac_price_by_country(country_code):
    filter_df = df[df['iso_a3'].str.lower() == country_code]
    mean_price = filter_df['dollar_price'].mean()
    return round(mean_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    filter_df = df[df['date'].str.startswith(str(year))]
    min_price = filter_df['dollar_price'].min()
    cheapest_row = filter_df[filter_df['dollar_price'] == min_price].iloc[0]
    country_name = cheapest_row['name']
    country_code = cheapest_row['iso_a3']
    dollar_price = cheapest_row['dollar_price']
    
    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filter_df = df[df['date'].str.startswith(str(year))]
    max_price = filter_df['dollar_price'].max()
    cheapest_row = filter_df[filter_df['dollar_price'] == max_price].iloc[0]
    country_name = cheapest_row['name']
    country_code = cheapest_row['iso_a3']
    dollar_price = cheapest_row['dollar_price']

    return f"{country_name}({country_code}): ${round(dollar_price, 2)}"

if __name__ == "__main__":
    function_1 = get_big_mac_price_by_year(2000,'bra')
    print(function_1)

    function_2 = get_big_mac_price_by_country('ind')
    print(function_2)

    fucntion_3 = (get_the_cheapest_big_mac_price_by_year(2012))
    print(fucntion_3)

    function_4 = (get_the_most_expensive_big_mac_price_by_year(2003))
    print(function_4)

