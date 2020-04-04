# Customer Churn Prediction with Azure ML: <br /> From Kaggle Dataset to Productionalized Model

This repository contains an end-to-end ML lifecycle demo using the Azure Maching Learning Studio.

Different features of the Azure Machine Learning Studio will be shown while working to solve a Kaggle challenge to predict customer churn. The Kaggle challenge can be found here: https://www.kaggle.com/blastchar/telco-customer-churn.

**Prerequisites to rebuild the demo:**
- Azure subscription (with credits)
- Some foundational Azure and Data Science knowledge

# Demo Instructions
## Step 1:
Create a resource group.

![create-resource-group](https://user-images.githubusercontent.com/34235961/78451170-1e0ab400-7684-11ea-84ab-ec6707d7c44e.png)

## Step 2:
Create an Azure Machine Learning workspace.

![create-azure-ml-workspace](https://user-images.githubusercontent.com/34235961/78451184-3b3f8280-7684-11ea-93d6-bc64767b8cbd.png)

## Step 3:
Enter your Azure Machine Learning workspace by clicking "Launch Now".

![launch-workspace](https://user-images.githubusercontent.com/34235961/78451415-c9683880-7685-11ea-91b7-2e4a9797ab29.png)

## Step 4:
Create a compute instance in your Azure Maching Learning workspace.

![create-compute-instance](https://user-images.githubusercontent.com/34235961/78451196-54483380-7684-11ea-8996-02c44cd37f44.png)

## Step 5:
Open Jupyter Notebooks in your compute instance.

![open-jupyter](https://user-images.githubusercontent.com/34235961/78451232-a5582780-7684-11ea-8fbb-bdb1e341a905.png)

## Step 6:
Enter the terminal, switch directories to your user directory and clone this repository.

![enter-terminal](https://user-images.githubusercontent.com/34235961/78451218-8bb6e000-7684-11ea-9149-cb9d4c4711b3.png)

![clone-git-repo](https://user-images.githubusercontent.com/34235961/78451210-704bd500-7684-11ea-9f4f-f88080d5218b.png)

## Step 7:
Download the two data files from the "data" folder to your local machine.

![download-data](https://user-images.githubusercontent.com/34235961/78451350-73939080-7685-11ea-9173-a8be7b23e038.png)

## Step 8:
Create an Azure Data Lake Gen2. You do this by creating a storage account that has hierarchical namespace enabled.

![create-data-lake-gen2-1](https://user-images.githubusercontent.com/34235961/78451320-40510180-7685-11ea-985f-9b93a0031135.png)

Enable hierarchical namespace:

![create-data-lake-gen2-2](https://user-images.githubusercontent.com/34235961/78451335-58288580-7685-11ea-8075-9ad4f24296b0.png)

Create a container called "raw" in your Azure Data Lake Gen2.

![create-container](https://user-images.githubusercontent.com/34235961/78451261-d5072f80-7684-11ea-8ef3-46a5db9cf161.png)

Create two directories: 
- 2020/03/31
- 2020/04/01

![create-directory](https://user-images.githubusercontent.com/34235961/78451249-c4ef5000-7684-11ea-9107-8698ca2fdab0.png)

## Step 9:
Upload the two data files in the respective directories in your Azure Data Lake Gen2 (according to the date).

![upload-data](https://user-images.githubusercontent.com/34235961/78451429-e13fbc80-7685-11ea-94e2-e19746bcc0b4.png)

## Step 10:
Register your Azure Data Lake Gen2 as a **storage account** (not as an Azure Data Lake Gen2) datastore in the Azure Machine Learning workspace

First retrieve your storage account key from the Azure Portal:

![get-storage-account-key](https://user-images.githubusercontent.com/34235961/78451374-8c03ab00-7685-11ea-88ec-5b3cff8f2ba0.png)

![create-datastore](https://user-images.githubusercontent.com/34235961/78451312-2c0d0480-7685-11ea-88bc-4c5b59b6c1fa.png)


## Step 11:
Register a dataset using your datastore. **Important: the dataset has to be named "customer-churn".

![create-dataset-1](https://user-images.githubusercontent.com/34235961/78451271-ed774a00-7684-11ea-93e8-ac79edb06b91.png)

![create-dataset-2](https://user-images.githubusercontent.com/34235961/78450741-17c70880-7681-11ea-850f-c3c9f134eba0.png)

![create-dataset-3](https://user-images.githubusercontent.com/34235961/78451294-05e76480-7685-11ea-9688-3d97a699b174.png)

![create-dataset-4](https://user-images.githubusercontent.com/34235961/78451305-18619e00-7685-11ea-9a39-52c60cedd2c1.png)

## Step 12:
Install all necessary dependencies on your compute instance.

![install_dependencies](https://user-images.githubusercontent.com/34235961/78451391-a63d8900-7685-11ea-9da0-4e4ef13cd8bc.png)

## Step 13:
You can now run the notebooks. Specific instructions can be found in the notebooks. You can ommit running 03_customer_churn_train_decision_tree and 04_customer_churn_train_automl.
