# verifica maior idade
# idade = int(input('informe sua idade: '))

# if idade >= 18:
#     print(f'Se você tem {idade}, então você é maior de idade')
# else:
#     print(f'Se você tem {idade}, então você é menor de idade')

pontos = int(input('Quantos pontos? '))

if pontos >= 100:
    print('Nível máximo')
elif pontos >=50:
    print('Nível bom')
elif pontos >=25:
    print('Nível regular')
else:
    print('Nível baixo')

# se a resposta entra em uma condição, ela não entra mais nas subseguintes utilizando esse esquema de if/elif/else. Se fosse somente if, pode ser que a resposta atingisse todas as condições.
    
