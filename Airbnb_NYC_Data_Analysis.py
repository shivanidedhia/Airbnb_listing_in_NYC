#!/usr/bin/env python
# coding: utf-8

# # NYC Airbnb Bookings
# ### Python Final Project

# #### Akhila Pamukuntla and Shivani Dedhia

# In[41]:


import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import warnings


# In[9]:


url="https://raw.githubusercontent.com/shivanidedhia/Airbnb_listing_in_NYC/main/AB_NYC_2019.csv"


# In[11]:


s=requests.get(url).content
airbnb=pd.read_csv(io.StringIO(s.decode('utf-8')))


# In[12]:


# understanding the first few coloumns of the Airbnb Data set
airbnb.head()


# In[13]:


# number of rows in the Airbnb Datasets
len(airbnb)


# In[14]:


# type of object in each coloumn
airbnb.dtypes


# ### Cleaning the Data

# In[20]:


# Understanding the empty cells in each col. 
airbnb.isnull().sum()


# #### Last_review and reviews_per_month have the most amount of empty col. which makes sense since it is an optional field

# In[22]:


# Dropping coloumns which are not as significant
airbnb.drop(['id','host_name','last_review'], axis=1, inplace=True)


# In[25]:


# All NaN values in 'reviews_per_month' are replaced with 0
airbnb.fillna({'reviews_per_month':0}, inplace=True)
airbnb.isnull().sum()


# #### Only name coloumn now has 16 missing values

# In[26]:


# Which neighbourhoods are present in the dataset?
airbnb.neighbourhood_group.unique()


# #### As suspected, all 5 boroughs of New York City are present in the Airbnb NYC Dataset

# In[27]:


# What type of rooms are available on Airbnb?
airbnb.room_type.unique()


# #### Private Room, Entire home/apt, and Shared room are all the choices available while booking an Airbnb

# ### Exploring and Visualizing the Data

# In[76]:


#setting figure size for visualizations
sns.set(rc={'figure.figsize':(10,8)})
sns.set_style('white')


# In[29]:


# Which hosts have had the most amount of bookings?
hosts_w_most_bookings = airbnb.host_id.value_counts()


# In[ ]:





# In[38]:


# Top 5 hosts with the highest Airbnb bookings
top_5 = hosts_w_most_bookings.head()
top_5


# In[99]:


top_host=pd.DataFrame(top_5)
top_host.reset_index(inplace=True)
top_host.rename(columns={'index':'Host_ID', 'host_id':'Booking_Count'}, inplace=True)
top_host


# In[113]:


sns.barplot(x="Host_ID", 
            y="Booking_Count", 
            data=top_host,
            order=top_host.sort_values('Booking_Count').Host_ID,
            palette="magma")


# In[57]:


sns.countplot(x = 'neighbourhood_group',
              data = airbnb,
              order = airbnb['neighbourhood_group'].value_counts().index,
              palette="magma")
plt.xlabel("New York City's Borough's", size=10)
plt.ylabel("Number of Airbnb Listings", size=10)
plt.title("Listings by Boroughs", size=18)


# #### Manhattan has the most amount of bookings followed by Brooklyn which is intuitive

# In[72]:


plt.figure(figsize=(20,12))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue= airbnb.room_type, palette="magma")


# #### Creating a violin plot to show the price distribution
# ###### Prices had to be normalized so, prices above 500 are removed for the sake of the visualisation

# In[85]:


price_less_500 = airbnb[airbnb.price < 500]


# In[86]:


sns.violinplot(data=price_less_500, x='neighbourhood_group', y='price')
plt.xlabel("Boroughs", size=10)
plt.ylabel("Airbnb Price", size=10)
plt.title("Price by Neighborhood", size=18)


# In[ ]:





# In[ ]:




