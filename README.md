# Project Description
SmartFoods is a web app aimed to make healthy diets simple for anyone. Rather than having to count calories and nutrients yourself, all you need to do is select what you want to eat and we will tell you how this fits into a healthy diet!

After users create their cart, we use the Nutritionix API to find the nutritional information of all the items inside the cart. Users are then shown their list of items with corresponding nutritional info and where they can order the item online (currently from Amazon and SaveOnFoods). Links are auto sorted by the lowest price first. 

Microsoft Cloud AKS clusters were used to host our website.  

Further developments include budgeting options, evaluation of which nutrients are (in)sufficient (code in repo but unimplemented due to time), and adding more stores.

## Demo
![image](images/demo-img-0.png)
![image](images/demo-img-1.png)
![image](images/demo-img-2.png)
![image](images/demo-img-3.png)

# Deployment Steps

### Step 1 Create AKS Cluster in Azure

![image](images/createakscluster.png)

### Step 2 Settings for AKS Cluster

![image](images/settings-basic-1.png)
![image](images/settings-basic-2.png)
![image](images/settings-integration.png)
![image](images/settings-networking.png)

-   leave the rest of settings untouched
    ![image](images/settings-option.png)
-   click on review and create
    ![image](images/create-cluster.png)

### Login to Azure

-   Using Azure Cli, using `az login` to get credentials to azure
-   Using Azure aks cli `az aks get-credentials --resource-group smart-foods --name smart-food-aks` to get credential for accessing the aks cluster
-   the context should be set up to the aks cluster you created

### Creating a Ingress Controller

-   Create new namespace with `kubectl create namespace ingress-basic`
-   Find the Resource Group for load balancer
    ![image](images/rg-for-load-balancer.png)
-   Create a public ip as a ingress endpoint for routing to different services `az network public-ip create --resource-group MC_smart-foods_smart-foods-cluster_canadacentral --name PublicIPForIngress --sku Standard --allocation-method static`
-   Using Helm to ingress ingress nginx and changing configs `helm install ingress-nginx ingress-nginx/ingress-nginx --namespace ingress-basic --set controller.nodeSelector."kubernetes\.io/os"=linux --set defaultBackend.nodeSelector."kubernetes\.io/os"=linux --set controller.service.externalTrafficPolicy=Local --set controller.service.loadBalancerIP="4.204.191.212"`
    ![image](images/static-ip.png)
-   Create new namespace with `kubectl create namespace ingress-basic`
-   Create a public ip as a ingress endpoint for routing to differetn services `az network public-ip create --resource-group smart-foods --name PublicIPForIngress --sku Standard --allocation-method static`
    ![image](images/static-ip.png)
-   Installing Ingress-Nginx controller
    ![image](images/ingress-controller.png)
