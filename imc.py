import math

peso = int(input("Ingresa tu peso en kilos: "))
altura = int(input("Ingresa tu altura en centímetros: "))

IMC = peso/((altura/100)**2)

print(f"el IMC es: {IMC:.2f}") 


if IMC <= 18.5:
    print("La clasificación OMS Bajo Peso")
elif IMC > 18.5 and IMC <= 25:
    print("La clasificación OMS Adecuado")    
elif IMC > 25 and IMC <= 30:
    print("La clasificación OMS Sobrepeso")    
elif IMC < 30 and IMC <=35:
    print("La clasificación OMS Obesidad Grado I")  
elif IMC <35  and IMC <=40:
    print("La clasificación OMS Obesidad Grado II")  
elif IMC > 40:
    print("La clasificación OMS Obesidad Grado III")  