valorinicial = float(input('Qual foi o valor da compra? '))

# if valorinicial > 250.00:
#     valorfinal = valorinicial * 0.84
#     print(f'Nesta caso há desconto de 16%. O valor final da compra é R${valorfinal}')
# else:
#     print(f'Neste caso não há desconto. O valor final da compra continua sendo R${valorinicial}')

if valorinicial <= 250.00:
    print(f'Neste caso não há desconto. O valor final da compra continua sendo R${valorinicial}')
else:
    valorfinal = valorinicial * 0.84
    print(f'Nesta caso há desconto de 16%. O valor final da compra é R${valorfinal}')