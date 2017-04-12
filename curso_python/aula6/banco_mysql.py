import MySQLdb

con = MySQLdb.connect(
	host='127.0.0.1', user='admin', passwd='python4linux', db='projeto'
)

cur = con.cursor()

#insert
try:
	cur.execute(
		"INSERT INTO posts(titulo, conteudo) \ VALUES('Meu Titulo', 'Meu conteudo')"

	)

	con.commit()
except Exception as e:
		con.rollback()

#update

try:
	cur.execute(
		"UPDATE posts SET titulo='Novo Titulo' \ where id=1"
	)		
	con.commit()
except Exception as e:
		con.rollback()

#select one

cur.execute(
	'SELECT * FROM posts WHERE id=1'
)

print cur.fetchone()

# select all
cur.execute(
	'SELECT id, titulo FROM posts WHERE id=1'
)

for row in cur.fetchall():
	print row

con.close()