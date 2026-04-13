import boto3

from enviroment import (
    REGION_AWS, 
    SERVICIO_AWS_DYNAMODB
    )

def conexion_aws_boto3():
    return boto3.resource(SERVICIO_AWS_DYNAMODB,
                           region_name=REGION_AWS)

