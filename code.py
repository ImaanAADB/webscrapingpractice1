from bs4 import BeautifulSoup
import requests
import pandas as pd



url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

soup.find_all('table') # Gives us ALL the tables on the page
table = soup.find_all('table')[1] #This gives us the first table on the webpage

world_titles = table.find_all('th') # find the <th> tags within table using the find_all function again.
world_table_titles = [title.text.strip() for title in world_titles] # Use list comprehension to extract the table titles and clean up using.strip().
print (world_table_titles)


#Table Headers 
df = pd.DataFrame(columns = world_table_titles)


column_data = table.find_all('tr') #Finds all the rows in table and save it to column data.
for row in column_data:    #For ever single row <tr> in column data
    row_data = row.find_all('td') #Find all the <td> tags in each <tr> tag
    individual_row_data = [data.text.strip() for data in row_data] #For each <td> tag, we are striping tansforming into text.

#Looks at the length of the dataframe, which should be nothing prior to the loop start. And appending each row into the next position
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

#Prints Entire Table in Panda
print(df)

#Exports to csv file 
df.to_csv(r'C:\Users\ImaanAB\Documents\Data analyst Career Path\Project # 1 - Webscraping\Companies.csv', index = False)
