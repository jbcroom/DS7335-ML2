#******************************************************************
# DS 7337 - Machine Learning 2
# Author: Brandon Croom
# Assignment: Homework 2
# Date: 6/3/2020
#******************************************************************

#******************************************************************
# Assignment Parameters 
#
# 1. Write a function to take a list or dictionary of clfs and hypers ie use
#   logistic regression, each with 3 different sets of hyper parameters for each
#
# 2. expand to include larger number of classifiers and hyperparameter settings
#
# 3. find some simple data
#
# 4. generate matplotlib plots that will assist in identifying the optimal clf
#   and parameters settings
# 
# 5. Please set up your code to be run and save the results to the
#   directory that its executed from
#
# 6. Investigate grid search function
#*******************************************************************

# import necessary libraries
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold 
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

#********************************************************************
# Define dictionaries and global variables for use in the program
#********************************************************************
#
# set the number of folds we want for k-folds. Start at 5
n_folds = 5

# define the initial set of models we want to compare as a dictionary.
# Because this is a dictionary we can add/remove as needed
model_dict = {
    'RandomForestClassifier': RandomForestClassifier,
    'KNeighboursClassifier': KNeighborsClassifier,
    'LogisticRegression': LogisticRegression
}

# define the optimization parameters for the models above. Selected just a few of 
# the possible parameters. Because this is a dictionary we can add/remove as needed
model_params_dict = {
    'RandomForestClassifier':{ 
            "n_estimators"      : [100, 200, 500, 1000],
            "max_features"      : ["auto", "sqrt", "log2"],
            "bootstrap": [True],
            "criterion": ['gini', 'entropy'],
            "oob_score": [True, False]
            },
    'KNeighboursClassifier': {
        'n_neighbors': np.arange(3, 15),
        'weights': ['uniform', 'distance'],
        'algorithm': ['ball_tree', 'kd_tree', 'brute']
        },
    'LogisticRegression': {
        'solver': ['newton-cg', 'sag', 'lbfgs'],
        'multi_class': ['ovr', 'multinomial']
        }  
}

#**********************************************************************************
# Define methods for use in the script
# *********************************************************************************
#
# METHOD NAME: run
# METHOD DESC: This method processes a dictionary of clfs with optional hyperparameters againsts a 
#              provided set of data. The functions returns a dictionary containing the clf name, 
#              results of the train/test split and the accuracy score of the clf execution
# INPUTS:
#   - a_clf - a dictionary containing a listing of clfs for execution
#   - data - a tuple containing the data, target variable and number of folds to be executed
#   - clf_hyper - optional parameter, a dictionary containing the hyperparameter combinations to be
#                 used in the clf
# OUTPUTS:
#   - no return value
#   - will output matplotlib plots to the directory where the script is executed
#
# NOTE: Code below has been provided as part of the homework assignment

def run(a_clf, data, clf_hyper={}):
  M, L, n_folds = data 
  kf = KFold(n_splits=n_folds) 
  ret = {} 

  for ids, (train_index, test_index) in enumerate(kf.split(M, L)): 
    clf = a_clf(**clf_hyper) 
    clf.fit(M[train_index], L[train_index])
    pred = clf.predict(M[test_index]) 
    ret[ids]= {'clf': clf,                   
               'train_index': train_index,
               'test_index': test_index,
               'accuracy': accuracy_score(L[test_index], pred)}

  return ret

# METHOD NAME: plot_parameters
# METHOD DESC: This method processes a dictionary  containing a listing of clfs, hyperparameters and
#              output results. The method configures matplotlib to plot the results and then both
#              displays the plots and saves the plots to the current directory where the script is
#              executing
# INPUTS:
#   - clfsAccuracyDict - the dictionary containing a listing of clfs, hyperparameters and
#                        output results for plotting
#   - filename - optional parameter, provided to allow custom filenames for saving
# OUTPUTS:
#   - no return value
#   - will output matplotlib plots to the directory where the script is executed
#
# NOTE: Code below was from office hours with D. Stroud. All comments from the code left intact
#       Code has been moved to a method to make the overall code base readable.

