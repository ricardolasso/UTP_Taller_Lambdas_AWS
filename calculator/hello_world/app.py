import json

# import requests

def calculator(a: int, b: int, c: str ):
    if c == "suma": 
        return a + b
    elif c == "resta": 
        return a - b
    else: 
        return "No contemplado"


def lambda_handler(event, context):
    calculator_data = event["calculator"]
    a = calculator_data["numero1"]
    b = calculator_data["numero2"]
    funcion = calculator_data["funcion"]
    print(f'Numero 1: {a}, Numero 2: {b}, Funcion: {funcion}')
    calc = calculator(int(a), int(b), funcion)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{calc}",
            # "location": ip.text.replace("\n", "")
        }),
    }
