cerveja =10
vodka =30
wisky =50
cliente =int(input("Você quer qual bebida? 1 para cerveja 2 para vodka 3 para wisky: "))

if cliente == 2:
    quantidade =int(input('quantas doses você quer?' ))
    preço = quantidade * vodka
    print(f'Você comprou {quantidade} doses de vodka, total a pagar: {preço} R$ ')    
    
elif cliente == 1:
    quantidade =int(input('quantas doses você quer?' ))
    preço = quantidade * cerveja
    print(f'Você comprou {quantidade} doses de cerveja, total a pagar: {preço} R$ ')

elif cliente == 3:
    quantidade =int(input('quantas doses você quer?' ))
    preço = quantidade * wisky
    print(f'Você comprou {quantidade} doses de wisky, total a pagar: {preço} R$ ')

else:
   print('digito inválido')