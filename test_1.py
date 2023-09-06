import paramiko
import getpass
 
command = """
uname -a
"""
 
username = input("Enter username: ")
passwd = getpass.getpass("Enter Password: ")
 
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(username=username, password=passwd, hostname='192.168.100.67')
 
stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())
print(stderr.read().decode())
 
client.close()