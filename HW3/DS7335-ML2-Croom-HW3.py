#******************************************************************
# DS 7337 - Machine Learning 2
# Author: Brandon Croom
# Assignment: Homework 3
# Date: 7/1/2020
#******************************************************************

#******************************************************************
# Assignment Parameters 
#
# A medical claim is denoted by a claim number ('Claim.Number'). Each claim consists
# of one or more medical lines denoted by a claim line number ('Claim.Line.Number').
#
# 1. J-codes are procedure codes that start with the letter 'J'.
#      A. Find the number of claim lines that have J-codes.
#      B. How much was paid for J-codes to providers for 'in network' claims?
#      C. What are the top five J-codes based on the payment to providers?
#
# 2. For the following exercises, determine the number of providers that were paid
# for at least one J-code. Use the J-code claims for these providers to complete the following exercises.
#
#     A. Create a scatter plot that displays the number of unpaid claims (lines
#     where the ‘Provider.Payment.Amount’ field is equal to zero) for each provider versus the number of paid claim
#     B. What insights can you suggest from the graph?
#     C. Based on the graph, is the behavior of any of the providers concerning? Explain.
#
# 3. Consider all claim lines with a J-code.
#      A. What percentage of J-code claim lines were unpaid?
#      B. Create a model to predict when a J-code is unpaid. Explain why you choose the modeling approach.
#      C. How accurate is your model at predicting unpaid claims?
#      D. What data attributes are predominately influencing the rate of non-payment?
#*******************************************************************

# import necessary libraries
import numpy as np
import numpy.lib.recfunctions as rfn 
from collections import OrderedDict
from collections import Counter 
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from scipy.sparse import csr_matrix

# define helper functions

# Define a function to do our one hot encoding. 
def OHE_Values(arrayVals):
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(arrayVals)

    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    
    return onehot_encoded

# Column names that will be used in the below function
names = ["V1","Claim.Number","Claim.Line.Number",
         "Member.ID","Provider.ID","Line.Of.Business.ID",
         "Revenue.Code","Service.Code","Place.Of.Service.Code",
         "Procedure.Code","Diagnosis.Code","Claim.Charge.Amount",
         "Denial.Reason.Code","Price.Index","In.Out.Of.Network",
         "Reference.Index","Pricing.Index","Capitation.Index",
         "Subscriber.Payment.Amount","Provider.Payment.Amount",
         "Group.Index","Subscriber.Index","Subgroup.Index",
         "Claim.Type","Claim.Subscriber.Type","Claim.Pre.Prince.Index",
         "Claim.Current.Status","Network.ID","Agreement.ID"]

#These are the data types or dtypes that will be used in the below function
types = ['S8', 'f8', 'i4', 'i4', 'S14', 'S6', 'S6', 'S6', 'S4', 'S9', 'S7', 'f8',
         'S5', 'S3', 'S3', 'S3', 'S3', 'S3', 'f8', 'f8', 'i4', 'i4', 'i4', 'S3',
         'S3', 'S3', 'S4', 'S14', 'S14']

#read in the claims data into a structured numpy array
ClaimData = np.genfromtxt('C:/RAI/DS7335-ML2/HW3/claim.sample.csv', dtype=types, delimiter=',', names=True,
                       usecols=[0,1,2,3,4,5,
                                6,7,8,9,10,11,
                                12,13,14,15,16,
                                17,18,19,20,21,
                                22,23,24,25,26,
                                27,28])

# 1A - Get the count of J-Codes in the file
# Count Procedure codes that start with J
test = 'J'
test = test.encode()

#Try find() on ClaimData. Look only in the first position since J-Codes start with "J"
JCodeIndexes = np.flatnonzero(np.core.defchararray.find(ClaimData['ProcedureCode'], test, start=0, end=1)!=-1)

#Using those indexes, subset ClaimData to only JCodes
JCodes = ClaimData[JCodeIndexes]

