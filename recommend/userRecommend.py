import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("healingfeeling-9c1bf-firebase-adminsdk-kktgb-7226f7ac89.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://healingfeeling-9c1bf-default-rtdb.firebaseio.com/'
})

dir = db.reference('score').child('노래')
dirbook = db.reference('score').child('도서')
dirwhere = db.reference('score').child('장소')

print(dir.get())


#!/usr/bin/env python
#coding: utf-8

# In[35]:

#rating; 평가
import math
import pandas as pd

    
dataset_df=pd.DataFrame(dir.get())
dataset_df.fillna("Not Seen Yet",inplace=True)
dataset_df

dataset_df2=pd.DataFrame(dirbook.get())
dataset_df2.fillna("Not Seen Yet",inplace=True)
dataset_df2

dataset_df3=pd.DataFrame(dirwhere.get())
dataset_df3.fillna("Not Seen Yet",inplace=True)
dataset_df3
# In[36]:
dataset=dir.get()
datasetbook=dirbook.get()
datasetwhere=dirwhere.get()

print(dirbook.get())
def unique_items_song(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list

def unique_items_book(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list

def unique_items_where(dataset):
    unique_items_list = []
    for person in dataset.keys():
        for items in dataset[person]:
            unique_items_list.append(items)
    s=set(unique_items_list)
    unique_items_list=list(s)
    return unique_items_list
# In[37]:


print(unique_items_song(dataset))
print(unique_items_book(datasetbook))
print(unique_items_where(datasetwhere))


# In[61]:



# custom function to create pearson correlation method from scratch
import math

def person_corelation(dataset,person1,person2):
    both_rated = {}
    for item in dataset[person1]:
        if item in dataset[person2]:
            both_rated[item] = 1

    number_of_ratings = len(both_rated)
    if number_of_ratings == 0:
        return 0

    person1_preferences_sum = sum([dataset[person1][item] for item in both_rated])
    person2_preferences_sum = sum([dataset[person2][item] for item in both_rated])

    # Sum up the squares of preferences of each user
    person1_square_preferences_sum = sum([pow(dataset[person1][item], 2) for item in both_rated])
    person2_square_preferences_sum = sum([pow(dataset[person2][item], 2) for item in both_rated])

    # Sum up the product value of both preferences for each item
    product_sum_of_both_users = sum([dataset[person1][item] * dataset[person2][item] for item in both_rated])

    # Calculate the pearson score
    numerator_value = product_sum_of_both_users - (
    person1_preferences_sum * person2_preferences_sum / number_of_ratings)
    denominator_value = math.sqrt((person1_square_preferences_sum - pow(person1_preferences_sum, 2) / number_of_ratings) * (
    person2_square_preferences_sum - pow(person2_preferences_sum, 2) / number_of_ratings))
    if denominator_value == 0:
        return 0
    else:
        r = numerator_value / denominator_value
        return r
    
def most_similar_users(dataset,target_person,no_of_users):
    
    # Used list comprehension for finding pearson similarity between users
    scores = [(person_corelation(dataset,target_person,other_person),other_person) for other_person in dataset if other_person !=target_person]
    
    #sort the scores in descending order
    scores.sort(reverse=True)
    
    #return the scores between the target person & other persons
    return scores[0:no_of_users]


tp = 'CvOap2Q2t7MTe47zBxAvBpgFBTW2'
most_similar_users(dataset,tp,len(dataset))
most_similar_users(datasetbook,tp,len(datasetbook))
most_similar_users(datasetwhere,tp,len(datasetwhere))


# In[62]:


def recommendation_phase(dataset,person):
    # Gets recommendations for a person by using a weighted average of every other user's rankings
    totals = {}  #empty dictionary
    simSums = {} # empty dictionary
    for other in dataset:
        # don't compare me to myself
        if other == person:
            continue
        sim = person_corelation(dataset,person, other)
        # ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in dataset[other]:
            # only score movies i haven't seen yet
            if item not in dataset[person]:
                # Similrity * score
                totals.setdefault(item, 0)
                totals[item] += dataset[other][item] * sim
                # sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
                # Create the normalized list

    rankings = [(total / simSums[item], item) for item, total in totals.items()]
    rankings.sort(reverse=True)
    # returns the recommended items
    recommendataions_list = [(recommend_item,score) for score, recommend_item in rankings]
    return recommendataions_list


# In[63]:


print("Enter the target person")
b=False
b2=False
b3=False

if tp in dataset.keys():
    a=recommendation_phase(dataset,tp)
    print(a)
    if a != -1:
        print(a)
        print("Recommendation Using User based Collaborative Filtering:  ")
        
        for webseries,weights in a:
            print(webseries,'——>',weights)
            if(b==False):
                title=webseries
                data=weights
            b=True
        
else:
    title="no"
    data="no"

if tp in datasetbook.keys():
        a=recommendation_phase(datasetbook,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(b2==False):
                    titlebook=webseries
                    databook=weights
                b2=True
            
else:
    titlebook="no"
    databook="no"

if tp in datasetwhere.keys():
        a=recommendation_phase(datasetwhere,tp)
        if a != -1:
            print("Recommendation Using User based Collaborative Filtering:  ")
            for webseries,weights in a:
                print(webseries,'——>',weights)
                if(b3==False):
                    titlewhere=webseries
                    datawhere=weights
                b3=True
            
else:
    titlewhere="no"
    datawhere="no"

# In[ ]:
print(title)
print(data)
print(titlebook)
print(databook)
print(titlewhere)
print(datawhere)
