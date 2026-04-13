"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo para Elimina la tabla  con AWS DynamoDb con boto3

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

def eliminar_tabla(table_name):
    try:
        table = dynamodb.Table(table_name)
        table.delete()
        table.wait_until_not_exists()  # espera hasta que se elimine completamente
        print(f"Tabla {table_name} eliminada correctamente")
    except Exception as e:
        print(f"Error al eliminar la tabla {table_name}")
        print(e)

# Uso
eliminar_tabla("Usuarios")