#comparando dois numeros
primeiro = input('Dgite aqui o primeiro numero')
segundo = input('Digite aqui o segundo numero')

primeiro =int(primeiro) #convertendo str para int
segundo =int(segundo)
if primeiro >= segundo:
  print('O primeiro numero é maior')
else:
  print('O segundo numero é maior')