#!/usr/bin/env python
# coding: utf-8

# In[ ]:


introduction to list Data type


# In[ ]:


Def: A list is a collection of items declared in a particular order
    classification:mutable


# In[1]:


students =  ['imran','imtiaz','azhar','arsha','ayesha']


# In[2]:


print(students)


# In[3]:


type(students)


# In[ ]:


1.how to access the above elements in the list


# In[ ]:


req# i want to access imtiaz from the list


# In[ ]:


introduction to indexing:0,1,2,3....


# In[4]:


print(students[1])


# In[ ]:


req# i want to access ayesha from the list


# In[5]:


print(students[4])


# In[ ]:


1.how to add new elements to the list
2.how to modify the elements in the list
3.how to delete  elements from the list


# In[6]:


print(students)


# In[ ]:


req# i want to add simrah to the list


# In[8]:


students.insert(1,'simrah')


# In[9]:


print(students)


# In[ ]:


Difference between append and insert--INTERVIEW Q


# In[10]:


print(students)


# In[ ]:


req# i want to modify imran to nikhath to the list


# In[12]:


print(students[0])


# In[13]:


students[0]='nikhath'


# In[14]:


print(students)


# In[ ]:


req# i want to delete imtiaz from the list


# In[15]:


del students[2]


# In[16]:


print(students)


# In[ ]:


Temp deletion


# In[ ]:


pop: it is used to delete the elemewnts temp---it will be  carbon copy of the deleted items and stores in a variable 
    assigned to it
pop: by default will be deleting the last element in the list


# In[17]:


print(students)


# In[18]:


x = students.pop()


# In[19]:


print(students)


# In[20]:


print(x)


# In[ ]:




