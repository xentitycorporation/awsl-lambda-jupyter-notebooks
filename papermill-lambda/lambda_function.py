"""
Lambda that executes Jupyter Notebooks and saves executed outputs back to s3.
"""
import tempfile
import logging
import boto3
import papermill as pm
# import nbformat
# from nbconvert.preprocessors import ExecutePreprocessor
# from nbparameterise import (
#     extract_parameters, replace_definitions, parameter_values
# )

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    """
    Main lambda handler.
    """
    notebook = event['notebook']
    bucket = event['bucket']
    key = event['key']
    output_key = event['output_key']
    output = event['output']
    tmp = tempfile.gettempdir()
    s3_client = boto3.resource('s3')
    params = event['params']
    s3_client.meta.client.download_file(bucket, f'{key}/{notebook}', f'{tmp}/{notebook}')
    pm.execute_notebook(
        f'{tmp}/{notebook}',
        f'{tmp}/{output}',
        kernel_name='python3',
        parameters=params,
        log_output=True,
        )
    # Get a list of Parameter objects
    # with open(f'{tmp}/{notebook}', encoding='utf-8') as nb_file:
    # # with open(f'./notebooks/{notebook}') as ff:
    #     nb_in = nbformat.read(nb_file, nbformat.NO_CONVERT)
    #     orig_parameters = extract_parameters(nb_in)

    #     # Update one or more parameters
    #     nb_params = parameter_values(orig_parameters, **params)

    #     # Make a notebook object with these definitions
    #     nb_in = replace_definitions(nb_in, nb_params)

    # ep = ExecutePreprocessor(timeout=6000)
    # nb_out= ep.preprocess(nb_in)
    # with open(f'{tmp}/{output}', 'w', encoding='utf-8') as f:
    #     nbformat.write(nb_out[0], f)

    s3_client.meta.client.upload_file(f'{tmp}/{output}', bucket, f'{output_key}/{output}')
