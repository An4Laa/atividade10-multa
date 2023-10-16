vel = float(input("Velocidade atingida: "))
limite = 60
multa = limite * 7
if vel > limite :
 print(F"Você recebeu uma multa de {multa}")
else :
 print(f"Você não recebeu nenhuma multa.")