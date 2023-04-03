import boto3

def lambda_handler(event, context):
    # Configura o cliente SNS
    sns = boto3.client('sns')
    
    # Define o tópico SNS para enviar o e-mail
    topic_arn = 'arn:aws:sns:us-east-1:755424459357:Test'
    
    # Define o corpo do e-mail
    subject = 'Teste de envio de e-mail via AWS Lambda'
    message = 'Este é um e-mail de teste enviado por uma função Lambda da AWS.'
    
    # Envia a mensagem para o tópico SNS
    sns.publish(
        TopicArn=topic_arn,
        Subject=subject,
        Message=message
    )
    
    # Retorna uma mensagem de sucesso
    return {
        'statusCode': 200,
        'body': 'E-mail enviado com sucesso!'
    }
