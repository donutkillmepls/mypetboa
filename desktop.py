#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 1


# In[16]:


a= [3,6,9,12,15,18]
print (a)
b=a.pop(4)
a.insert(2,b)
a.append(b)


# In[17]:


a


# In[ ]:


#question 2


# In[18]:


list_1=[1,1,2,2,3,3,4,4,5]
list_2=[54,56,54,56,55,57,58,53,52]
print (list_1)
print (list_2)
set_1=set(list_1)
set_2=set(list_2)
print (set_1)
print (set_2)
finalset=set_1.union(set_2)
finallist=list(finalset)
print(finallist)


# In[ ]:


#question 3


# In[20]:


q3=[44,76,83,57,13,13,74,62]
print(q3)
set3=set(q3)
print(set3)
tup3=tuple(set3)
print(tup3)
print(min(tup3))
print(max(tup3))


# In[ ]:


#question 4


# In[3]:


sample="my name is dog food"
print(*sample)


# In[4]:


#question 5


# In[25]:


doggy = {'physics': 80, 'math': 90, 'chemistry': 86}
print (doggy)
print(doggy['physics'])


# In[18]:





# In[ ]:





# In[ ]:




