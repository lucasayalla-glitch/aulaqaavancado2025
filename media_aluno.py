#inicio
nome = input('digite seu nome: ')
nota1 = float(input("qual foi sua nota em matematica: "))
nota2 = float(input('qual foi sua nota em ciencias? :'))
nota3 = float(input('qual sua nota em portugues: '))
nota4 = float(input('e qual foi sua nota em artes? :'))

#soma das notas 
media = (nota1 + nota2 + nota3 + nota4) / 4

#print final 
print(f'Olá, {nome}! Sua média é: {media: .1f} pontos')     