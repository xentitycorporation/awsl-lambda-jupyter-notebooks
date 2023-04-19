"""
Lambda that executes Jupyter Notebooks and saves executed outputs back to s3.
"""
import os
import tempfile
import logging
from dotenv import load_dotenv
import boto3
import papermill as pm

logger = logging.getLogger()
logger.setLevel(logging.INFO)

load_dotenv()
print(os.environ["AWS_PROFILE"])

def lambda_handler(event, context):
    """
    Main lambda handler.
    """
    notebook = event['notebook']
    bucket = event['bucket']
    key = event['key']
    output = event['output']
    tmp = tempfile.gettempdir()
    s3_client = boto3.resource('s3')
    params = {
        'offset': event['offset'],
        'batch_size': event['batch_size'],
        'bucket': bucket,
        'csv_file': event['csv_file']
    }
    s3_client.meta.client.download_file(bucket, notebook, f'{tmp}/{notebook}')
    pm.execute_notebook(
        f'{tmp}/{notebook}',
        f's3://{bucket}/{output}',
        kernel_name='python3',
        parameters=params
        )
    s3_client.meta.client.upload_file(f'{tmp}/{output}', bucket, f'{key}/{output}')
