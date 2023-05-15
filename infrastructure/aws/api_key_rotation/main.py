import logging

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# secret's name and region
grafana_api_key_name = "flight-controller-grafana-api-key"
secrets_api_key_name = "flight-controller/grafana-api-key"
secrets_workspace_id_name = "flight-controller/grafana-workspace-id"
region_name = "ap-southeast-2"

def lambda_handler(event, context):
    secretmanager_client = boto3.client('secretsmanager')
    grafana_client = boto3.client('grafana')

    # Calling SecretsManager
    workspace_id = secretmanager_client.get_secret_value(
        SecretId=secrets_workspace_id_name
    )['SecretString']
    
    # Calling SecretsManager
    current_api_key = secretmanager_client.get_secret_value(
        SecretId=secrets_api_key_name
    )['SecretString']
    
    # Delete key if exists
    try:
        logger.info("Deleting old API Key")
        grafana_client.delete_workspace_api_key(
            keyName=grafana_api_key_name,
            workspaceId=workspace_id
        )
        logger.info("Deleted old API key")
    except Exception as error:
        logger.error(f"Deletion of old API key failed. Error: {error}")

    # Generate new API key
    try:
        logger.info("Creating new API key")
        new_api_key = grafana_client.create_workspace_api_key(
            keyName=grafana_api_key_name,
            keyRole='ADMIN',
            secondsToLive=2592000,
            workspaceId=workspace_id
        )['key']
        logger.info("Created new API Key :{}".format(new_api_key))
    except ClientError as error:
        logger.error(error)
        return {
            'statusCode': 500,
            'message': 'Error: Failed to generate new API key'
        }

    # Update the secret with the new API key
    try:
        logger.info("Storing new API key in Secrets Manager")
        secretmanager_client.update_secret(
            SecretId=secrets_api_key_name,
            SecretString=new_api_key
        )
        logger.info("Successfully stored new API key in Secrets Manager")
    except ClientError as error:
        logger.error(error)
        return {
            'statusCode': 500,
            'message': 'Error: Failed to update secret'
        }

    return {
        'statusCode': 200,
        'message': 'Success: Secret rotated successfully'
    }