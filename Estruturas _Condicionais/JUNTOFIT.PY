 #JUNTOFIT

frequencia = int(input("Quantos dias consecutivos o aluno treinou? "))

if frequencia == 21:
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ!")
elif frequencia > 0 and frequencia < 21:
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO!")
elif frequencia == 0:
    print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
