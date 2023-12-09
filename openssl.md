```
openssl s_client -connect storage.googleapis.com:443
openssl s_client -CApath /etc/ssl/certs/ -connect storage.googleapis.com:443
openssl s_client -CAfile /etc/ssl/certs/ca-certificates.crt -connect storage.googleapis.com:443


openssl x509 -text -in /etc/ssl/certs/ca-certificates.crt –noout
openssl s_client -showcerts -host storage.googleapis.com -port 443
```

```
check expiration date
check_ssl_expire(){
  listDomains=$1
  DATE=$(date '+%Y-%m-%d %H:%M:%S')
#  EC2_AVAIL_ZONE=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
#  EC2_REGION="`echo \"$EC2_AVAIL_ZONE\" | sed 's/[a-z]$//'`"
#  MODULE=$(hostname | cut -c5-7)
  OUTPUT="date:${DATE}"
  for domain in ${listDomains}; do
    result=$(echo | timeout 10 openssl s_client -connect $domain 2>/dev/null | openssl x509 -noout -enddate | cut -d "=" -f2)
    domain=$(echo ${domain} | sed 's/:.*//')
    expireTime=$(date -d" $result" +%s)
    nowDayTime=$(date +%s)

    remainDay=`expr \( $expireTime - $nowDayTime \) / \( 3600 \* 24 \)`
    OUTPUT="${OUTPUT}|${domain}:${remainDay}"
  done
  echo ${OUTPUT} >> ${LOG_PATH}/check_ssl_expire.log
}

run_check(){
  check_ssl_expire "ipa.sre.com:443 ipa-admin.sre.com:443 ipa-kibana.sre.com:443 ipa-logstash.sre.com:5044 ipa-client.sre.com:443 tag.sre.com:443"
}
```
Neu co loi thi fix
`check certs folder cua openssl version -d`
