```
Đầy ổ đĩa do 1 tiến trình hold quá nhiều file đã xóa
Check lsof +L1 --> restart tiến trình
```


```
root@bastion-spew1-01:/var/spool/clientmqueue]# crontab -e
/tmp/crontab.BUUK4T: No space left on device
Reason: have one folder has full inode while disk usage not full
-Check diskusage:
df -h
- Check inode:
df -i
- Find folder used inode full
for i in /*; do echo $i; find $i/ |wc -l; done
/* : folder has inode full

- Choose folder has max inode
- Cd to them
- Remove inode
find . -type f |xargs rm -rf

cd /var/spool/clientmqueue/
  find . -type f | xargs rm -rf
http://192.155.82.96/solved-how-delete-files-clientmqueue
```


```
Check memory usage in System
free -m
#Check process using Memory
ps aux --sort '%mem'

#Kill process using max MEM

CacheUsage >= 90% then clear cache on RAM:
 echo 3 | sudo tee '/proc/sys/vm/drop_caches'
 swapoff -a && swapon -a
free -m
Note:
1. Clear PageCache Only
echo 1 > /proc/sys/vm/drop_caches
2. Clear detries and inodes
echo 2 > /proc/sys/vm/drop_caches
3. Clear PageCache, detries and inodes
echo 3 > /proc/sys/vm/drop_caches
```
