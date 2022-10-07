# Running Jupyter Notebooks Using papermill Deployed to AWS Lambda
Assumptions:
* The current requirements.txt file contains papermill, pandas, numpy, ipykernel, jupyter. If the notebook needs other packages, they can be added there.
* A function already exists. If not then the function can be created using the CLI tool and command shown [here](https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html) or was created through the AWS console.

### Prerequisites

* A credentials file with no file extension needs to be created to pass in your AWS credentials. This file includes 
```
AWS_ACCESS_KEY_ID=<ID>
AWS_SECRET_ACCESS_KEY=<KEY>
AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>
AWS_REGION=<region>
```


### To run and test lambda locally:

* Pull lambda image using command `docker pull lambci/lambda:python3.8`
* `docker build --build-arg bucket=<bucket name> -t papermill-lambda-test-image .`
* `docker run --name papermill-container --env-file <credentials-filepath> -v "$PWD":/var/task -it papermill-lambda-test-image lambda_function.lambda_handler '{}'`

(Note that if one of your packages need to be installed using a git repo i.e. `git+https://github.com/openai/whisper.git` it will not be possible in test due to the image not allowing for installation of git)

### To deploy the lambda into AWS:

* Pull lambda image using command `docker pull lambci/lambda:build-python3.8`
* `docker build --build-arg bucket=<bucket name> -t papermill-lambda-image -f Dockerfile-deploy .`
* `docker run --env-file <credentials-filepath> -e bucket=<bucket name> papermill-lambda-image`

