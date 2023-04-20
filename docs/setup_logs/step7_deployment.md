# Gunicorn Entry point

created 
|_ application.py
|_ requirements.txt

The file import `app` from app.webapp.py. Azure use `application:app` as default for running gunicorn.


# Setup Azure Cli
curl -L https://aka.ms/InstallAzureCli | bash

az login --use-device-code

# Create a Running Environment

`az webapp up --runtime PYTHON:3.10 --resource-group seunb --sku F1`

This command should also create a `.azure/config` file with the new machine properties. 


# Update already configured machine

`az webapp up`

# Read Logs

`az webapp log tail`


# Create Github Action

az webapp deployment github-actions add \
  --repo "gabrielsr/rottenpotatoes" \
  --resource-group esunb \
  --branch main \
  --name <app-service-name> \
  --login-with-github



# Delete App

az group delete \
    --name msdocs-python-webapp-quickstart \
    --no-wait


# Access 
https://green-wave-a6e316b5d8f04194b6ca148a95d18bad.azurewebsites.net

# Admin
https://green-wave-a6e316b5d8f04194b6ca148a95d18bad.scm.azurewebsites.net/webssh/host


https://github.com/Azure/webapps-deploy/issues/28
https://stackoverflow.com/questions/64518967/azure-github-app-deployment-error-publish-profile-does-not-contain-kudu-url