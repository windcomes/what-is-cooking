import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

with open('train.json', encoding='utf-8') as f:
    d = json.load(f)
    f.close()

full_data = pd.DataFrame(d)
full_data = full_data.drop(['id'],axis=1)



#x_train_full, y_train_full = data_process(train_data)
'''x_train, x_val, y_train, y_val = train_test_split(x_train_full, y_train_full, test_size=0.3, random_state=1)
x_val, x_test, y_val, y_test = train_test_split(x_val,y_val,test_size=0.33,random_state=1)'''
print(full_data[])