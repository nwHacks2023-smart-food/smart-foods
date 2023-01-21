# Deployment Steps
### Step 1 Create AKS Cluster in Azure
![image](images/createakscluster.png)
### Step 2 Settings for AKS Cluster
![image](images/settings-basic-1.png)
![image](images/settings-basic-2.png)
![image](images/settings-integration.png)
![image](images/settings-networking.png)
- leave the rest of settings untouched
![image](images/settings-option.png)
- click on review and create 
![image](images/create-cluster.png)
- createing the clustet
<br>
### Login to Azure
- Using Azure Cli, using `az login` to get credentials to azure
- Using Azure aks cli `az aks get-credentials --resource-group smart-foods --name smart-food-aks` to get credential for accessing the aks cluster
- the context should be set up to the aks cluster you created
