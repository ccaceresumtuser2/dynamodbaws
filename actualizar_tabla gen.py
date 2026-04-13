"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo Actualiza la tabla  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""

from config.conexion_aws import conexion_aws_boto3

#llamado a la conexión DynamoDb
dynamodb = conexion_aws_boto3()

#Actualizar tabla generica
def actualizar_tabla(table_name, item):
    try:
        table = dynamodb.Table(table_name)

        update_expression = "SET "
        expression_values = {}
        expression_names = {}

        for key, value in item.items():
            if key != "id":  # no actualizar PK
                update_expression += f"#{key} = :{key}, "
                expression_values[f":{key}"] = value
                expression_names[f"#{key}"] = key

        # quitar última coma
        update_expression = update_expression.rstrip(", ")
        print(update_expression)
        print(expression_values)
        print(expression_names)
        response = table.update_item(
            Key={'id': item['id']},#Identifica qué registro vas a actualizar con id
            UpdateExpression=update_expression,#es la instrucción de actualizacion
            ExpressionAttributeValues=expression_values,#valores reales
            ExpressionAttributeNames=expression_names,#Sirve para evitar errores con palabras reservadas
            ReturnValues="UPDATED_NEW"
        )

        print("Usuario actualizado:", response.get("Attributes"))

    except Exception as e:
        print("Error al actualizar usuario")
        print(e)

item = {
            "id": "1",
            "nombre": "Juan Perez",
                }

#llamado a la función
actualizar_tabla("Usuarios", item)