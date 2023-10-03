#!/usr/bin/env python
# coding: utf-8

# ## UDEMY COURSES DATA ANALYSIS (REAL WORLD DATA)
# PREPARED BY: ISHAN NAUTIYAL \
# DATE: 08/09/2023 \
# DATASET : KAGGLE 

# In[3]:


# Lets import the libraries 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:



data= pd.read_csv("C:\\Users\\ishan\\datasets\\udemy_courses.csv",parse_dates=['published_timestamp'])


# In[5]:


df1= pd.DataFrame(data)


# In[29]:


df1.head()


# In[6]:


df1.columns


# In[7]:


df1.dtypes


# In[35]:


df1.columns


# In[ ]:





# In[38]:


sns.countplot(x)


# In[42]:


df1.dtypes


# In[8]:


df1.isnull().sum()


# In[9]:





# In[12]:


dup


# In[20]:


df1= df1.drop_duplicates()


# In[13]:


df1.columns


# In[14]:


df1['subject'].value_counts()


# In[18]:


# lets visualize it 
sns.countplot(df1['subject'])# barplot of seaborn
plt.xlabel('subjects',fontsize= 13)# label the axis and font size
plt.ylabel('no of courses ', fontsize = 13)
plt.xticks(rotation = 65) # rotate the title for better view 
plt.show() # remove the extra strings 


# In[21]:


dup


# In[22]:


df1.columns


# In[24]:


df1['is_paid'].value_counts()


# In[26]:


sns.countplot(df1['is_paid'])
plt.xlabel('free or paid ')
plt.ylabel('no of courses')
plt.show()


# In[27]:


df1.columns


# In[29]:


df1['level'].value_counts()


# In[30]:


sns.countplot(df1['level'])
plt.xlabel('levels',fontsize = 12)
plt.ylabel('no of courses', fontsize= 12)
plt.xticks(rotation= 80)
plt.show()


# In[31]:


df1.columns


# In[36]:


sns.barplot(x= 'is_paid', y= 'num_subscribers', data = df1)
plt.xlabel('course type')


# In[37]:


df1.columns


# In[39]:


sns.barplot(x= 'level', y= 'num_subscribers', data= df1)
plt.xlabel('level of course')
plt.ylabel('number bof users ')
plt.xticks(rotation= 75)
plt.show()


# In[49]:


df1[df1['num_subscribers'].max()==df1['num_subscribers']]['course_title']


# In[56]:


top_10=df1.sort_values(by='num_subscribers', ascending = False ).head(10)


# In[57]:


sns.barplot(x= 'num_subscribers', y= 'course_title', data= top_10)


# In[58]:


df1.columns


# In[60]:


df1.sort_values(by= 'num_reviews', ascending = False).head(10)[['course_title','num_reviews']]


# In[61]:


top_rev= df1.sort_values(by= 'num_reviews', ascending = False).head(10)


# In[62]:


sns.barplot(x= 'num_reviews', y= 'course_title', data= top_rev)


# In[63]:


# does price affect the number of revies 
df1.columns


# In[66]:


plt.figure(figsize=(15,3))
sns.scatterplot(x= 'price', y= 'num_reviews', data = df1)


# In[67]:


# total number of courses related to subject python 
df1.columns


# In[70]:


len(df1[df1['course_title'].str.contains('python', case = False)])


# In[72]:


top_python =  df1[df1['course_title'].str.contains('python', case = False)]


# In[74]:


top_10_py=top_python.sort_values(by = 'num_subscribers',ascending = False).head(10)


# In[76]:


# visualize it 
sns.barplot(x= 'num_subscribers',y= 'course_title', data = top_10_py)


# In[77]:


df1.columns


# In[79]:


df1['Year']=df1['published_timestamp'].dt.year


# In[80]:


df1.head()


# In[82]:


sns.countplot('Year', data = df1)


# In[83]:


df1.groupby('Year')['subject'].value_counts()

