"""
#backup windows
echo on 
SET input=C:\xampp\
SET output=C:\Users\Administrator\Documents\backup\
rem SET des=\\107.113.53.70\Public\Temp\backup_windows\
SET des=\\107.127.130.21\Public\Temp\backup_windows\

set TIMESTAMP=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%

rem Dump mysql
rem "C:\xampp\mysql\bin\mysqldump.exe" -hlocalhost -P3306 -u root --all-databases --skip-lock-tables > %des%backup.%TIMESTAMP%.sql

"C:\xampp\mysql\bin\mysqldump.exe" -hlocalhost -P3306 -u root --lock-tables=false atms > %des%%TIMESTAMP%.atms.sql
"C:\xampp\mysql\bin\mysqldump.exe" -hlocalhost -P3306 -u root apptest > %des%%TIMESTAMP%.apptest.sql


rem Compress data folder
"C:\Program Files\7-Zip\7z.exe" a "%output%%TIMESTAMP%.zip" "%input%"

cd /D %output%
copy * %des%

rem echo "Backup data daily"
timeout /t 4000 /nobreak


rem #Remove file
del /s /q %output%*
"""
'''
#check service processs
delete service windows #SC: Service Control

sc query redis
sc stop redis
sc delete redis

SC QUERY state= all | FIND "redis"
process

tasklist
taskkill
taskkill /F /PID 892
#CHECK INBOUND/OUTBOUND windows #telnet --> check connection/port

netstat -na | findstr "LISTENING" netstat -nao

change directory path: cd d/ D:
'''

'''
#check_port_mapping
echo on
rem SET tool=E:\plink.exe
E:\plink.exe -ssh 107.113.*.* -P 2022 -l scloud -pw opsOpenstack@$#2019 "sudo iptables -t nat -L -v -n --line-numbers | grep 172.17.0.190"

timeout /t 4000 /nobreak
'''
