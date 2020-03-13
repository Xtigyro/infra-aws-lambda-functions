import json
import boto3

ec2 = boto3.client('ec2')
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):

    subnets = ec2.describe_subnets()

    subnet_ids = []

    for subnet in subnets['Subnets']:
        subnet_ids.append(subnet['SubnetId'])

        dynamodb.put_item(TableName='subnet_ids', Item={'SUBNET_ID': {
            'S': subnet['SubnetId']}, 'CIDR': {'S': subnet['CidrBlock']}})

    subnet_ids_json = json.dumps(subnet_ids)

    return {
        'statusCode': 200,
        'body': subnet_ids_json
    }
