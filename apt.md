```
cd /var/cache/apt/archives/
apt-cache madison python2.7-minimal

apt-get download python2.7=2.7.6-8
dpkg -i /var/cache/apt/archives/python2.7_2.7.6-8ubuntu0.5_amd64.deb



apt remove python-sss sssd -f

apt-get autoremove -f
dpkg -l | grep sssd



apt install --reinstall percona-xtrabackup-24
apt install python-sss=1.11.8-0ubuntu0.7
```