def plot_parameters(clfsAccuracyDict,filename='clf_Histograms_'):
    # for naming the plots
    filename_prefix = filename

    # initialize the plot_num counter for incrementing in the loop below
    plot_num = 1

    # Adjust matplotlib subplots for easy terminal window viewing
    left  = 0.125  # the left side of the subplots of the figure
    right = 0.9    # the right side of the subplots of the figure
    bottom = 0.1   # the bottom of the subplots of the figure
    top = 0.6      # the top of the subplots of the figure
    wspace = 0.2   # the amount of width reserved for space between subplots,
                   # expressed as a fraction of the average axis width
    hspace = 0.2   # the amount of height reserved for space between subplots,
                   # expressed as a fraction of the average axis height
                   
    # for determining maximum frequency (# of kfolds) for histogram y-axis
    n = max(len(v1) for k1, v1 in clfsAccuracyDict.items())

    #create the histograms
    #matplotlib is used to create the histograms: https://matplotlib.org/index.html
    for k1, v1 in clfsAccuracyDict.items():
        # for each key in our clfsAccuracyDict, create a new histogram with a given key's values
        fig = plt.figure(figsize =(10,10)) # This dictates the size of our histograms
        ax  = fig.add_subplot(1, 1, 1) # As the ax subplot numbers increase here, the plot gets smaller
        plt.hist(v1, facecolor='green', alpha=0.75) # create the histogram with the values
        ax.set_title(k1, fontsize=25) # increase title fontsize for readability
        ax.set_xlabel('Classifer Accuracy (By K-Fold)', fontsize=25) # increase x-axis label fontsize for readability
        ax.set_ylabel('Frequency', fontsize=25) # increase y-axis label fontsize for readability
        ax.xaxis.set_ticks(np.arange(0, 1.1, 0.1)) # The accuracy can only be from 0 to 1 (e.g. 0 or 100%)
        ax.yaxis.set_ticks(np.arange(0, n+1, 1)) # n represents the number of k-folds
        ax.xaxis.set_tick_params(labelsize=20) # increase x-axis tick fontsize for readability
        ax.yaxis.set_tick_params(labelsize=20) # increase y-axis tick fontsize for readability
        #ax.grid(True) # you can turn this on for a grid, but I think it looks messy here.

        # pass in subplot adjustments from above.
        plt.subplots_adjust(left=left, right=right, bottom=bottom, top=top, wspace=wspace, hspace=hspace)
        plot_num_str = str(plot_num) #convert plot number to string
        filename = filename_prefix + plot_num_str # concatenate the filename prefix and the plot_num_str
        plt.savefig(filename, bbox_inches = 'tight') # save the plot to the user's working directory
        plot_num = plot_num+1 # increment the plot_num counter by 1
    plt.show()
    
# METHOD NAME: groupClassifiers
# METHOD DESC: This method processes a dictionary containing the output results of the run function. 
#              The method will iterate through the dictionary to find the combination with the highest
#              accuracy score. The combination of the highest accuracy score will be returned as a 
#              dictionary as output
# INPUTS:
#   - results_dict - the dictionary containing a listing of clfs, hyperparameters and output results
# OUTPUTS:
#   - returns a dictionary containing the best permutation of results for plotting
#
# NOTE: Code below was from office hours with D. Stroud. All comments from the code left intact
#       Code has been moved to a method to make the overall code base readable. 

def groupClassifiers(results_dict):
    clfsAccuracyDict = {}
    
    for key in results_dict:
        k1 = results_dict[key]['clf']
        v1 = results_dict[key]['accuracy']
        k1Test = str(k1) #Since we have a number of k-folds for each classifier...
                         #We want to prevent unique k1 values due to different "key" values
                         #when we actually have the same classifer and hyper parameter settings.
                         #So, we convert to a string

        #String formatting
        k1Test = k1Test.replace('            ',' ') # remove large spaces from string
        k1Test = k1Test.replace('          ',' ')

        #Then check if the string value 'k1Test' exists as a key in the dictionary
        if k1Test in clfsAccuracyDict:
            clfsAccuracyDict[k1Test].append(v1) #append the values to create an array (techically a list) of values
        else:
            clfsAccuracyDict[k1Test] = [v1] #create a new key (k1Test) in clfsAccuracyDict with a new value, (v1)

    return(clfsAccuracyDict)

