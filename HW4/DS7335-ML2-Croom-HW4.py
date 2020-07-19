#******************************************************************
# DS 7337 - Machine Learning 2
# Author: Brandon Croom
# Assignment: Homework 4
# Date: 7/1/2020
#******************************************************************

#******************************************************************
# Assignment Parameters
#
# Decision Making With Matrices
# This is a pretty simple assignment.  You will do something you do everyday, but today it will be with matrix manipulations. 
# The problem is: you and your work friends are trying to decide where to go for lunch. You have to pick a restaurant that’s best for everyone.  Then you should decided if you should split into two groups so everyone is happier.  
# Despite the simplicity of the process you will need to make decisions regarding how to process the data. 
# This process was thoroughly investigated in the operation research community.  This approach can prove helpful on any number of decision making problems that are currently not leveraging machine learning.  
# You asked your 10 work friends to answer a survey. They gave you back the following dictionary object.  
# people = {'Jane': {'willingness to travel':
#                  'desire for new experience':
#                  'cost':
#                  'indian food':
#                  'mexican food':
#                  'hipster points':
#                  'vegetarian': }
#                }          
# Transform the user data into a matrix(M_people). Keep track of column and row ids.   
#
# Next you collected data from an internet website. You got the following information.
#restaurants  = {'flacos':{'distance' : 
#                        'novelty' :
#                        'cost': 
#                        'average rating': 
#                        'cuisine':
#                        'vegetarians':}}
#
# Transform the restaurant data into a matrix(M_resturants) use the same column index.
#
# The most important idea in this project is the idea of a linear combination.  
# Informally describe what a linear combination is  and how it will relate to our restaurant matrix.
#
# Choose a person and compute(using a linear combination) the top restaurant for them.  What does each entry in the resulting vector represent? 
#
# Next, compute a new matrix (M_usr_x_rest  i.e. an user by restaurant) from all people.  What does the a_ij matrix represent? 
#
# Sum all columns in M_usr_x_rest to get the optimal restaurant for all users.  What do the entries represent?
#
# Now convert each row in the M_usr_x_rest into a ranking for each user and call it M_usr_x_rest_rank.   Do the same as above to generate the optimal restaurant choice.  
#
# Why is there a difference between the two?  What problem arrives?  What does it represent in the real world?
#
# How should you preprocess your data to remove this problem. 
#
# Find  user profiles that are problematic, explain why?
#
# Think of two metrics to compute the disatistifaction with the group.  
#
# Should you split in two groups today? 
#
# Ok. Now you just found out the boss is paying for the meal. How should you adjust? Now what is the best restaurant?
#
# Tomorrow you visit another team. You have the same restaurants and they told you their optimal ordering for restaurants.  Can you find their weight matrix?

# Import necessary libraries
import numpy as np
from scipy.stats import rankdata


