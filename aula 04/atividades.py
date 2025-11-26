# valorinicial = float(input('Qual foi o valor da compra? '))

# if valorinicial > 250.00:
#     valorfinal = valorinicial * 0.84
#     print(f'Nesta caso há desconto de 16%. O valor final da compra é R${valorfinal}')
# else:
#     print(f'Neste caso não há desconto. O valor final da compra continua sendo R${valorinicial}')

# if valorinicial <= 250.00:
#     print(f'Neste caso não há desconto. O valor final da compra continua sendo R${valorinicial}')
# else:
#     valorfinal = valorinicial * 0.84
#     print(f'Nesta caso há desconto de 16%. O valor final da compra é R${valorfinal}')

#verificacaoo de login
# usuario = input('Informe o usuário: ')
# senha = input('Informe a senha: ')

# if usuario == 'admin' and senha == '1234':
#     print('O pai ta on!')
# else:
#     print('Ops! Usuário ou senha incorreto!')

# # Condicao para brinde
# compra = float(input('Valor da compra: '))
# cliente_frequente = input('Cliente frequente? [S/N]').lower()

# if compra >= 1000 or cliente_frequente == 's':
#     print('Você tem direito a um brinde!')
# else:
#     print('Sem brinde hoje')

# exercicio notas
# nota = float(input('Informe a nota final do aluno: '))
# # frequencia = float(input('informe a frenquencia do aluno: '))

# #uma opcao
# # if nota >= 7 and frequencia >=75:
# #     print('APROVADO')
# # else:
# #     print('REPROVADO')

# #outra opcao (if encadeado)
# if nota >= 7:
#     frequencia = float(input('Qual a frenquencia do aluno: '))
#     if frequencia >= 75:
#         print('APROVADO')
#     else:
#         print('FREQUENCIA INSUFICIENTE')
# else:
#     print('REPROVADO')

#atividade 2

estoque = float(input('Quantidade disponível no estoque: '))
cliente = float(input('Quantidade solicitada por cliente: '))
pesounid = 3

if cliente < estoque:
    pesofinal = cliente * pesounid
    if pesofinal > 50:
        print('PESO ULTRAPASSA 50KG')
    else:
        print(f'PEDIDO LIBERADO:\n{cliente} UNID.\nTOTAL: {pesofinal}KG')
else:
    print( 'ESTOQUE INSUFICIENTE')
              
   


