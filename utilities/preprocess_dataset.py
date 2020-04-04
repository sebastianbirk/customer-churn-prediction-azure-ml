
import numpy as np
import pandas as pd

def run(data, training_mode=True):  
    '''
    This function preprocesses the customer churn dataset so that it is in a format ready to be fed into ML pipelines.
    
    Input: Uncleansed customer churn Pandas dataframe
    
    Output: X is a Pandas dataframe of label & one-hot encoded features
            y is a Pandas series containing the target column "Churn"
    '''
    
    if training_mode==False: # service mode
        
        columns = ['customerID','gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure','PhoneService',
                 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges',
                 'TotalCharges']
        
        data_zipped = zip(columns,data)
        
        data_dictionary = dict(data_zipped)
        
        df = pd.DataFrame(data_dictionary, index=[0])
    
    else:
        df = data
    
    # Drop unnecessary columns which should not be used as features
    df.drop("customerID", axis=1, inplace=True)
    df.drop("PartitionDate", axis=1, inplace=True, errors="ignore")
    
    # Replace spaces with null values in total charges column
    df['TotalCharges'] = df["TotalCharges"].replace(" ",np.nan)
    
    # Convert total charges to float type and tenure to int type
    df["TotalCharges"] = df["TotalCharges"].astype(float)
    df["tenure"] = df["tenure"].astype(int)
    
    # Replace 'No internet service' to No for the following columns
    replace_cols = ["OnlineSecurity", "OnlineBackup", "DeviceProtection",
                    "TechSupport","StreamingTV", "StreamingMovies"]
    for i in replace_cols : 
        df[i]  = df[i].replace({"No internet service":"No"})
    
    # Replace 0 and 1 for numeric binary columns
    num_bin_cols = ["gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService", 
                    "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV",
                    "StreamingMovies", "PaperlessBilling"]
    for i in num_bin_cols : 
        df[i]  = df[i].replace({0:"No", 1:"Yes"})
    
    if training_mode:
        # Replace values for Churn column
        df["Churn"] = df["Churn"].replace({False:0, True:1})
    
    # Transform tenure to categorical column
    def tenure_lab(df) :    
        if df["tenure"] <= 12 :
            return "Tenure_0-12"
        elif (df["tenure"] > 12) & (df["tenure"] <= 24 ):
            return "Tenure_12-24"
        elif (df["tenure"] > 24) & (df["tenure"] <= 48) :
            return "Tenure_24-48"
        elif (df["tenure"] > 48) & (df["tenure"] <= 60) :
            return "Tenure_48-60"
        elif df["tenure"] > 60 :
            return "Tenure_gt_60"
        
    df["tenure_group"] = df.apply(lambda df:tenure_lab(df), axis = 1)
    
    # Drop original tenure column
    df.drop("tenure", axis=1, inplace=True)
    
    # Separate target column from feature columns
    if training_mode:
        y = df["Churn"]
        X = df.drop("Churn", axis=1)
        
    else:
        X = df
    
    '''# Get categorical features
    categorical_features = X.nunique()[df.nunique() < 6].keys().tolist() # get columns with less than 6 unique values

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
    X = pd.get_dummies(data = X)'''
    
    if training_mode:
        return X, y
    
    else:
        return X
