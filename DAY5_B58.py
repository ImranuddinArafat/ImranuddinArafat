#!/usr/bin/env python
# coding: utf-8

# In[ ]:


organising the list data type


# In[1]:


cars = ['indica','bmw','benz','cadillac','gm','kia']


# In[2]:


print(cars)


# In[ ]:


# i want to display the list in alphabetical order


# In[ ]:


1.temp  approach---changes are applied temp-----sorted
2.permanent approach----changes are applied permanent---sort


# In[3]:


print(sorted(cars))


# In[4]:


print(cars)  # it is giving me  the original order


# In[5]:


cars.sort() # the changes are applied permanently


# In[6]:


print(cars)


# In[7]:


print(cars)


# In[ ]:


interview: what is the diff btw sorted and sort method in a list  datatype? can you  pls explain


# In[9]:


print(cars)


# In[ ]:


# req: i want to  print the list in reverse order


# In[10]:


cars.reverse()


# In[11]:


print(cars)


# In[ ]:


# req: i want to  count the number of elements in the list 


# In[14]:


len(cars)


# In[ ]:


introduction to  slicing:


# In[15]:


students = ['imran','imtiaz','azhar','arsalaan','arafat','ehan']


# In[16]:


print(students)


# In[17]:


type(students)


# In[ ]:


general syntax of slicing


# In[ ]:


list[startvalue:stopvalue:stepcount]
note: stop value is always exclusive, to include  the stop value have to increase the index by +1


# In[19]:


print(students[0:1])


# In[20]:


print(students[0:2])


# In[ ]:


req2 azhar and arsalaan


# In[22]:


print(students[2:4])


# In[ ]:


req3 arafat and ehan


# In[24]:


print(students[4:6])


# In[25]:


print(students)


# In[26]:


print(students[0:5:2])


# In[27]:


print(students[0:5:1])


# In[28]:


print(students[0:5:3])


# In[29]:


print(students[0:5:4])


# In[30]:


print(students[0:5:5])


# In[32]:


print(students)


# In[ ]:




