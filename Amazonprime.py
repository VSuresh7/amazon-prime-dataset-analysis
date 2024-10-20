#!/usr/bin/env python
# coding: utf-8

# In[8]:


#importing a csv dataset from device
import pandas as pd
data = pd.read_csv("C:\\Users\\Vadty\\OneDrive\\Desktop\\DA\\PythonProject\\amazon_prime_titles.csv")
data


# In[11]:


#To get top 9 rows from whole dataset
data.head(9)


# In[10]:


#to get bottom 9 rows
data.tail(9)


# In[13]:


#to get no. of rows and columns
data.shape


# In[14]:


#get number elements
data.size


# In[15]:


#To get all column names 
data.columns


# In[17]:


#To get data type of those columns
data.dtypes


# In[18]:


#To get overall information of dataset
data.info()


# In[27]:


#Checking for the number of duplicate records in this dataset
data.duplicated().sum()


# In[31]:


#To Remove duplicates
data.drop_duplicates(inplace = True)


# In[32]:


#Null values present in dataset
data.isnull()


# In[156]:


#Null values present in dataset at a particular column
df[df["date_added"].isnull()]


# In[37]:


#To get count of null values at particular column
data.isnull().sum()


# In[40]:


import seaborn as sns
sns.heatmap(data.isnull())


# In[78]:


data[data['release_year'].isin(['2008'])]


# In[60]:


data.dtypes


# In[81]:


#dt.year.value_counts
data['date'].dt.year.value_counts()


# In[3]:


import pandas as pd
df = pd.read_csv("C:\\Users\\Vadty\\OneDrive\\Desktop\\DA\\PythonProject\\amazon_prime_titles.csv")
df


# In[4]:


df.head(16)


# In[6]:


#to  get number of tv shows and movies
bar=df.groupby("type").type.count()
bar


# In[20]:


#TO make a scatterplot using seaborn
import seaborn as sns
sns.scatterplot(bar)
df.groupby('type').type.count()


# In[35]:


#To show Tv Shows which are released in 2014
df[(df["type"]=='TV Show')&(df["release_year"]==2014)]


# In[45]:


#To show titles of all Tv Shows which are released in India
df[(df['type']=='TV Show')&(df['country']=='India')]['title']

    


# In[57]:


df[df['director'].duplicated()]


# In[60]:


#Show top 10 directors who gave highest number of tv shows and movies
df['director'].value_counts().head(10)


# In[63]:


#To show all records, where type is Movie and listed in comedy or  country is united kingdom
df[(df['type']=='Movie')&(df['listed_in']=='Comedy')|(df['country']=='United Kingdom')]


# In[85]:


#To show how many movies/shows Leo Gorcey was acted
df['cast'].str.contains('Leo Gorcey').sum()


# In[87]:


#To Show how many movies are there directed by paul weiland
df['director'].str.contains('Paul Weiland').sum()


# In[104]:


#To split mins and units in separate column
df[['Minutes','Units']]=df['duration'].str.split(' ',expand=True)
df.head(4)


# In[128]:


#TO show Which Individual country has highest tv shows
Tv_Show=df[df['type']=='TV Show']
Top_Country=Tv_Show.country.value_counts()
print("The Country which has highest TV shows is:",Top_Country)


# In[144]:


import matplotlib.pyplot as plt
plt.pie(Top_Country,labels=Top_Country,autopct=None)
plt.show()


# In[148]:


df.sort_values(by='release_year',ascending=False)


# In[153]:


#Find all conditions where type is movie and listed in drama or type is Tv Show and Romantic
df[(df['type']=='Movie')&(df['listed_in']=='drama')|(df['type']=='TV Show')&(df['listed_in']=='Romance')]

