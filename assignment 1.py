#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# # Q3

# In[ ]:





# In[ ]:





# # Q4

# In[ ]:





# In[ ]:





# # Q5

# In[ ]:





# In[ ]:





# # Q6

# In[ ]:





# In[ ]:





# # Q7

# In[56]:


import pandas as pd
import numpy as np
import seaborn as sn


# In[4]:


a=pd.read_csv("Q7.csv")


# In[5]:


a


# ### Mean

# In[29]:


a.groupby('Points')[['Score','Weigh']].mean()


# In[32]:


a.describe()


# ### Median

# In[33]:


from scipy import stats
import statistics as sc


# In[35]:


sc.median(a.Points)


# In[36]:


sc.median(a.Score)


# In[37]:


sc.median(a.Weigh)


# ### Mode

# In[46]:


a.value_counts()


# ### standard deviation

# In[48]:


b=a.std()
b


# ### variance

# In[50]:


b**2


# ### range

# In[52]:


a.min()


# In[53]:


a.max()


# In[ ]:





# In[ ]:





# # Q9,a

# In[62]:


c=pd.read_csv("Q9_a.csv")


# In[55]:


c.skew()


# In[ ]:


'''index and dist are having positive skew values where as speed is having negavive skew value'''


# In[61]:


c.kurt()


# In[ ]:


'''index and speed are having negative kurtosis, where dist is positive kurtosis'''


# In[58]:


sn.distplot(c["Index"])


# In[59]:


sn.distplot(c["dist"])


# In[60]:


sn.distplot(c["speed"])


# ### b

# In[63]:


d=pd.read_csv("Q9_b.csv")


# In[64]:


d.skew()


# In[88]:


'''SP is positive skew value where as WT is having negavive skew value'''


# In[65]:


d.kurt()


# In[66]:


'''SP and WT are having positive kurtosis'''


# In[67]:


sn.distplot(d["SP"])


# In[68]:


sn.distplot(d["WT"])


# In[ ]:





# # Q10

# In[ ]:





# In[ ]:





# # Q11

# In[ ]:





# In[ ]:





# # Q12

# In[73]:


e=[34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]


# In[ ]:


xp=np.array(e)
xp


# In[78]:


xp.mean()  #mean#


# In[84]:


sc.median(e) #median#


# In[87]:


xp.std() #standard deviation#


# In[89]:


xp.std()**2 #variance#


# In[ ]:





# # Q13

# In[98]:


#when mean and median are equal the graph will be symetric, is called non skewed data or symetric data


# In[ ]:





# # Q14

# In[ ]:


#when mean > median it is positive skewness


# In[ ]:





# # Q15

# In[ ]:


#when median > mean it is negative skewness


# In[ ]:





# # Q16

# In[104]:


''''the positive kurtosis is also know as thinner tail or wider peak kurtosis because its data is widely spread and not a sharp peak'''


# In[ ]:





# # Q17

# In[106]:


''''the negative kurtosis is also know as heavy tail kurtosis because its data is not much spreaded and has a high peak'''


# In[ ]:





# # Q18

# In[ ]:


#the data is non symetrically distributed
#this is a negative skewed data
#the IQR lies between 10 and 18, which is betweed 1st quaratile and 3rd quaratile


# In[ ]:





# # Q19

# In[ ]:


#the two boxplots are having different data ranges, the 1st boxplot IQR ranges from 250 to 275. 
#Whereas 2nd boxplot IQR ranges from 225 to 300. 


# In[ ]:





# # Q20

# In[ ]:





# In[ ]:





# # Q21

# In[ ]:





# In[ ]:





# # Q22

# In[ ]:





# In[ ]:





# # Q23

# In[ ]:





# In[ ]:





# # Q24

# In[ ]:





# In[ ]:




