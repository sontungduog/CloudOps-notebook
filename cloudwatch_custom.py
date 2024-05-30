# Collect cloudwatch custom metrics using Lambda
import boto3
import json
from datetime import datetime


def lambda_handler(event, context):
    client = boto3.client('workspaces')
    response = client.describe_workspaces()
    workspaces = response['Workspaces']

    key_to_find = "State"
    for workspace in workspaces:
        if key_to_find in workspace:
            print(f"{key_to_find}: {workspace[key_to_find]}")
            value_finded = workspace[key_to_find]
            if value_finded == 'AVAILABLE':
                value_finded = 1
            else:
                value_finded = 2

            print(value_finded)
            send_cw_metric(key_to_find, value_finded)
        else:
            print(f"Key '{key_to_find}' not found in the JSON data")


def send_cw_metric(prefixlist_id, pl_used_percent):
    cw_client = boto3.client('cloudwatch')
    response = cw_client.put_metric_data(
        Namespace='Custom/WSStatus',
        MetricData=[
            {
                'MetricName': 'workspaces_status',
                # 'Dimensions': [
                #     {
                #         'Name': 'PrefixListId',
                #         'Value': prefixlist_id
                #     },
                # ],
                'Timestamp': datetime.now(),
                'Value': pl_used_percent,
                'Unit': 'Count'
            },
        ]
    )

