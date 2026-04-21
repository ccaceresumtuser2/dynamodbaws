"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo busqueda pk,sk,gsi

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 20-04-2026
VERSIÓN: 1.0
Partition Key (obligatorio)
Sort Key (opcional, pero potente)
o un GSI si necesitas otra forma de búsqueda (combinacion pk y sk)

Tabla: Empleados

Campo	          Tipo	Descripción
departamento_id	   PK	Agrupa empleados
empleado_id	       SK	Identificador único
nombre	           atributo	Nombre
apellido           atributo Correo
cargo 
correo	           atributo	Para GSI

===========================================================
"""
import boto3

from config.conexion_aws import conexion_aws_boto3
from boto3.dynamodb.conditions import Key
dynamodb = conexion_aws_boto3()

tabla = dynamodb.Table('Empleados')

#Buscar todos por departamento (PK)
def buscar_por_departamento(depto):
   
    response = tabla.query(
        KeyConditionExpression=Key('departamento_id').eq(depto)
    )
    return response['Items']

# Buscar empleado específico (PK + SK)
def buscar_empleado(depto, emp_id):
    response = tabla.query(
        KeyConditionExpression=
            Key('departamento_id').eq(depto) &
            Key('empleado_id').eq(emp_id)
    )
    return response['Items']

#Buscar por correo (GSI)
def buscar_por_correo(correo):
    response = tabla.query(
        IndexName='correo-index',
        KeyConditionExpression=Key('correo').eq(correo)
    )
    return response['Items']

#Buscar por nombre completo (GSI)
def buscar_por_nombre(nombre_apellido):
    response = tabla.query(
        IndexName='nombre-index',
        KeyConditionExpression=Key('nombre_apellido').eq(nombre_apellido)
    )
    return response['Items']

#Buscar por cargo (GSI)
def buscar_por_cargo(cargo):
    response = tabla.query(
        IndexName='cargo-index',
        KeyConditionExpression=Key('cargo').eq(cargo)
    )
    return response['Items']

def mostrar(items):
   for item in items:
      print(item)

mostrar(buscar_por_departamento('IT'))
#mostrar(buscar_empleado('IT', 'E001'))
#mostrar(buscar_por_correo('luis@mail.com'))
#mostrar(buscar_por_nombre('Ana Gomez'))
#mostrar(buscar_por_cargo('Backend'))
