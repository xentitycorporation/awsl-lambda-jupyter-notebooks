# demo-serverless-python-lambda
Serverless Framework Demo for a Python Lambda deployment that showcases how to organize, test, and deploy a project.

# AWS Profile
For xentity users you can setup your profile by contacting the TECH Track for credentials and Access to AWS.

Once you have your AWS Access Key ID and Secret you can configure you profile by typing `aws configure --profile xentity`. If you do not have AWS CLI installed you can download it at https://aws.amazon.com/cli/ on the right hand side.

You will also need to copy the sample.env to be .env to have your profile used by pipenv. You will know it is being used becuase when you run any pipenv run command it will print in the console `Loading .env environment variables...`

# Install Tools
If you have not done so already here are some links and instructions on the various tools that will be needed for this project.

## NodeJS
- Download and install LTS version from https://nodejs.org/en/

## Serverless Framework
- `npm i` to install the serverless drivers

# Deployment
To deploy run the command `npm run stg:deploy` or `npm run prd:deploy` depending on the stage you are publishing.

## Add a layer

These were the steps taken to create the papermill layer to deploy using the serverless framework

- Within the `layers/` folder, run command `mkdir papermill`
- `cd papermill`
- `pip install ipykernel ipython jupyter papermill -t ./python`
-  Once that has finished installing, go to `serverless.yml` and add under layers
    ```yml
    Papermill:
        path: ./layers/papermill
        compatibleRuntimes:
        - python3.8
        - python3.9
    ```
- add to provider
    ```yml
    layers:
        - !Ref PapermillLambdaLayer
    ```
- add to function using papermill layer:
    ```yml
    layers:
        - !Ref PapermillLambdaLayer
    ```
Change as needed if another layer needs to be added. Link to [Documentation](https://www.serverless.com/framework/docs/providers/aws/guide/layers)