# METHOD NAME: hyper_search
# METHOD DESC: This method processes dictionaries of clfs and hyperparamters against a data set
#              The method will then determine the best clf/hyperparameter combination and output
#              matplot lib plots to show confirmation.
# INPUTS:
#   - model_dict - the dictionary containing a listing of clfs 
#   - param_dict - the dictionary containing the parameters for the clfs
#   - data - the packed data containing the number of folds
#   - filename - optional parameter, used for naming the plot outputs
# OUTPUTS:
#   - no returned values
#   - will output into running directory matplotlib plots of best clf/hyper permutations
#
def hyper_search(model_dict, param_dict, data, filename=''):
    # define empty dictionaries to start
    np_results = {}
    accuracyDics = {}
    
    # iterate through the model dictionary to execute each model
    for key, value in model_dict.items():
        # just for grins, let the user know which model we're processing
        print('Processing Model: ', key)
        
        # get the hyper parameter dictionary listings for the specific model
        paramDict = param_dict[key]
        
        # take our hyper parameter dictionary and use itertools to build out
        # all possible permutations for execution
        keys1, values1 = zip(*paramDict.items())
        paramList = [dict(zip(keys1, v)) for v in itertools.product(*values1)]
        
        # iterate through the hyper parameter permutations and execute them
        for dic in paramList:
            # execute the run function on each model type and hyper parameter configuration
            # add the results to the np_results dictionary for use in other methods
            np_results.update(run(value, data, dic))
           # results = run(value, data, dic)
            
        # find the classifiers for plotting from all the permutations we've run through
        # this will get us to the "best" permutation of results to plot and prevent us
        # from printing 100's of plots
        accuracyDics.update(groupClassifiers(np_results))


    #plot the parameters
    plot_parameters(accuracyDics,filename)

#*****************************************************************************************
# Begin execution of code testing and development with multiple iterations of the 
# executions for sanity checks
#*****************************************************************************************

# Load the necessary data set. For this example let's use the breast cancer data set
cancer_data, cancer_target = datasets.load_breast_cancer(return_X_y=True)

# build out the data set to pass to run
data = (cancer_data, cancer_target,n_folds)

#*****************************************************************************************
# START - execute the final hyper_search code to take the parameters and data and output the 
#         histograms
#****************************************************************************************
hyper_search(model_dict, model_params_dict, data, "BCroom_clf_Histograms_")

#*****************************************************************************************
# END - full run of modified code using hyper parameters
#****************************************************************************************

# NOTE: The sections of commented code below are my sanity checks that the final function
#       was able to be built the way I wanted it to be. I'm going to leave these sections
#       in here just for purposes to show my though process.     

#*****************************************************************************************
# START - Initial run of the methods above with single clf and no hyper parameters to verify logic
#*****************************************************************************************
# results = run(RandomForestClassifier, data, clf_hyper={})

# # find the classifiers for plotting
# accuracyDics = groupClassifiers(results)

# # plot the parameters
# plot_parameters(accuracyDics,"BCroom_T1_clf_Histograms_")
#*****************************************************************************************
# END - Initial run of the methods above with single clf and no hyper parameters to verify logic
#*****************************************************************************************


#*****************************************************************************************
# START - run code with multiple classifiers, still no hyper parameters
#*****************************************************************************************
# run this code in "cheat mode" by just looping throught the models we defined above
# for crlfs in models.values():
#     # execute the run function on each model type
#     results = run(crlfs, data, clf_hyper={})

#     # find the classifiers for plotting
#     accuracyDics = groupClassifiers(results)

#     # plot the parameters
#     plot_parameters(accuracyDics,"BCroom_T2_clf_Histograms_")

#*****************************************************************************************
# END - run code with multiple classifiers, still no hyper parameters
#*****************************************************************************************

