#!/usr/bin/env python
# coding: utf-8

# # Task1: Restaurant Ratings

# ## Analyze the distribution of aggregate ratings and determine the most common rating range

# In[91]:


import pandas as pd


# In[92]:


df = pd.read_csv("Dataset.csv")
df.head(2)


# In[93]:


occ_rating = df["Aggregate rating"].value_counts()
occ_rating


# In[94]:


res = df[df["Aggregate rating"]>3]
res.head(5)


# In[95]:


#Analysis on Distribution of Aggregate Rating
df["Aggregate rating"].describe()


# In[96]:


#Most Common Ratings
df["Aggregate rating"].mode()


# In[97]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.bar(occ_rating.index,occ_rating.values,width=0.09)
plt.xlabel("Aggregate rating")
plt.ylabel("Occurence")
plt.title("Most Common Rating Analysis")
plt.show()


# ## Calculate the average number of votes received by restaurants

# In[98]:


df["Votes"].describe()


# In[99]:


#Average Number of Votes Received by restaurants are 156.90


# In[100]:


vote = df["Votes"].value_counts()
vote


# In[101]:


#names of restaurant getting votes less than 5
df[["Restaurant Name","Votes","Has Online delivery"]][(df["Votes"]<5)]


# # Task2: Cuisine Combination

# ## Identify the most common combinations of cuisines in the dataset

# In[102]:


df.head(5)


# In[103]:


data = df["Cuisines"].value_counts().head(10)
data


# cuisines_combo = pd.DataFrame({'Cuisines Combination.':data.index,'Occurence':data.values})
# cuisines_combo

# # Task3: Geographical Analysis

# ##  Plot the locations of restaurants on a map using longitude and latitude coordinates

# In[104]:


pip install folium


# In[105]:


import folium


# In[106]:


new_df1 = pd.DataFrame({'Restaurant Name':df["Restaurant Name"],'City':df["City"],'Latitude':df["Latitude"],'Longitude':df["Longitude"]})
new_df1


# In[109]:


df["Popularity"] = (df["Aggregate rating"]/5)*100
df.head(2)


# In[135]:


new_df3 = df[["City","Latitude","Longitude","Popularity"]][df["Popularity"]>98]
new_df3


# In[145]:


new_df4 = df[["City","Latitude","Longitude","Popularity"]][df["Popularity"]<50].head(100)
new_df4


# In[146]:


avg_lat = df["Latitude"].mean()
avg_lon = df["Longitude"].mean()
print(f'Average_latitude:',avg_lat)
print(f'Average_longitude:',avg_lon)


# In[144]:


import folium
mymap = folium.Map(location=[avg_lat,avg_lon],zoom_start=1)
mymap

for idx,rows in new_df3.iterrows():
    folium.Marker(
        location=[rows['Latitude'],rows['Longitude']],
        tooltip=(rows['City'],"Most popular"),
        icon = folium.Icon(color="green",icon="glyphicon glyphicon-glass")
        ).add_to(mymap)
    
for idx,rows in new_df4.iterrows():
    folium.Marker(
        location=[rows['Latitude'],rows['Longitude']],
        tooltip=(rows['City'],"Least Popular"),
        icon = folium.Icon(color="red",icon="glyphicon glyphicon-glass")
        ).add_to(mymap)

mymap


#  ## Identify any patterns or clusters of restaurants in specific areas

# In[ ]:


#from the geographical analysis of dataset it is found that
#The most Popular restaurants are located in: INDIA


# In[165]:


mymap = folium.Map(location=[avg_lat,avg_lon],zoom_start=5)
mymap

for idx,rows in new_df3.iterrows():
    folium.CircleMarker(
        radius=50,
        location=[rows['Latitude'],rows['Longitude']],
        tooltip=(rows['City'],"Most popular"),
        icon = folium.Icon(color="red",icon="glyphicon glyphicon-glass"),
        fill=True
        ).add_to(mymap)
mymap


# # Task4: Restaurant Chains

# ##  Identify if there are any restaurant chains present in the dataset.

# In[166]:


df["Restaurant Name"].duplicated().value_counts()


# In[167]:


#Chain restaurants are the restaurants  which have their franchise in different locations
chain_res = df.groupby("Restaurant Name").filter(lambda x:len(x)>1)
ch_res = chain_res[["Restaurant Name","City"]]


# In[168]:


ch_res.sort_values(by="Restaurant Name")


# In[169]:


counts = ch_res["Restaurant Name"].value_counts()
counts


# In[170]:


counts_df = pd.DataFrame({'Restaurant_Name':counts.index,'Locations':counts.values})
counts_df


# In[179]:


import seaborn as sns
sns.barplot(x=counts_df["Restaurant_Name"],y=counts_df["Locations"],data=counts_df,width=0.5)
plt.title("Top 25 Restaurant Chains in World")
plt.xticks(rotation=45,ha="right")
plt.xlim(0,25)
plt.show()


# ## Analyze the ratings and popularity of different restaurant chains.

# In[172]:


chain_res.head(2)


# In[173]:


rating = chain_res["Aggregate rating"].value_counts()


# In[174]:


rat1 = pd.DataFrame({'Ratings':rating.index,'No. of Resturants chains':rating.values})
rat1.head(10)


# In[175]:


sns.barplot(x=rat1["Ratings"],y=rat1["No. of Resturants chains"],data=rat1,width=0.5)
plt.xticks(rotation=90,ha='right')
plt.title("Ratings of Restaurant change")
plt.show()


# In[176]:


popular = df["Popularity"].value_counts()
popular


# In[177]:


pop1 = pd.DataFrame({'Popularity(in %)':popular.index,'No. Of Restaurants':popular.values})
pop1.sort_values("Popularity(in %)").head(5)


# In[178]:


sns.barplot(x=pop1["Popularity(in %)"],y=pop1["No. Of Restaurants"],data=pop1)
plt.xticks(rotation=90,ha='right')
plt.title("No.Of Restaurant Vs Popularity")
plt.show()


# In[ ]:




