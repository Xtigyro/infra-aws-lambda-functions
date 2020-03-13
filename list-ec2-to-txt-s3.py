import json
import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')


def lambda_handler(event, context):

    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['*']
        }
    ]

    instances = ec2.instances.filter(Filters=filters)

    RunningInstances = []

    for instance in instances:
        RunningInstances.append(instance.id)

    instanceList = json.dumps(RunningInstances)

    s3.Object(
        'kodyaz-com-aws',
        'instanceList.txt').put(Body=instanceList)

    return {
        'statusCode': 200,
        'body': instanceList
    }
