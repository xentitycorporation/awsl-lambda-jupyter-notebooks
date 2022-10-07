import json
import boto3
import papermill as pm
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    s3.meta.client.download_file('nb-scripts', 'testing.ipynb', '/tmp/test.ipynb')
    pm.execute_notebook('/tmp/test.ipynb', '/tmp/juptest_output.ipynb', kernel_name='python3')
    s3.meta.client.upload_file('/tmp/juptest_output.ipynb', 'nb-scripts', 'output/juptest_output.ipynb')
    logger.info(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
