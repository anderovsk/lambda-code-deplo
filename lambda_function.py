import json

def lambda_handler(event, context):
    path = event['path']
    http_method = event['httpMethod']
    
    if path == '/funcao1' and http_method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps('Esta é a função 1')
        }
    
    elif path == '/funcao2' and http_method == 'POST':
        return {
            'statusCode': 200,
            'body': json.dumps('Esta é a função 2')
        }
    
    elif path == '/funcao3' and http_method == 'PUT':
        return {
            'statusCode': 200,
            'body': json.dumps('Esta é a função 3')
        }
    
    else:
        return {
            'statusCode': 404,
            'body': json.dumps('Recurso não encontrado')
        }
