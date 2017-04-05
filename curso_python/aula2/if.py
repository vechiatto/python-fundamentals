idade = raw_input ("Digite sua idade: ")
alcoolizado = raw_input ("Esta alcoolizado?: ")
carteira = raw_input ("Possui carteira?: ")

if idade >= 18 and carteira == 'S' and alcoolizado =='N':
	print 'habilitado'
else:
	print 'proibido'


# nome = 'none'

# if nome:
# 	print 'primeiro if'
# elif False:
# 	print 'elif'
# else:
# 	print 'primeiro else'