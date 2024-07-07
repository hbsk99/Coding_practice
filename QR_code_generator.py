#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pyqrcode
import png
data = "https://www.linkedin.com/in/hrishikesh-bharadwaj-s-k-67b345167/"
url = pyqrcode.create(data)
url.png('Downloads/hbsk.png', scale = 6)

