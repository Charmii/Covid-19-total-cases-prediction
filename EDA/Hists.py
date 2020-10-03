
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
df = df[df.location == 'India']
fig = plt.figure(figsize = (15,10))
plt.subplots_adjust(top = 0.99, bottom=0.01, hspace=1.0, wspace=0.4)

#Univariate Analysis 
#Histograms 
plt.subplot(6,5,1)
sns.distplot(df['total_cases'],color = 'red', kde = False,bins = 8);
plt.subplot(6,5,2)
sns.distplot(df['new_cases'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,3)
sns.distplot(df['total_deaths'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,4)
sns.distplot(df['total_cases_per_million'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,5)
sns.distplot(df['new_cases_per_million'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,6)
sns.distplot(df['total_deaths_per_million'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,7)
sns.distplot(df['new_deaths_per_million'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,8)
sns.distplot(df['total_tests'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,9)
sns.distplot(df['total_tests_per_thousand'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,10)
sns.distplot(df['new_tests_per_thousand'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,11)
sns.distplot(df['new_tests_smoothed'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,12)
sns.distplot(df['new_tests_smoothed'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,13)
sns.distplot(df['stringency_index'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,14)
sns.distplot(df['population'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,15)
sns.distplot(df['population_density'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,16)
sns.distplot(df['median_age'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,17)
sns.distplot(df['aged_65_older'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,18)
sns.distplot(df['aged_70_older'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,19)
sns.distplot(df['gdp_per_capita'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,20)
sns.distplot(df['extreme_poverty'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,21)
sns.distplot(df['cvd_death_rate'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,22)
sns.distplot(df['diabetes_prevalence'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,23)
sns.distplot(df['female_smokers'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,24)
sns.distplot(df['male_smokers'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,25)
sns.distplot(df['handwashing_facilities'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,26)
sns.distplot(df['hospital_beds_per_thousand'],color = 'red', kde = False, bins = 10);
plt.subplot(6,5,27)
sns.distplot(df['life_expectancy'],color = 'red', kde = False, bins = 10);





plt.subplot(6,5,1)
sns.distplot(df['total_cases'],color = 'red', kde = True,bins = 8);
plt.subplot(6,5,2)
sns.distplot(df['new_cases'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,3)
sns.distplot(df['total_deaths'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,4)
sns.distplot(df['total_cases_per_million'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,5)
sns.distplot(df['new_cases_per_million'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,6)
sns.distplot(df['total_deaths_per_million'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,7)
sns.distplot(df['new_deaths_per_million'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,8)
sns.distplot(df['total_tests'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,9)
sns.distplot(df['total_tests_per_thousand'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,10)
sns.distplot(df['new_tests_per_thousand'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,11)
sns.distplot(df['new_tests_smoothed'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,12)
sns.distplot(df['new_tests_smoothed'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,13)
sns.distplot(df['stringency_index'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,14)
sns.distplot(df['population'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,15)
sns.distplot(df['population_density'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,16)
sns.distplot(df['median_age'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,17)
sns.distplot(df['aged_65_older'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,18)
sns.distplot(df['aged_70_older'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,19)
sns.distplot(df['gdp_per_capita'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,20)
sns.distplot(df['extreme_poverty'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,21)
sns.distplot(df['cvd_death_rate'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,22)
sns.distplot(df['diabetes_prevalence'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,23)
sns.distplot(df['female_smokers'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,24)
sns.distplot(df['male_smokers'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,25)
sns.distplot(df['handwashing_facilities'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,26)
sns.distplot(df['hospital_beds_per_thousand'],color = 'red', kde = True, bins = 10);
plt.subplot(6,5,27)
sns.distplot(df['life_expectancy'],color = 'red', kde = True, bins = 10);



