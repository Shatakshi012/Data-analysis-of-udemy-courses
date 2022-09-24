#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data= pd.read_csv('udemy_courses.csv',parse_dates=['published_timestamp'])
data.dtypes


# # Information of dataset

# In[3]:


data.info()


# # Number of column and rows in our dataset

# In[4]:


print("Number of rows:",data.shape[0])
print("Number of columns:",data.shape[1])


# # Display Top 5 Rows of The Dataset
#  

# In[5]:


data.head(5)


# # Display Last 5 Rows of The Dataset

# In[6]:


data.tail(5)


# # CHECK NULL VALUES 

# In[7]:


sns.heatmap(data.isnull())


# # Check for duplicate values and later drop, if any

# In[8]:


print(data.duplicated().any())


# In[9]:


data=data.drop_duplicates()


# In[10]:


print(data.duplicated().any())


# # Number of courses per subject

# In[11]:


data['subject'].value_counts()


# In[12]:


sns.countplot(data['subject'])
plt.xlabel("Subjects",fontsize=12)
plt.ylabel("Number of courses per subject",fontsize=12)
plt.xticks(rotation=65,fontsize=10)
plt.show()


# # Total number of paid and free courses

# In[13]:


data['is_paid'].value_counts()


# In[14]:


sns.countplot(data['is_paid'])
plt.ylabel("Number of free and paid courses",fontsize=12)
plt.xticks(fontsize=10)
plt.show()


# # Comparison of free and paid courses

# Which has more lectures?

# In[15]:


data.groupby(['is_paid']).mean()


# Which has more number of subscribers?

# In[16]:


data.columns


# In[17]:


sns.barplot(x='is_paid',y='num_subscribers',data=data)
plt.ylabel("Number of subscribers")


# # Levels for which udemy provide courses

# In[18]:


data.columns


# In[19]:


data['level'].value_counts()


# In[20]:


sns.countplot(data['level'])
plt.xlabel("Level",fontsize=12)
plt.ylabel("Number of courses per level",fontsize=12)
plt.xticks(rotation=65,fontsize=10)
plt.show()


# # Which level has highest number of subscribers?

# In[21]:


data.columns


# In[22]:


sns.barplot(x='level',y='num_subscribers',data=data)
plt.ylabel("Total number of subscribers")
plt.xticks(rotation=65)
plt.show()


# # Most popular course

# In[23]:


data.columns


# In[24]:


data[data['num_subscribers'].max()==data['num_subscribers']]['course_title']


# # Five most subscribed courses

# In[25]:


Top_5=data.sort_values(by='num_subscribers',ascending=False).head(5)


# In[26]:


Top_5


# In[27]:


sns.barplot(x='num_subscribers',y='course_title',data=Top_5)
plt.ylabel("Courses",fontsize=12)
plt.xlabel("Number of subscribers",fontsize=12)
plt.show()


# # Most reviewed course

# In[28]:


data.columns


# In[29]:


plt.figure(figsize=(8,4))
sns.barplot(x='subject',y='num_reviews',data=data)
plt.xlabel("Subject",fontsize=12)
plt.ylabel("Toatal number of reviews",fontsize=12)
plt.show()


# # Affect on reviews due to price

# In[30]:


plt.figure(figsize=(15,7))
sns.scatterplot(x='price',y='num_reviews',data=data)
plt.xlabel("Price",fontsize=12)
plt.ylabel("Number of reviews",fontsize=12)
plt.show()


# # Courses for analytics

# In[31]:


data.columns


# In[32]:


data[data['course_title'].str.contains('Analytics',case=False)]


# # Five most subscribed web development courses

# In[33]:


web_development=data[data['course_title'].str.contains('web development',case=False)].sort_values(by='num_subscribers',ascending=False).head(5)


# In[34]:


web_development


# In[35]:


sns.barplot(x='num_subscribers',y='course_title',data=web_development)
plt.xlabel("Number of subscribers",fontsize=12)
plt.ylabel("Courses",fontsize=12)
plt.show()


# # Number of courses posted each year

# In[36]:


data.columns


# In[37]:


data['year']=data['published_timestamp'].dt.year


# In[38]:


sns.countplot('year',data=data)
plt.xlabel('Year',fontsize=12)
plt.ylabel('Total numbers of courses',fontsize=12)
plt.show()


# # Category-wise count of subjects posted in different years

# In[39]:


data.groupby('year')['subject'].value_counts()


# In[ ]:




