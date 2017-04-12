import psycopg2

flag = True

host = 'localhost'
dbname = 'projeto'
user = 'postgres'
password = '123456'

con = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password))
cur = con.cursor()

session = False

while flag:

    banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Lista usuario
4) Sair
Selecione a opcao: '''

    option = int(raw_input(banner))
    

    if option == 1:

        user = raw_input('Username: ')
        pswd = raw_input('Password: ')

        query = "SELECT * FROM users WHERE usuario='%s' AND pass='%s'" % (user, pswd)
        cur.execute(query)

        usuario = cur.fetchone()

        if usuario:

            session.append(usuario)

        else:

            print 'Username ou password invalidos'

    elif option == 2:

        if not session:

            print 'Usuario nao logado'

            continue

        user = raw_input('Novo Username: ')
        pswd = raw_input('Novo Password: ')

        query = "INSERT INTO users(usuario, pass) \
        VALUES ('%s', '%s')" % (user, pswd);
        try:
            
            cur.execute(query)
            if cur.rowcount:
                cur.commit()
                print 'Cadastro com sucesso'
        except Exception as e:
            con.rollback()
            print 'Falha ao cadastrar'

        
    elif option == 3:
        if not session:
            print 'Usuario nao logado'
            continue

        user = raw_input('Localizar usuario: ')

        query = "SELECT * FROM users WHERE usuario LIKE '%%%S%%'" % user

        cur.execute(query)

        usuario = cur.fechone()

        if usuario:

            print '+++++++++++++++++++++++++++++++++++++++++++++++++++'
            print 'Usuario: %s\nSenha: &s' % (usuario[1], usuario[2])
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++'


    elif option == 4:
        print 'Volte sempre'
        exit()
