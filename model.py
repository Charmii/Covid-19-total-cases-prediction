df.count()
df.isna().sum()/len(df)
#None of the columns have null values more than 50%


#Filling mean value in numerical columns 
df["new_tests"].fillna(df['new_tests'].mean(), inplace = True) 
df["total_tests_per_thousand"].fillna(df['total_tests_per_thousand'].mean(), inplace = True) 
df["new_tests_per_thousand"].fillna(df['new_tests_per_thousand'].mean(), inplace = True) 
df["new_tests_smoothed"].fillna(df['new_tests_smoothed'].mean(), inplace = True) 
df["new_tests_smoothed_per_thousand"].fillna(df['new_tests_smoothed_per_thousand'].mean(), inplace = True) 
df["stringency_index"].fillna(df['stringency_index'].mean(), inplace = True)
df["total_tests"].fillna(df['total_tests'].mean(), inplace = True) 
df.count()


#Filling mode value in categorical columns 
df["tests_units"] = df["tests_units"].fillna(df["tests_units"].mode())
df["tests_units"].fillna("samples tested")
df.count()


import datetime as dt
df["date"]=pd.to_datetime(df["date"])
df["date"]=df["date"].map(dt.datetime.toordinal)
df["date"]


#Removing categorical variables
df = df.drop(['iso_code','location','tests_units','continent'] , axis =1)
df = df.drop(['population','population_density','median_age','aged_65_older','aged_70_older',
'gdp_per_capita','extreme_poverty','cvd_death_rate','diabetes_prevalence','female_smokers',
'male_smokers','handwashing_facilities','hospital_beds_per_thousand','life_expectancy'], axis = 1)

y = df['total_cases']
X = df.drop(['total_cases'], axis = 1)


#Splitting test and training set using train_test_split
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size = 0.25)

#Random Forest Regressor 
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators =20, random_state = 0)
regressor.fit(X_train, Y_train)
y_pred = regressor.predict(X_test)


import math 
RMSE = (Y_test-y_pred)*(Y_test - y_pred)
RMSE = RMSE.mean()
RMSE = math.sqrt(RMSE)
print(RMSE)


#Multiple linear regressor 
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X_train, Y_train)
y_predicted = reg.predict(X_test)


RMSE_m = (Y_test-y_predicted)*(Y_test - y_predicted)
RMSE_m = RMSE_m.mean()
RMSE_m = math.sqrt(RMSE_m)
print(RMSE_m)

new_date = df[df.date == 737552]
new_date

new_date = new_date.drop(['total_cases'],axis =1)
reg.predict(new_date) #Linear regression
regressor.predict(new_date) #Random Forest 

