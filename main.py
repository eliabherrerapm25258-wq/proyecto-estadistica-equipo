#declaracion de la funcion
def multiplicacion (a,b):
    rest = a * b
    return rest

""""
Realiza la multiplicacion de dos numeros:

argumentos:
   a (int):primer numero a multiplicar
   b (int):segundo numero a multiplicar

retorno:
    (int): resultado de la multiplicacion de dos numeros
"""
def main():
    print("--- Analizador de datos v1.0---")
    datos = [10,20.30,40,50,60] # datos de prueba
    print(f"Datos a procesar: {datos}")

if __name__ == "__main__":
    main() 