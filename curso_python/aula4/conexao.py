import paramiko
import os

from paramiko.client import SSHClient

client = SSHClient()

client.load_system_host_keys()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host = '192.168.202.7'

user = 'noturno'

password = '4linux'

client.connect(hostname=host, username=user, password=password )

stdin, stdout, stderr = client.exec_command("LS -la")

#print stdout.read()

#-------------------------------------------------------------

if stderr.channel.recv_exit_status() !=0:
	print stderr.channel.recv_exit_status()
	print stderr.read()
else:
	print stdout.read()

#-----------------------------------------------------------
