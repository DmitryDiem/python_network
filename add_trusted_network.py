import paramiko
import sys

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('###', username='###', password='###')

stdin, stdout, stderr = ssh.exec_command("get system status")
type(stdin)
arrayF = stdout.readlines()
y = "Virtual domain configuration: enable\n"
for x in arrayF:
    if x.split(" ") == y.split(" "):
        stdin = ssh.exec_command(
            "config system admin\nedit admin\n set trusthost9 192.168.49.0 255.255.255.0\n end \nend")
    else:
        stdin = ssh.exec_command(
            "conf global\nconfig system admin\nedit admin\nset trusthost9 192.168.49.0 255.255.255.0\nend\nend")
