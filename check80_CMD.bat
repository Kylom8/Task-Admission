cd "%USERPROFILE%\Desktop"
mkdir check80
cd "%USERPROFILE%\Desktop\check80"
netstat -aon | findstr "80" > netstat.txt
del netstat.txt