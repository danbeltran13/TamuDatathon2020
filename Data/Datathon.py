import pandas as pd

#read csv
data_cities = pd.DataFrame(pd.read_csv("cities.csv"))
data_cities = data_cities.set_index("City")
data_qof = pd.DataFrame(pd.read_csv("movehubqualityoflife.csv"))
data_qof = data_qof.set_index("City")
data_cof = pd.DataFrame(pd.read_csv("movehubcostofliving.csv"))
data_cof = data_cof.set_index("City")
#merge data and create new dataframe
data = data_cities.merge(data_cof,right_index= True, left_index = True)
data = data.merge(data_qof, right_index= True, left_index= True)
data = data.loc[data['Country'] == "United States"]
us_cities = pd.DataFrame(pd.read_csv("datathon cities.csv"))
us_cities = us_cities.set_index("City")
data = us_cities.merge(data, right_index = True, left_index = True)
columns = list(data.columns)


#narrow data for user
