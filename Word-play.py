import numpy as np
import json
import re
import os

os.getcwd()
os.chdir('D:\Documents\DME\Project')

with open('train.json',encoding='utf-8') as f:
    d = json.load(f)                             #Training data
    f.close()

n = len(d)

less_3_ingr = []                                #Find the columns with 2 or less ingredients
nb_ingr = np.zeros((n))
for i in range(n):
    nb_ingr[i] = len(d[i]['ingredients'])
    if( nb_ingr[i] < 3):
        less_3_ingr.append(i)
        
nb_ingr = np.delete(nb_ingr,less_3_ingr)
for i in sorted(less_3_ingr,reverse = True):    #Delete the recipes with 2 or less ingredients
    del d[i]

n = len(d)
print(nb_ingr)
   
long_list_ingr = []                             #A "long" list of all ingredients in the data set
for i in range(n):
    for j in range(int(nb_ingr[i])):
        long_list_ingr.append(d[i]['ingredients'][j])
        
long_list_ingr = [re.sub(r'\W',' ',string) for string in long_list_ingr]
        
long_words = []                                 #Split the ingredients into single words
for i in range(len(long_list_ingr)):
    split_list = long_list_ingr[i].split()
    for j in range(len(split_list)):
        long_words.append(split_list[j])

unique_words = list(set(long_words))    #Gives the unique words
print(len(unique_words))                #Number of unique words          
  
def CleanThoseWords(list_of_words):
    for i in range(len(list_of_words)):
        list_of_words[i] = list_of_words[i].lower()         #Make sure the word is in lower case
        
        list_of_words[i] = re.sub(r'\W','',list_of_words[i]) #Delete symbols

        list_of_words[i] = re.sub(r"\d", "", list_of_words[i]) #Delete numbers

        list_of_words[i] = re.sub(r'\b[a-zA-Z]\b', "", list_of_words[i]) #Delete letters standing alone

        list_of_words[i] = re.sub(r'\s+', ' ', list_of_words[i], flags = re.I) #Delete double spaces
        
    return(list_of_words)


unique_words = CleanThoseWords(unique_words)
unique_words = list(set(unique_words))
print(len(set(unique_words)))

#Here are all the words I could find to try and simplify the ingredient names 
dict_remove = ["fat", "free", "oz", "fine", "finely","superfine", "crushed", "crush", "cut", "up", "age",
               "fashioned", "press", "refined", "squeeze", "refrigerated", "smoked", "sweet", "diced", "processed",
               "nonfat", "packed", "firmly", "loosely", "gluten", "low", "high", "less", "sodium", "reduced",
               "organic", "store bought", "of", "the", "semi", "condensed", "whole", "reduced", "light", "softened"
               "ground", "fresh", "black", "natural", "flavored", "plain","unsweetened", "vegan", "nonfat"]

#All the brand names I found
Brand_names = ["Bertolli", "Crocker", "Conimex", "Colman", "Crystal Farms", "DeLallo", "Domino",
               "Doritos", "Earth Balance", "Elmlea", "Estancia", "Fisher", "Flora", "Foster Farms",
               "Gourmet Garden", "Goya", "Green Giant", "Heinz", "Hellmann", "Hidden Valley",
               "Honeysuckle White", "Imperial", "JOHNSONVILLE", "Jack Daniels", "Johnsonville",
               "Jimmy Dean", "KRAFT", "Knorr", "Lipton", "Manischewitz", "McCormick", "Mazola",
               "Old El Paso", "Pillsbury", "Progresso", "Pure Wesson", "Ragu", "San Marzano", 
               "Sargento", "Soy Vay", "Spice Islands", "TACO BELL", "Truvía", "Uncle Ben",
               "Velveeta", "Wish Bone", "Yoplait", "Zatarain", "Best Food", "Breyers",
               "Campbell", "Hidden Valley", "Knorr", "McCormick", "Mizkan", "Progresso",
               "Frank", "Red Gold"]
    
Brand_names = [Brand_names[i].lower() for i in range(len(Brand_names))] #lower case brand names

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

dict_remove = dict_remove + Brand_names + [string for string in ENGLISH_STOP_WORDS]

#Removes all the words from dict_remove
def RemoveWords(list_of_words):
    for i in range(len(list_of_words)):
        for word_remove in dict_remove:          
            list_of_words[i]  = re.sub("\\b" + word_remove + "\\b", "", list_of_words[i]) #Only match full words
    return(list_of_words)

unique_words = RemoveWords(unique_words)
unique_words = list(set(unique_words))
print(len(set(unique_words))) 

from nltk.stem import PorterStemmer   #Leximmatization
porter = PorterStemmer()
unique_words = [porter.stem(string) for string in unique_words]
unique_words = list(set(unique_words))
print(len(set(unique_words))) 

unique_words = RemoveWords(unique_words) #Rerun to check if the words of the leximmatization can be removed 
unique_words = list(set(unique_words))
print(len(set(unique_words))) 

dict_remove = [porter.stem(string) for string in dict_remove] #Leximmatize the words to remove as some are not in most basic form
unique_words = RemoveWords(unique_words) #Rerun to check if the leximmatized words can be removed 
unique_words = list(set(unique_words))
print(len(set(unique_words))) 









    
    
    
    
    
    
    