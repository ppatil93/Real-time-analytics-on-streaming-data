#!/usr/bin/env python
# coding: utf-8

# In[49]:


#!/usr/bin/env python
from kafka import KafkaProducer
import json,requests


# In[50]:


# Creating Kafka Producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(0,10,1))


# In[51]:


producer.send('meetup',b'Hello, Kafka right now')


# In[85]:


#Getting HTTP rsvp data requests from meetup.com
r = requests.get("https://stream.meetup.com/2/rsvps",stream=True)


# In[86]:


#Looping through the stream of data and sending these data to consumers
for line in r.iter_lines():
#Send each record in bytes. Kafka reads in bytes
    producer.send('meetup',line)
# json.loads convert bytes into object. json.dumps convert to object (dictionary form key value pair) string. Create
#object for grouping city in Group --> Group_city
    obj = json.loads(line.decode('utf-8'))
    print (obj['group']['group_city'])
  #  obj = json.dumps(line.decode('utf-8'))
#    producer.send('meetup',obj)

#     print (line)
#    obj = json.dumps(line.encode('utf-8'))
#    rsvps = (obj['group']['group_city'])
#    print (rsvps)


# In[87]:


producer.close()


# In[ ]:





# In[ ]:




