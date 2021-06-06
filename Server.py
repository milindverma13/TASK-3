#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, pickle, socket, struct


# In[2]:


try:
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created ...")
except socket.error as err:
    print("Socket creation failed with error {}".formatat(err))


# In[3]:


port = 1234
skt.bind(("", port))
skt.listen()
print("Socket is listening......")


# In[ ]:


while True:
    session, address = skt.accept()
    print("Connected to : ",address)
    if session:
        cam = cv2.VideoCapture(1)
        while(cam.isOpened()):
            ret, img = cam.read()
            data = pickle.dumps(img)
            msg = struct.pack("Q", len(data))+data
            session.sendall(msg)
            cv2.imshow("Transmitting video...",img)
            if cv2.waitKey(1) == 13:
                cv2.destroyAllWindows()
                session.close()
                break
        
    


# In[ ]:





# In[ ]:




