#!/bin/sh
#Enable admin api
sed -i "s/admin_http = false/admin_http = true/g" /opt/janus/etc/janus/janus.transport.http.jcfg
#sed -i "s/8088/80/g" /opt/janus/etc/janus/janus.transport.http.jcfg

curl ifconfig.co/ip -s > publicip
myip=\$(cat publicip)
sed -i "s/#stun_server/stun_server/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#stun_port/stun_port/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#rtp_port_range/rtp_port_range/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#nat_1_1_mapping = \"1.2.3.4\"/nat_1_1_mapping = \"$myip\"/g" /opt/janus/etc/janus/janus.jcfg
systemctl --system daemon-reload
systemctl enable janus.service
systemctl start janus.service
/bin/cp /root/janus.conf /etc/nginx/conf.d/janus.conf
systemctl restart nginx
cd /usr/share/nginx/html/ && rsync -r /root/janus-gateway/html/* .
chmod  0755 /usr/share/nginx/html
chmod  0644 /usr/share/nginx/html/*
#Fix demo to work with API REST token
sed -i 's/:8088//g' *.js
sed -i 's/:8089//g' *.js
sed -i 's/\/\/\s*token/token/g' echotest.js
sleep 30
curl -X POST localhost:7088/admin/ --data '{"admin_secret": "janusoverlord","transaction": "FromLocalhost","janus": "add_token","token": "mytoken"}'