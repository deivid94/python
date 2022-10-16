renda = int(input('Informe sua renda: ')) #convertidos para int
situacao_score = int (input('informe a quantidade de pontos no seu score 100 a 1000: ')) #onvertido para int


if (renda  >= 5000) and (situacao_score >=600):
  print (f'seu financiamento esta aprovado sua renda é:   {renda} e seu score é de: {situacao_score}') 
else:
  print(f'Voce nao atingiu os requisitos necessarios para aprovacao  Renda de 5.000 Reais, sua renda: {renda} e o seu escore precisa ser maior de 600 pontos, seu score {situacao_score}')
  





