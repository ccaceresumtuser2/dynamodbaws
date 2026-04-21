"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo muestra los item(s) de la tabla  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""
from boto3.dynamodb.conditions import Attr

from config.conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()

def scan_item_tabla(tabla):
    try:
        table = dynamodb.Table(tabla)
        response = table.scan()
        for item in response['Items']:
            print(item)
    except Exception as e:
        print(e)

def scan_item_tabla_ordenada(tabla):
    try:
        table = dynamodb.Table(tabla)
        response = table.scan()
        items = response['Items']
        # ordenar por id
        items_ordenados = sorted(items, key=lambda x: x['id'])
        for item in items_ordenados:
            print(item)
    except Exception as e:
        print(e)

def scan_filter_expresion_activo(tabla,activo):
    try:
        table = dynamodb.Table(tabla)
        response = table.scan(
             FilterExpression=Attr('activo').eq(activo)
        )
        items = response['Items']
        # ordenar por id
        items_ordenados = sorted(items, key=lambda x: x['id'])
        for item in items_ordenados:
            print(item)
    except Exception as e:
        print(e)


def scan_filter_expresion_activo_tabla(tabla,activo):
        table = dynamodb.Table(tabla)
        response = table.scan(
             FilterExpression=Attr('activo').eq(activo))
        return response
  
scan_filter_expresion_activo("Usuarios",False)