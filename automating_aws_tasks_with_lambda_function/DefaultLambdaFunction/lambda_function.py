import json

def lambda_handler(event, context):
    # Hello world pycharm test
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
