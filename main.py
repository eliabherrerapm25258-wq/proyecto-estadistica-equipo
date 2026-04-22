#declaracion de la funcion
def suma (a,b):
    rest = a+b
    return rest 
    
"""
realiza la suma de dos numeros:

argumentos:
a (int):primer numero a sumar
b (int):segundo numero a sumar
retorno:
   (int): resultado de la suma de dos numeros
   """
def main():
    print("--- Analizador de datos v1.0---")
    datos = [10,20.30,40,50,60] # datos de prueba
    print(f"Datos a procesar: {datos}")

if __name__ == "__main__":
    main()