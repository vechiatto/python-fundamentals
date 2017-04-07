animais = ['tigre', 'boi', 'galinha']

def exibir_lista(lista):

	for a in lista:

		print a

exibir_lista(animais)

#-----------------

def somar(a, b=2):
		return a+b

resultado = somar(5)

print resultado

#--------------------

def subtrair (*args):
	print args

subtrair(2,3,10,50)

#--------------------

def multiplicar (*args,**kwargs):
	
	print kwargs

multiplicar(a=2,b=1,c=4,d=6)

#-----------------------------------

words = ['pera', 'uva', 'mamao']
frutas = lambda words: [len(w) for w in words]
print frutas(words)

#------------------------------------------

words = ['pera', 'uva', 'mamao']

def size(words):
	lista = []
	for w in words:
		lista.append(len(w))
		return lista

print frutas(words)

#--------------------------------------------------

try:

	print 'linha 1'
	
	func()	
	
	print 3 + 3

except Exception as e:
	
	print 'Algo de errado'















