# Print out the number of J-Codes. Based on the search we have 51029 for the current data file
print("Total Number of J-Codes: " ,np.count_nonzero(JCodes))

# 1B - Determine the amount paid for J-Codes to "In Network" Providers
InNetworkCode = 'I'
InNetworkCode = InNetworkCode.encode()

# Try find() on JCodes. Look for all in network procedures
InNetJCodeIndexes = np.flatnonzero(np.core.defchararray.find(JCodes['InOutOfNetwork'], InNetworkCode, start=0, end=1)!=-1)

# Build the in-network JCodes List
InNetworkJCodes = JCodes[InNetJCodeIndexes]

# Get the total payment amount
PaidAmt = InNetworkJCodes['ProviderPaymentAmount'].sum()

# Print out the total payment amount of in-network J-code payments to providers
# Roughly $2,417,220.96 paid
print("Total Amount Paid to Providers In-Network: " , '${:,.2f}'.format(PaidAmt))

# 1C - What are the top five J-codes based on the payment to providers?
#Sort the J-Codes
Sorted_JCodes = np.sort(JCodes, order='ProviderPaymentAmount')

# Reverse the sorted JCodes (A.K.A. in descending order)
Sorted_JCodes = Sorted_JCodes[::-1]

# Subset the arrays
ProviderPayments = Sorted_JCodes['ProviderPaymentAmount']
JCodes = Sorted_JCodes['ProcedureCode']

# Join arrays together
arrays = [JCodes, ProviderPayments]

# Merge the two arrays into the providers array
JCodes_with_ProviderPayments = rfn.merge_arrays(arrays, flatten = True, usemask = False)

# Print the top 5 Provider amounts with J-Codes. 
# These are the top 5 provider amounts regardless of J-Code, hence J-Codes and amounts may be 
# repeated 
print("Top 5 Provider Amounts with J-Codes: ", JCodes_with_ProviderPayments[:5])

# To get more distinct and not produce duplicate J-codes we can use a 
# dictionary as provide in the example
#GroupBy JCodes using a dictionary
JCode_dict = {}

#Aggregate with Jcodes - code  modifiedfrom a former student's code, Anthony Schrams
for aJCode in JCodes_with_ProviderPayments:
    if aJCode[0] in JCode_dict.keys():
        JCode_dict[aJCode[0]] += aJCode[1]
    else:
        aJCode[0] not in JCode_dict.keys()
        JCode_dict[aJCode[0]] = aJCode[1]

#sum the JCodes
np.sum([v1 for k1,v1 in JCode_dict.items()])

#create an OrderedDict (which we imported from collections): https://docs.python.org/3.7/library/collections.html#collections.OrderedDict
#Then, sort in descending order
JCodes_PaymentsAgg_descending = OrderedDict(sorted(JCode_dict.items(), key=lambda aJCode: aJCode[1], reverse=True))

#print the results
JCodes_Agg = Counter(JCodes_PaymentsAgg_descending)
print("Top 5 Most Common J-Codes with Provider Amounts: ", JCodes_Agg.most_common(5))

# 2A. Create a scatter plot that displays the number of unpaid claims (lines
#     where the ‘Provider.Payment.Amount’ field is equal to zero) for each 
#     provider versus the number of paid claim

# Get the list of unique providers codes to use as l
plotLabels = Sorted_JCodes['ProviderID']
plotLabels = np.unique(plotLabels)

# Build out our UNPAIDAGG and PAIDAGG arrays. Fill with zeros initially
UNPAIDAGG = np.zeros(len(plotLabels))
PAIDAGG = np.zeros(len(plotLabels))

# Loop through the Sorted_JCodes array and build out our aggregates
for element in Sorted_JCodes:
    # find the index of the provider in our unique list
    idxProvider = np.where(plotLabels == element['ProviderID'])
    
    # Update the array with the count of paid vs. unpaid for the provider
    if (element['ProviderPaymentAmount'] > 0):
        PAIDAGG[idxProvider] = PAIDAGG[idxProvider] + 1
    else:
        UNPAIDAGG[idxProvider] = UNPAIDAGG[idxProvider] + 1


# Produce the scatterplot as the answer. 
# Code below comes from the office hours documents provided
fig, ax = plt.subplots()
ax.scatter(UNPAIDAGG, PAIDAGG)
ax.grid(linestyle='-', linewidth='0.75', color='red')

fig = plt.gcf()
fig.set_size_inches(25, 25)
plt.rcParams.update({'font.size': 28})

for i, txt in enumerate(plotLabels):
    ax.annotate(txt, (UNPAIDAGG[i], PAIDAGG[i]))

plt.tick_params(labelsize=35)
plt.xlabel('# of Unpaid claims', fontsize=35)

plt.ylabel('# of Paid claims', fontsize=35)

plt.title('Scatterplot of Unpaid and Paid claims by Provider', fontsize=45)
plt.savefig('Croom_HW_3_Paid_Unpaid_Scatterplot.png')

# 2B. What insights can you suggest from the graph?
#
# From the graph we're able to see that a few of the providers have a lot of unpaid claims and
# realtively few paid claims. There are also providers that have the reverse situation with high paid
# claims and low unpaid claims. There is also a cluster of providers who are extremely low on the scale
# this would need some additional digging to determine what the root cause of this is

# 2C. Based on the graph, is the behavior of any of the providers concerning? Explain.
#
# The providers with high unpaid claims and low paid claims does stand out. One wonders if the unpaid 
# claims could be due to coding errors or other paperwork mistakes. What we also don't see on the graph is
# providers with a high number of paid claims and a low number of unpaid claims. The size of the unpaid
# claims is much larger than paid claims. The trend seems to be the more paid claims providers have the more 
# unpaid claims there are. 

# 3A. What percentage of J-code claim lines were unpaid?

# Get the total number of records with J-Codes
TotalJCodes = len(Sorted_JCodes)


UnPaidLines = 0
# Loop through the Sorted_JCodes array and count the unpaid claims
for element in Sorted_JCodes:
    # Update the array with the count of paid vs. unpaid for the provider
    if (element['ProviderPaymentAmount'] == 0):
        UnPaidLines += 1

# Print out the unpaid percentage. Approximately 88.11%
print("The percentage of unpaid J-code claims is: ",'{:,.2f}%'.format((UnPaidLines/TotalJCodes)*100))

# B. Create a model to predict when a J-code is unpaid. Explain why you choose the modeling approach.

# Break out values for one-hot encoding. Since we're going to have so many zeros convert the matrices to
# sparse matrices to help save memory

lineOfBusiness = Sorted_JCodes['LineOfBusinessID']
lineOfBusiness = OHE_Values(lineOfBusiness)
lineOfBusiness = csr_matrix(lineOfBusiness)

RevenueCode = Sorted_JCodes['RevenueCode']
RevenueCode = OHE_Values(RevenueCode)
RevenueCode = csr_matrix(RevenueCode)

ServiceCode = Sorted_JCodes['ServiceCode']
ServiceCode = OHE_Values(ServiceCode)
ServiceCode = csr_matrix(ServiceCode)

ProcedureCode = Sorted_JCodes['ProcedureCode']
ProcedureCode = OHE_Values(ProcedureCode)
ProcedureCode = csr_matrix(ProcedureCode)

DiagnosisCode = Sorted_JCodes['DiagnosisCode']
DiagnosisCode = OHE_Values(DiagnosisCode)
DiagnosisCode = csr_matrix(DiagnosisCode)

claimCharge = Sorted_JCodes['ClaimChargeAmount']

DenialReasonCode = Sorted_JCodes['DenialReasonCode']
DenialReasonCode = OHE_Values(DenialReasonCode)
DenialReasonCode = csr_matrix(DenialReasonCode)

