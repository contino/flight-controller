import boto3
import botocore
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# secret's name and region
grafana_api_key_name = "flight-controller-grafana-api-key"
grafana_workspace_id = "flight-controller-grafana-workspace-id"
region_name = "ap-southeast-2"

#Set up our Session and Client
session = boto3.session.Session()
client = session.client(
    service_name='secretsmanager',
    region_name=region_name
)

def lambda_handler(event, context):
    secretmanager_client = boto3.client('secretsmanager')
    grafana_client = boto3.client('grafana')

    # Calling SecretsManager
    workspace_id = client.get_secret_value(
        SecretId=grafana_workspace_id
    )['SecretString']
    
    # Calling SecretsManager
    current_api_key = client.get_secret_value(
        SecretId=grafana_api_key_name
    )['SecretString']
    

    #Raw Response
    print(current_api_key)
    
    # Delete key if exists
    try:
        print("Deleting old API Key")
        grafana_client.delete_workspace_api_key(
            keyName=grafana_api_key_name,
            workspaceId=workspace_id
        )
        print("Deleted old API key")
    except grafana_client.exceptions.ResourceNotFoundException:
        pass

    # Generate new API key
    try:
        print("Creating new API key")
        new_api_key = grafana_client.create_workspace_api_key(
            keyName=grafana_api_key_name,
            keyRole='ADMIN',
            secondsToLive=2592000,
            workspaceId=workspace_id
        )['key']
        print("Created new API Key :{}".format(new_api_key))
    except botocore.exceptions.ClientError as error:
        logger.error(error)
        return {
            'statusCode': 500,
            'message': 'Error: Failed to generate new API key'
        }

    # Update the secret with the new API key
    try:
        print("Storing new API key in Secrets Manager")
        secretmanager_client.update_secret(
            SecretId=grafana_api_key_name,
            SecretString=new_api_key
        )
        print("Successfully stored new API key in Secrets Manager")
    except botocore.exceptions.ClientError as error:
        logger.error(error)
        return {
            'statusCode': 500,
            'message': 'Error: Failed to update secret'
        }

    return {
        'statusCode': 200,
        'message': 'Success: Secret rotated successfully'
    }