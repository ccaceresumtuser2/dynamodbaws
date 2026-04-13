"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo valida si existe Item  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""
from config.conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()


#funcion para validar si existe item por id y devuelve True o False
def existe_usuario(table_name, user_id):
    try:
        table = dynamodb.Table(table_name)

        response = table.get_item(
            Key={'id': user_id}
        )
        return 'Item' in response
    except Exception as e:
        print(e)

#llamado a la funcion
print(existe_usuario("Usuarios","2"))