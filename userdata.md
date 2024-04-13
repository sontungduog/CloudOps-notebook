By default, user data scripts run one time when you launch the instance. To run the user data scripts every time you reboot or start the instance
Linux
```
Content-Type: multipart/mixed; boundary="//"
MIME-Version: 1.0

--//
Content-Type: text/cloud-config; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="cloud-config.txt"

#cloud-config
cloud_final_modules:
- [scripts-user, always]

--//
Content-Type: text/x-shellscript; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Content-Disposition: attachment; filename="userdata.txt"

#!/bin/bash
adduser ipacheck
echo "ipacheck ALL=NOPASSWD: ALL" >> /etc/sudoers
echo "ipacheck:ipacheck123" | chpasswd
# chage -l root
# chage -m 0 -M 99999 -I -1 -E -1 root
# passwd -d root
--//--
```
Windows
```
<script>
</script>
<persist>true</persist>
```
