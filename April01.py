import json
import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
with open('train.json', encoding='utf-8') as f:
    d = json.load(f)
    f.close()

data_all = pd.DataFrame(d)
# From the file Quentin offered, we can see that if we reorder the ingredient names by its first charactor, it is 
# noted that there are some special numbers(like '1','10','15') or unit names('oz') which are meaningless.
# Hence, the first thing is to remove these from the datasets.

def datasets_cleaning(df,ingredient_column):
    num_recipe = len(df)
    for recipe_no in range(num_recipe):
        for ingre_no in range(len(df.iloc[recipe_no,2])):
            df.iloc[recipe_no,2][ingre_no]=df.iloc[recipe_no,2][ingre_no].replace(r"\\d.*\\d\s", "") # delete the string like 10 1/2 100 14.5
            df.iloc[recipe_no,2][ingre_no]=df.iloc[recipe_no,2][ingre_no].replace(r"\\d.*%\s","") # delete 2% 50%
            df.iloc[recipe_no,2][ingre_no]=df.iloc[recipe_no,2][ingre_no].replace(r"oz\.","")  # delete oz.
            df.iloc[recipe_no,2][ingre_no]=df.iloc[recipe_no,2][ingre_no].replace(r"^7\sUp","7up") # replace 7 Up by 7up, make it look like a word.
    return df

data_all = datasets_cleaning(data_all,"ingredients")
y_all = data_all['cuisine'].tolist()
X_all = data_all['ingredients'].tolist()

Xtrain, Xtestval, ytrain, ytestval = train_test_split(X_all,y_all, test_size = 0.2, random_state = 42)
Xtest, Xval, ytest, yval = train_test_split(Xtestval, ytestval, test_size = 0.5, random_state = 42)

data_train = pd.DataFrame(columns=['cuisine','ingredients'])
data_train['cuisine'] = ytrain
data_train['ingredients'] = Xtrain # Creat a DataFrame based on train data(size: 31819*2)