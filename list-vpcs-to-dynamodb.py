import json
import boto3

ec2 = boto3.client('ec2')
dynamodb = boto3.client('dynamodb')


def lambda_handler(event, context):

    vpcs = ec2.describe_vpcs()

    vpc_ids = []

    for vpc in vpcs['Vpcs']:
        vpc_ids.append(vpc['VpcId'])

        dynamodb.put_item(TableName='vpc_ids', Item={'VPC_ID': {
            'S': vpc['VpcId']}, 'CIDR': {'S': vpc['CidrBlock']}})

    vpc_ids_json = json.dumps(vpc_ids)

    return {
        'statusCode': 200,
        'body': vpc_ids_json
    }
