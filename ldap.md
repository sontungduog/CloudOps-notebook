`
LDAPTLS_REQCERT=never ldapsearch -xLLL -D "cn=directory manager" -w '***' -Z -b "uid=****,cn=users,cn=accounts,dc=sre,dc=com"
`
```
ldapmodify -x -D "cn=directory manager" -w '***' -Z <<EOF
dn: fqdn=$i,cn=computers,cn=accounts,dc=sre,dc=com
changetype: delete
EOF
```
