import json
import boto3

ec2 = boto3.client('ec2')
dynamodb = boto3.client('dynamodb')


def lambda_handler_vpcs(event, context):

    vpcs = ec2.describe_vpcs()

    vpc_ids = []

    for vpc in vpcs['Vpcs']:
        vpc_ids.append(vpc['VpcId'])

        dynamodb.put_item(TableName='vpc_ids', Item={vpc['VpcId']})

    vpc_ids_json = json.dumps(vpc_ids)

    return {
        'statusCode': 200,
        'body': vpc_ids_json
    }


def lambda_handler_subnets(event, context):

    subnets = ec2.describe_subnets()

    subnet_ids = []

    for subnet in subnets['Subnets']:
        subnet_ids.append(subnet['SubnetId'])

        dynamodb.put_item(TableName='subnet_ids', Item={subnet['SubnetId']})

    subnet_ids_json = json.dumps(subnet_ids)

    return {
        'statusCode': 200,
        'body': subnet_ids_json
    }