# define dictionaries for people and restaurants
# for the people listing we'll rank based on a score of 1 - 5. With 5 being the "best"
people = {'Jane': {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Steve' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Bob' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Joe' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Amy' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Aidan' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 5 },
          'Daniel' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'John' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Matt' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 },
          'Pat' : {'willingness to travel': 1,
                  'desire for new experience': 3,
                  'cost': 3,
                  'indian food': 3,
                  'mexican food': 3,
                  'hipster points': 3,
                  'vegetarian': 1 }
          
                }    

#for the restaurant listing we'll rank based on a score of 1 - 5. With 5 being the "best"
restaurants  = {'chilis':{'distance' : 1, 
                        'novelty' : 1,
                        'cost': 2,
                        'average rating': 3, 
                        'cuisine': 3,
                        'vegetarians': 1},
                'mooneys':{'distance' : 3,
                        'novelty' : 2,
                        'cost': 3,
                        'average rating': 4, 
                        'cuisine': 4,
                        'vegetarians': 4},
                'applebees':{'distance' : 1, 
                        'novelty' : 1,
                        'cost': 3,
                        'average rating': 3, 
                        'cuisine': 3,
                        'vegetarians': 2},
                'xcaret':{'distance' : 5, 
                        'novelty' : 4,
                        'cost': 5,
                        'average rating': 5, 
                        'cuisine': 5,
                        'vegetarians':3},
                'olivegarden':{'distance' : 5, 
                        'novelty' : 1,
                        'cost': 3,
                        'average rating': 2, 
                        'cuisine': 3,
                        'vegetarians':3},
                'texasroadhouse':{'distance' : 3, 
                        'novelty' : 2,
                        'cost': 3,
                        'average rating': 4, 
                        'cuisine': 3,
                        'vegetarians':1},            
                }

# Define helper function
def get_restaurant_name(idxVal):
        key_list = list(restaurants.keys()) 
        
        return key_list[idxVal]

def get_user_name(idxVal):
        key_list = list(people.keys()) 
        
        return key_list[idxVal]

# Convert our dictionaries to their respective matrices:
# M_people for the people dictionary
# M_restaurants for the restaurant dictionary
# 
# Make sure we order items so they match. We'll assume hipster points and ratings are the same
M_people = np.array([[v[j] for j in ['willingness to travel', 'desire for new experience', 'cost', 'indian food','mexican food','hipster points','vegetarian']] for k, v in people.items()])

M_restaurant = np.array([[v[j] for j in ['distance', 'novelty', 'cost', 'cuisine','average rating','vegetarians']] for k, v in restaurants.items()])

# Define a Linear Combination and how it relates to restaurant ranking
# A linear combination is the expression constructed from multiplying terms by a constant and then adding those terms
# together to obtain a result. In our restaurant ranking we use linear combinations to map user preferences to restaurant
# criteria and determine which restaurant is optimal based on the given solution.

M_people2 = np.empty((10,6))

# Let's collapse the cuisine fields in the people matrix. We'll average the recommendation for mexican
# and Indian into a single value. This will get our matrices in the correct shape.
iter = 0
for item in M_people:
        indian = item[3]
        mexican = item[4]
        item[3] = (indian + mexican) /2
        newarray = np.array([item[0],item[1],item[2],item[3],item[5],item[6]])
        M_people2[iter] = newarray
        iter +=1

M_people = np.copy(M_people2)

# Let's look at the ranking that Steve will have
usr_Steve = M_people[1]

# Using the rankdata with the length of the array and the dot product will get us an array
# with the ranking of the restaurants
rank_Steve = rankdata(len(usr_Steve)-rankdata(np.dot(M_restaurant,usr_Steve)))

# Based on the current dataset we see that Steve wants to go to Texas Roadhouse
print("Steve's ranks are: ", rank_Steve)
print("Steve wants to go to: ", get_restaurant_name(int(rank_Steve[0])-1))

# Now we'll calculate a value for all individuals and all restaurants. This matrix
# M_usr_x_rest represents the total values each individual place on each restaurant
M_usr_x_rest = np.dot(M_restaurant,M_people.T).T

# Sum up the entries for the usr_x_rest. This represents the total value each restaurant based
# on each users inputs
M_usr_x_rest.sum(axis=0)

# Generate a ranking of the restaurants
M_usr_x_rest_rank = rankdata(len(M_usr_x_rest)-rankdata(M_usr_x_rest))

# The difference between the single user ranking and the multi-user ranking is that with the single
# user ranking there is a definitive outcome of ranks. With the multi-user ranking we have ranks that 
# are the same for multiple users and this cannot come to a concrete decision. In the real world this
# would result in locked choices or customer dissatisfaction with choices. A decision couldn't be made.

# We can overcome this issue by just looking at the sums of the full listing to obtain the best 
# choice restaurant
rank_best = rankdata(len(M_usr_x_rest.sum(axis=0))-rankdata(M_usr_x_rest.sum(axis=0)))

# Based on this ranking this way the group wants to go to Texas Roadhouse
print("Group ranks are: ", rank_best)
print("The group wants to go to: ", get_restaurant_name(int(rank_best[0])-1))

# We can preprocess our data looking at common factors that could make the rankings the same or look at
# adding a weighting to our ranking to try to minimize the ties in the ranking. In this specific
# case of choosing a restaurant we could also factor in human interaction to make a determination on 
# how to handle any ties. 

# The problematic users are:
iter = 0
for item in M_people:
      tmp_rank = rankdata(len(item)-rankdata(np.dot(M_restaurant,item))) 
      print(get_user_name(iter), ' ranking: ', tmp_rank)
      iter += 1
      
# From the ranking above we see that the ranks are the same for all users for the first four 
# restaurants. For the later restaurants two individuals have differences in how to rank. This is
# due to the ranking differences in their individual preferences which places different restaurants
# at different levels

# Based on the information currently seen it seems the rankings are all similar and thus for this
# instance we would not break the group up into two groups.

# To evaluate group dissatisfaction we could capture thoughts on the ranking results to see if the 
# individuals were satisfied or not with the ranking output. This would be similar to a customer
# satisfaction ranking. Another metric we could use would be a physical tracking mechanism to see who
# actually went and ate at the restaurant. We could infer that those that didn't go were dissatisfied
# with the result and simply refused to go.

# If the boss is paying for the meal, we more than likely would put more weight on a higher cost
# restaurant and possibly one that is further way from the office (to make for a longer lunch).
# We could just rank based on those two items:
boss_list = np.empty((10,6))

iter = 0
for item in M_people:
        indian = item[3]
        mexican = item[4]
        item[3] = (indian + mexican) /2
        newarray = np.array([item[0],0,item[2],0,0,0])
        boss_list[iter] = newarray
        iter +=1

M_boss_x_rest = np.dot(M_restaurant,boss_list.T).T

rank_best_boss = rankdata(len(M_boss_x_rest.sum(axis=0))-rankdata(M_boss_x_rest.sum(axis=0)))

# Print our the bosses rankings and where we're going
print("Boss ranks are: ", rank_best_boss)
print("The the boss is taking us to: ", get_restaurant_name(int(rank_best_boss[0])-1))

# If we go with another team and are given their restaurant preferences we should be able to get
# back to their rankings. We would decompose the ranking matrix back to the restaurant sum matrix and 
# and then use the transpose of the restaurant matrix to get to the user ranking listing. 
      
