# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# import sqlite3


# # Extraire de l'information
# data = urlopen('https://fr.wikipedia.org/wiki/Surnom_des_%C3%A9quipes_nationales_de_rugby_%C3%A0_XV')
# data = data.read()


# # Transformation d'information
# soup = BeautifulSoup(data)
# team_table = soup.find('table', {'class':'wikitable'})

# tds = soup.find_all('span', {'class':'nowrap'})


# flag_urls = []
# flag_titles = []
# countries = []

# for td in tds:
#     flag_url = td.find('a', {'class':'mw-file-description'})['href']
#     #flag_title = td.find('a', {'class':'mw-file-description'})['title']
#     country = (td.text)
    
#     flag_urls.append(flag_url)
#     #flag_titles.append(flag_title)
#     countries.append(country)
    
    
# data = {'flag_urls':flag_urls, 'countries':countries}
# data = pd.DataFrame(data)
# data['countries'] = data['countries'].str.strip()
# data['creation_date'] = datetime.now()


# # Loading

# con = sqlite3.connect("DATA/rugby_team.sqlite")

# # Write the new DataFrame to a new SQLite table
# data.to_sql("ODS", con, if_exists="replace", index=False)

# con.close()
# sql_query = """
# SELECT SUBSTR(countries, 1, 1) AS first_letter, COUNT(countries) FROM ODS
# GROUP BY SUBSTR(countries, 1, 1) ;
# """

# con = sqlite3.connect("DATA/rugby_team.sqlite")

# # Load the data into a DataFrame
# data = pd.read_sql_query(sql_query, con)

# con.close()
# sql_query = """
# SELECT SUBSTR(countries, 1, 1) AS first_letter, COUNT(countries) FROM ODS
# GROUP BY SUBSTR(countries, 1, 1) ;
# """

# con = sqlite3.connect("DATA/rugby_team.sqlite")

# # Load the data into a DataFrame
# data = pd.read_sql_query(sql_query, con)

# con.close()
# data.head()
# con = sqlite3.connect("DATA/rugby_team.sqlite")

# data = pd.read_sql_query("SELECT *, SUBSTR(countries, 1, 1) AS first_letter from ODS", con)

# columns = ['first_letter', 'countries']

# data[columns].groupby('first_letter').count()
# import pandas as pd

# test_result = pd.read_excel('report.xlsx')

# mask = test_result['result'] == 'PASSED'
# str((test_result[mask].shape[0] / test_result.shape[0]) * 100) + " %"