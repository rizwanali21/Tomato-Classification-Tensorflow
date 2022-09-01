import os
import numpy as np
import shutil
import random

allFileNames = os.listdir('C:/Users/iTTaste/data/Tomato 4')
#np.random.shuffle(allFileNames)
train_t1, test_t1 = np.split(np.array(allFileNames),
                                                          [int(len(allFileNames)* (1 - 0.20))])


'''train_FileNames = [src+'/'+ name for name in train_FileNames.tolist()]
tn.append(train_FileNames)
test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]
tt.append(test_FileNames)'''

print("*****************************")
print('Total images: ', len(allFileNames))
print('Training: ', len(train_t1))
print('Testing: ', len(test_t1))
print("*****************************")


'''lab = ['Tomato 1', 'Tomato 2', 'Tomato 3', 'Tomato 4']'''
'''for j in range(0,len(tn)):'''
for name in train_t1:
    #for i in lab:
    shutil.copy('C:/Users/iTTaste/data/Tomato 4/'+name, 'C:/Users/iTTaste/data/train/Tomato 4')

#for j in range(0,len(tt)):
for name in test_t1:
    #for i in lab:
    shutil.copy('C:/Users/iTTaste/data/Tomato 4/'+name, 'C:/Users/iTTaste/data/test/Tomato 4')
print("Copying Done!")
