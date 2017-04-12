user = 'andre'
passwd = '123'

usuario = raw_input ('Digite o usuario: ')
senha = raw_input ('Digite a senha: ')

if usuario == user and senha == passwd:
	print 'Usuario autenticado com sucesso'
	print 'Seja bem vindo, %s' % usuario

else:

	print 'Acesso Negado'