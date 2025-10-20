nome_pet = input('qual o nome do doguinho?: ')
idade_pet = int(input("digite a idade do pet: "))
calculo = int(idade_pet*7)
print(f'seu cachorro tem {idade_pet} logo na idade em anos de cachorro é {calculo}')

porte = str(input('Qual o porte do cachorro: ' ))

valor = 00.00
custo = 00.00

if porte == 'grande': 
    valor = 75.00
    custo = 20.00

elif porte == 'médio':
     valor = 60.00
     custo = 15.00

elif porte == 'pequeno':
     valor = 50.00
     custo = 5.00

periodo = input('A quantos mêses esse cachorro é atendido?: ')
banho = input('E quantos banho ele tomou nesse periodo?: ')
lucro = valor - custo

print (f'olá, {nome_pet} tem {calculo} anos e nos últimos {periodo} meses o lucro com este animal foi de {lucro: .2f}')




