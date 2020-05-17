#!/usr/bin/env python
# coding: utf-8

# In[177]:


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


# In[178]:


# Read data file
dataFile = '/Users/binglin/Desktop/168DataSets/cleaned_users_neighborhood_anon.csv'
#dataFile = '/Users/binglin/Desktop/168DataSets/demo.csv'


# In[179]:


userCount = 0
#for userCount, line in enumerate(open('/Users/binglin/Desktop/168DataSets/demo.csv')):
for userCount, line in enumerate(open('/Users/binglin/Desktop/168DataSets/cleaned_users_neighborhood_anon.csv')):
    pass
    userCount += 1
print ("Total user count ",userCount-1)


# In[180]:


#Read characterizations list
with open(dataFile) as f:
    reader = csv.reader(f)
    header = next(reader)
    
    columns = []
    #Read column header
    for i, columnsHeader in enumerate(header):
        print(i+1,columnsHeader)
        columns.append(columnsHeader)
    print(columns)
    data = pandas.read_csv(dataFile,names = columns)


# In[230]:


# General characterization
# csv file format change to UTF-8

# Favorites
favorites = pd.DataFrame()
favorites['Favorites'] = data.favorites_count.tolist()[1:]
favorites = favorites.astype(float)
favorites.plot.hist(favorites,grid = True,bins = 30,color = '#607c8e',title = 'Data distribution - Favorites',orientation = 'horizontal')


tweets = pd.DataFrame()
tweets['Tweets'] = data.tweet_number.tolist()[1:]
tweets = tweets.astype(float)
tweets.plot.hist(tweets,grid = True,bins = 40,color = '#607c8e',title = 'Data distribution - Tweets',orientation = 'horizontal')


retweets = pd.DataFrame()
retweets['Retweets'] = data.retweet_number.tolist()[1:]
retweets = retweets.astype(float)
retweets.plot.hist(retweets,grid = True,bins = 40,color = '#607c8e',title = 'Data distribution - Retweets',orientation = 'horizontal')

statusLength = pd.DataFrame()
statusLength['Status length'] = data.status_length.tolist()[1:]
statusLength = statusLength.astype(float)
statusLength.plot.hist(statusLength,grid = True,bins = 100,color = '#607c8e',title = 'Data distribution - Status Length',orientation = 'horizontal')



# In[186]:


# Time between tweets not avaliable in the given file


# In[231]:


# Content Analysis

# Hashtags
hashtags = pd.DataFrame()
hashtags['Hashtags'] = data.number_hashtags.tolist()[1:]
hashtags = hashtags.astype(float)
hashtags.plot.hist(hashtags,grid = True,bins = 30,color = '#607c8e',title = 'Data distribution - Hashtags',orientation = 'horizontal')




# Mentions
mentions = pd.DataFrame()
mentions['Mentions'] = data.mentions.tolist()[1:]
mentions = mentions.astype(float)
mentions.plot.hist(mentions,grid = True,bins = 30,color = '#607c8e',title = 'Data distribution - Mentions',orientation = 'horizontal')




# Number of URLs
numURL = pd.DataFrame()
numURL['numURL'] = data.number_urls.tolist()[1:]
numURL = numURL.astype(float)
numURL.plot.hist(numURL,grid = True,bins = 30,color = '#607c8e',title = 'Data distribution - Number of URLs',orientation = 'horizontal')

# Sentiment analysis


# In[219]:


# Account evaluation

followers = pd.DataFrame()
followers['Followers'] = data.followers_count.tolist()[1:]
followers = followers.astype(float)
followers.plot.hist(followers,bins = 500,color = '#607c8e',title = 'Data distribution - Followers',xlim = (0,3000000),ylim = (0,100000))
#print(followers.mean())
#print(followers.median())
#print(followers.std())
# Mean 45941.0
# Median 3086.0
# Std 153358.566675



followees = pd.DataFrame()
followees['Hashtags'] = data.followees_count.tolist()[1:]
followees = followees.astype(float)
followees.plot.hist(followees,bins = 20,color = '#607c8e',title = 'Data distribution - Followees')
#print(followees.mean())
#print(followees.median())
#print(followees.std())
# Mean 2631.241379.0
# Median 997.0
# Std 4010.916565

#df = [followers,followees]
#df[['followers','followees']].plot.hist()
#followship = pd.DataFrame({'Followers': ['Followers'],'Followees': followees[1]},columns = ['Followers','Followees'])


# In[ ]:




