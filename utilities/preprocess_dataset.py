
# Import libraries
import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder

def run_preprocessing(telcom):  
    '''
    This function preprocesses the customer churn dataset so that it is in a format ready to be fed into ML pipelines.
    
    Input: Uncleansed customer churn Pandas dataframe
    
    Output: X is a Pandas dataframe of label & one-hot encoded features
            y is a Pandas series containing the target column "Churn"
    '''
    
    # Drop unnecessary columns which should not be used as features
    telcom.drop(["customerID", "PartitionDate"], axis=1, inplace=True)
    
    # Replace spaces with null values in total charges column
    telcom['TotalCharges'] = telcom["TotalCharges"].replace(" ",np.nan)
    
    # Convert total charges to float type
    telcom["TotalCharges"] = telcom["TotalCharges"].astype(float)
    
    # Replace 'No internet service' to No for the following columns
    replace_cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                    "TechSupport","StreamingTV", "StreamingMovies"]
    for i in replace_cols : 
        telcom[i]  = telcom[i].replace({"No internet service" : "No"})
        
    # Replace values for Churn column
    telcom["Churn"] = telcom["Churn"].replace({False:0, True:1})
    
    # Transform tenure to categorical column
    def tenure_lab(telcom) :    
        if telcom["tenure"] <= 12 :
            return "Tenure_0-12"
        elif (telcom["tenure"] > 12) & (telcom["tenure"] <= 24 ):
            return "Tenure_12-24"
        elif (telcom["tenure"] > 24) & (telcom["tenure"] <= 48) :
            return "Tenure_24-48"
        elif (telcom["tenure"] > 48) & (telcom["tenure"] <= 60) :
            return "Tenure_48-60"
        elif telcom["tenure"] > 60 :
            return "Tenure_gt_60"
        
    telcom["tenure_group"] = telcom.apply(lambda telcom:tenure_lab(telcom), axis = 1)
    
    # Drop original tenure column
    telcom.drop("tenure", axis=1, inplace=True)
    
    # Separate target column from feature columns
    y = telcom["Churn"]
    X = telcom.drop("Churn", axis=1)
    
    # Get categorical features
    categorical_features = X.nunique()[telcom.nunique() < 6].keys().tolist() # get columns with less than 6 unique values

    # Get numerical features
    numeric_features = [x for x in X.columns if x not in categorical_features]
    
    # Binary columns with two values
    binary_features   = X.nunique()[X.nunique() == 2].keys().tolist()
    
    # Columns with more than two values
    multi_features = [i for i in categorical_features if i not in binary_features]
    
    le = LabelEncoder()
    for i in binary_features:
        X[i] = le.fit_transform(X[i])
    
    # Build dummy columns for multi value columns
    X = pd.get_dummies(data = X)
    
    return X, y
