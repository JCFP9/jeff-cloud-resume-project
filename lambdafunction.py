import boto3
from botocore.exceptions import ClientError

# Define the Lambda handler function
def lambda_handler(event, context):
    # Initialize a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    
    # Replace 'YourTableName' with the actual name of your DynamoDB table
    table = dynamodb.Table('VisitCounter')
    
    try:
        # Update the 'count' attribute of the item with 'id' as 'counter'
        # Use '#c' as a placeholder for the reserved keyword 'count'
        response = table.update_item(
            Key={
                'id': 'counter'
            },
            UpdateExpression='ADD #c :inc',
            ExpressionAttributeNames={
                '#c': 'count'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues='UPDATED_NEW'
        )
        return response
    except ClientError as e:
        # Handle the exception
        print(e.response['Error']['Message'])
        return e.response['Error']['Message']
