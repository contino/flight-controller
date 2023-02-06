# Store API Key valie in SSM Parameter store
import boto3
ssm_client = boto3.client('ssm')
ssm_client.put_parameter(Name="flight_controller_api_key", Value="<INSERT NEW KEY HERE>", Type="String", Overwrite=True)