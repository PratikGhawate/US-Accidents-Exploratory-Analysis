#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # US Accidents Exploratory Analysis
# 

# In[2]:


df = pd.read_csv("/Users/pghawate8458/Desktop/US_Accidents_Dec21_updated.csv")


# In[3]:


df.head(10)


# ### Data Preparation  and Cleaning
# Tasks  
# - Load the file using Pandas
# - Look at some information about the data & the columns
# - Fix any missing or incorrect values

# In[4]:


df 


# In[5]:


df.columns


# In[6]:


len(df)


# In[7]:


df.info()


# In[8]:


len(df.columns)


# In[9]:


df.describe()


# In[10]:


numerics = ['int16', 'int32','int64','float16','float32','float64']
numeric_df = df.select_dtypes(include=numerics)
len(numeric_df.columns)


# In[11]:


missing_percentages= df.isna().sum().sort_values(ascending=False)/len(df)
missing_percentages


# Percentage of missing values per column

# In[12]:


missing_percentages[missing_percentages != 0].plot(kind='barh')


# Remove columns that you don't want to use.
# 
# 

# 

# ### Exploratory Analysis and Visualization
# 1.City
# <br>
# 2.Start Time
# <br>
# 3.Start Lat, Start Lng
# <br>
# 4.Temperature
# <br>
# 5.Weather Condition

# In[13]:


cities=df.City.unique()
len(cities)


# In[14]:



import pandas as pd


# New york is not in the list

# In[15]:


df = pd.read_csv("/Users/pghawate8458/Desktop/US_Accidents_Dec21_updated.csv")


# In[16]:


missing_percentages= df.isna().sum().sort_values(ascending=False)/len(df)
missing_percentages


# In[17]:


missing_percentages[missing_percentages != 0].plot(kind='barh')


# In[18]:


cities=df.City.unique()
len(cities)


# In[19]:


cities=df.City.unique()
len(cities)


# In[20]:


cities_accidents = df.City.value_counts()
cities_accidents[:10]


# In[21]:


'New York' in df.City


# In[22]:


'New York' in df.State


# New York doesn't include in dataset

# In[23]:


cities_accidents[:15].plot(kind='barh')


# top 15 cities bar graph

# In[24]:


import seaborn as sns


# In[25]:


sns.set_style("whitegrid")


# In[26]:


sns.distplot(cities_accidents)


# In[27]:


high_city_accidents = cities_accidents[cities_accidents>=1000]
low_city_accidents = cities_accidents[cities_accidents<1000]


# In[28]:


len(high_city_accidents)/len(cities)


# less than 5% of the cities have more than 1000 accidents

# In[29]:


sns.histplot(cities_accidents, log_scale= True)


# In[30]:


cities_accidents[cities_accidents==1]


# over 1100 cities reported just single accidents

# ### Start Time

# In[31]:


df.Start_Time


# In[32]:


Start_Time=pd.to_datetime(df.Start_Time)
df.Start_Time[0]


# In[33]:


sns.histplot(Start_Time, log_scale=True)


# In[34]:


len(high_city_accidents)


# In[35]:


len(low_city_accidents)


# In[36]:


Start_Time=pd.to_datetime(df.Start_Time)
df.Start_Time[0]


# In[37]:


Start_Time


# In[38]:


Start_Time.dt.hour


# In[39]:


sns.distplot(Start_Time.dt.hour, bins= 24, kde= False, norm_hist= True)


# Most of the accidents occurs in 4pm - 7pm
# 

# In[40]:


sns.distplot(Start_Time.dt.dayofweek, bins=7, kde=False, norm_hist= True)


# On weekdays number of accidents are higher compared to weekends. So we might say that on weekdays rush is more.

# In[41]:


monday_accidents = df.Start_Time[Start_Time.dt.dayofweek==0]
monday_accidents= pd.to_datetime(monday_accidents)
sns.distplot(monday_accidents.dt.hour, bins= 24 , kde= False, norm_hist= True)


# On Weekdays peak is between 7am to 10am and between 3pm to 7pm. It might be at the time of starting of office hours and and after office hours

# In[42]:


Sunday_accidents = df.Start_Time[Start_Time.dt.dayofweek==6]
Sunday_accidents= pd.to_datetime(Sunday_accidents)


# In[43]:


sns.distplot(Sunday_accidents.dt.hour, bins= 24, kde= False, norm_hist= True)


# On weekends the graph of number of accidents is somewhat normally distrubuted and peak around 1pm to 8pm

# In[44]:


monthly_accidents = df.Start_Time
monthly_accidents= pd.to_datetime(monthly_accidents)
sns.distplot(monthly_accidents.dt.month,bins= 12, kde= False )


# Monthly Accidents of Graph

# In[45]:


accidents2018= df.Start_Time[Start_Time.dt.year==2020]
len(accidents2018)


# In[46]:


i = 2016
while i < 2022:
    accidents= df.Start_Time[Start_Time.dt.year==i]
    print( "The Number of accidents in yeart",i,"is",len(accidents))
    i += 1


# In[47]:


Yearly_Accidents = Start_Time.dt.year
Yearly_Accidents= pd.to_datetime(Yearly_Accidents)
sns.distplot(Yearly_Accidents, bins=6, kde= False )


# Rate of accidents are increasing year by year. It might be due to increase in vehicles on road which ultimately reflects increase in population

# In[48]:


accidents_2020 = df.Start_Time[Start_Time.dt.year==2020]
accidents_2020 = pd.to_datetime(accidents_2020)
sns.distplot(accidents_2020.dt.month, bins=12, kde= False)


# In year 2020 , data for 2 months is missing
# 

# ### Start Latitude and Start Longitude

# In[49]:


sns.scatterplot(x= df.Start_Lng, y= df.Start_Lat, size=0.0000001)


# In[50]:


sample_df= df.sample(int(0.1*len(df)))
sns.scatterplot(x=sample_df.Start_Lng, y= sample_df.Start_Lat, size= 0.0000001)


# In[51]:


pip install folium


# In[52]:


import folium 


# In[53]:


lat, lng = df.Start_Lat[0], df.Start_Lng[0]
lat, lng


# In[54]:



Map= folium.Map()
Marker= folium.Marker((lat,lng))
Marker.add_to(Map)
Map


# In[55]:


from folium.plugins import HeatMap


# In[56]:


lat_lng= list(zip(list(df.Start_Lat),list(df.Start_Lng)))


# In[57]:


Map = folium.Map()

HeatMap(lat_lng[:100000]).add_to(Map)
Map


# In[ ]:




