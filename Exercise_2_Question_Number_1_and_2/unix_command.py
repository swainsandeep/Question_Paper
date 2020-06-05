#Script for telenet to the server

import getpass
import sys
import telnetlibHOST = "hostname"
user = 'user'
# password = getpass.getpass()
password = 'password'
tn = telnetlib.Telnet(HOST)
tn.read_until("login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
tn.write("ls\n")
tn.write("exit\n")
print (tn.read_all())

#script for ssh to a server check the disk usage,inode usage,check the list of files,
#copy files from local system using scp and ftplib

import paramiko
import time
import ftplib
import os
from scp import SCPClientip = 'hostname'
name = 'userid'
password = 'password'
ssh_client = paramiko.SSHClient()
ssh_client.connect(hostname=ip,username=name,password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('ls')
print (ssh_stdout)
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('df -h')
print (ssh_stdout)
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('df -i')
print (ssh_stdout)

#via scp
with SCPClient(ssh.get_transport()) as scp:
    scp.put('my_file.txt', 'my_file.txt')ssh_client#via ftplib

#via ftplibrary
filename = "MyFile.py"
ftp = ftplib.FTP("xx.xx.xx.xx")
ftp.login("UID", "PSW")
ftp.cwd("/Unix/Folder/where/I/want/to/put/file")
os.chdir(r"\\windows\folder\which\has\file")
myfile = open(filename, 'r')
ftp.storlines('STOR ' + filename, myfile)
myfile.close()
ftp.quit()


###connect to ftp server and write n number of files and zip them 
####and download them

import StringIO
import paramikoprint ("enter the numeber")
no_of_files = int(input())
ftp = FTP('ftp.mysite.com')
ftp.login('un','pw')
ftp.cwd('/')
for i in range(no_of_files):
    ftp.storbinary(f'STOR file_name_{i}', StringIO.StringIO('text to store'))
ftp.quit()
ip = 'hostname'
name = 'userid'
password = 'password'
ssh_client = paramiko.SSHClient()
ssh_client.connect(hostname=ip,username=name,password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command('zip archive.zip file_name_*')
# print (ssh_stdout)filename = archive.zip
ftp = FTP("Server IP")
ftp.login("UserName", "Password")
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()
