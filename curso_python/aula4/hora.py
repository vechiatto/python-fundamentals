from datetime import datetime, timedelta

#print datetime.now()

#print datetime.now().strftime('%H/%m/%d')

print datetime(1999, 8, 7, 0,0,0)

print datetime(1999, 8, 7, 0,0,0).strftime('%d/%m/%Y')

#adicionar 4 dias no time delta
print datetime.now() + timedelta(4)

acesso = datetime(2017,01,22,00,00,00)
atual = datetime(2017,01,22,00,55,00)

if (atual - acesso).total_seconds() > 3600:
	print "seu token expirou"

else:

	print "Acesso liberado"