PriceIndex = Sorted_JCodes['PriceIndex']
PriceIndex = OHE_Values(PriceIndex)
PriceIndex = csr_matrix(PriceIndex)

PlaceOfServiceCode = Sorted_JCodes['PlaceOfServiceCode']
PlaceOfServiceCode = OHE_Values(PlaceOfServiceCode)
PlaceOfServiceCode = csr_matrix(PlaceOfServiceCode)

inOutNetwork = Sorted_JCodes['InOutOfNetwork']
inOutNetwork = OHE_Values(inOutNetwork)
inOutNetwork = csr_matrix(inOutNetwork)

ReferenceIndex = Sorted_JCodes['ReferenceIndex']
ReferenceIndex = OHE_Values(ReferenceIndex)
RevenueCode = csr_matrix(ReferenceIndex)

PricingIndex  = Sorted_JCodes['PricingIndex']
PricingIndex = OHE_Values(PricingIndex)
PricingIndex = csr_matrix(PricingIndex)

CapitationIndex = Sorted_JCodes['CapitationIndex']
CapitationIndex = OHE_Values(CapitationIndex)
CapitationIndex = csr_matrix(CapitationIndex)

ProviderPaymentAmount = Sorted_JCodes['ProviderPaymentAmount']

ClaimType = Sorted_JCodes['ClaimType']
ClaimType = OHE_Values(ClaimType)
ClaimType = csr_matrix(ClaimType)

ClaimPrePrinceIndex = Sorted_JCodes['ClaimPrePrinceIndex']
ClaimPrePrinceIndex = OHE_Values(ClaimPrePrinceIndex)
ClaimPrePrinceIndex = csr_matrix(ClaimPrePrinceIndex)

ClaimCurrentStatus = Sorted_JCodes['ClaimCurrentStatus']
ClaimCurrentStatus = OHE_Values(ClaimCurrentStatus)
ClaimCurrentStatus = csr_matrix(ClaimCurrentStatus)

# Horizontally stack our sparse matrices to keep the shape
newarray = hstack([lineOfBusiness, RevenueCode, ServiceCode, ProcedureCode,
          DiagnosisCode, DenialReasonCode,PriceIndex, inOutNetwork,
          ReferenceIndex, PricingIndex, CapitationIndex, ClaimType,
          ClaimPrePrinceIndex, ClaimCurrentStatus]).toarray()

# combine our one hot encoded arrays with our numerical arrays
arrays = [newarray,  claimCharge]
OHE_JCodes = rfn.merge_arrays(arrays, flatten = True, usemask = False)

# Convert our ProviderPayerAmount to 0 or 1 for model analysis
ProviderPaymentAmount = np.where(ProviderPaymentAmount > 0,1,0)

# GIven that we're trying to classify whether payment will be made not we'll perform a 
# Logistic Regression. This will be the easiest model to get results from
X_train, X_test, y_train, y_test = train_test_split(newarray, ProviderPaymentAmount, test_size=0.3, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Display the accuracy of our classifier. Based on what we're seeing the accuracy is in the 90's. This 
# may mean we got really lucky and have a good model or that we should go back and perform additional refinement 
# of the variables.
y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

# Display the confusion_matrix and classification report for viewing.
confusion_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion_matrix)

print("Classification Report")
print(classification_report(y_test, y_pred))

# Get the important features and plot them. We see with the one hot encoding we 
# have a bunch of features. There are only a few that seem to be significant though. 
importance = logreg.coef_[0]
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature: %0d, Score: %.5f' % (i,v))
 
# plot feature importance
plt.bar([x for x in range(len(importance))], importance)
plt.show()
plt.savefig('Croom_HW3_Feature_Importance.png')

# Let's clean up the features a bit and display anything greater than -2 or 2
# This will give us the key features of importance
for i,v in enumerate(importance):
    if v <= -2 or v > 2:
	    print('Feature: %0d, Score: %.5f' % (i,v))
     
     
