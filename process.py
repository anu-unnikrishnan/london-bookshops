import pandas as pd 

#load data that lives in bookshops.csv
data = pd.read_csv('bookshops.csv')

#only extract bookshops that are open 
bookdata = data[(data['open'])]

#only extract bookshops that aren't chains, i.e. wh smith, waterstones, blackwell’s, the works, daunt books, foyles
bookdata = bookdata[(data['name'].str.contains("WHSmith") == False)]
bookdata = bookdata[(data['name'].str.contains("Waterstones") == False)]
bookdata = bookdata[(data['name'].str.contains("Blackwell's") == False)]
bookdata = bookdata[(data['name'].str.contains("The Works") == False)]
bookdata = bookdata[(data['name'].str.contains("Daunt Books") == False)]
bookdata = bookdata[(data['name'].str.contains("Foyles") == False)]

#only keep the columns we need 
bookdata = bookdata[['name', 'lat', 'long']]

#write to file 
bookdata.to_csv('indie_bookshops.csv', index = False)