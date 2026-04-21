import boto3

tabla = boto3.resource('dynamodb').Table('Empleados')

def guardar_empleado(depto, emp_id, nombre, apellido, cargo, correo):
    tabla.put_item(Item={
        'departamento_id': depto,
        'empleado_id': emp_id,
        'nombre': nombre,
        'apellido': apellido,
        'nombre_apellido': f"{nombre} {apellido}",  # 🔥 clave para búsquedas
        'cargo': cargo,
        'correo': correo
    })

guardar_empleado('IT', 'E001', 'Carlos', 'Perez', 'Backend', 'carlos@mail.com')
guardar_empleado('IT', 'E002', 'Ana', 'Gomez', 'Frontend', 'ana@mail.com')
guardar_empleado('RRHH', 'E003', 'Luis', 'Lopez', 'HR', 'luis@mail.com')