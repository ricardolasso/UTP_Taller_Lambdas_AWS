import json

# import requests

def calculator_function(numero1, numero2, funcion):
    match funcion:
        case "suma":
            return numero1 + numero2
        case "resta":
            return numero1 - numero2
        case "multiplicacion":
                return numero1 * numero2
        case "division":
            return numero1 / numero2
    

def lambda_handler(event, context):
    calculator = event['calculator']
    numero1 = int(calculator['numero1'])
    numero2 = int(calculator['numero2'])
    funcion = calculator['funcion']
    print(f'Numero1: {numero1}, Numero2: {numero2}, Funcion: {funcion}')
    result = calculator_function(numero1, numero2, funcion)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "resultado": f"{result}",
        }),
    }
