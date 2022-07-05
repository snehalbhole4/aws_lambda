import boto3
import json


#Update

def lambda_handler(event, context):
    


    id = event['id']
    name = event['name']

    client = boto3.resource('dynamodb')

    table = client.Table('Pets')

    response = table.update_item(
        Key={'id': 'a'
        },
        UpdateExpression = "SET #ts = :values",
        ExpressionAttributeValues = {':values': 'Polo'},
        ExpressionAttributeNames={"#ts": "name"},
        ReturnValues="UPDATED_NEW"

      )
      

    return {

       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

       'body': 'Record ' + event['id'] + ' updated'

   }

