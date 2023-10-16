vel = float(input("Velocidade atingida: "))
multa = vel * 7
limite = 60
if vel > limite :
 print(F"Você recebeu uma multa de {multa}")
else :
 print(f"Você não recebeu nenhuma multa.")