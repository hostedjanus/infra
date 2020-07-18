#!/bin/bash
#Enable admin api
sed -i "s/admin_http = false/admin_http = true/g" /opt/janus/etc/janus/janus.transport.http.jcfg
curl ifconfig.co/ip -s > publicip
myip=\$(cat publicip)
sed -i "s/#stun_server/stun_server/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#stun_port/stun_port/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#rtp_port_range/rtp_port_range/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#nat_1_1_mapping = \"1.2.3.4\"/nat_1_1_mapping = \"$myip\"/g" /opt/janus/etc/janus/janus.jcfg
