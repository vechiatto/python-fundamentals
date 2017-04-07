import psycopg2

con = psycopg2.connect(
	"host=%s dbname=%s user=%s password=%s" % (
	'localhost', 'projeto', 'postgres', '123456'
))

cur = con.cursor()

cur.execute(" \
	insert into posts(conteudo, titulo) \
	values ('locadora media', 'filme suspense')")

con.commit()