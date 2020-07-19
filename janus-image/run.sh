#!/bin/bash
# Defaults
readonly rtp_ports="20000-40000"
readonly admin_token="janusoverlord"
readonly token="mytoken"

#Enable admin api and network settings
sed -i "s/admin_http = false/admin_http = true/g" /opt/janus/etc/janus/janus.transport.http.jcfg
curl ifconfig.co/ip -s > publicip
myip=$(cat publicip)
#FIXME own stun
sed -i "s/#stun_server/stun_server/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#stun_port/stun_port/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#rtp_port_range/rtp_port_range/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#nat_1_1_mapping = \"1.2.3.4\"/nat_1_1_mapping = \"$myip\"/g" /opt/janus/etc/janus/janus.jcfg

# CHANGEME port from parameter
sed -i "s/20000-40000/$rtp_ports/g" /opt/janus/etc/janus/janus.*

# Run
screen -S janus -d -m
screen -r janus -X stuff $'/opt/janus/bin/janus -C /opt/janus/etc/janus/janus.jcfg -A -L /tmp/janus.log\n'

# CHANGEME tokens from parameter
curl -4 --retry 5 --retry-connrefused --retry-max-time 30 -X POST localhost:7088/admin/ --data '{"admin_secret": "'"$admin_token"'","transaction": "FromLocalhost","janus": "add_token","token": "'"$token"'"}'
tail -F /tmp/janus.log