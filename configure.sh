cat <<EOF > /root/build.sh
#!/bin/sh
# Requirements

yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum-config-manager --enable epel

yum install -y jansson-devel gnutls-devel libgcrypt-devel\
   openssl-devel libsrtp-devel sofia-sip-devel glib2-devel \
   opus-devel libogg-devel libcurl-devel pkgconfig gengetopt \
   libconfig-devel libtool autoconf automake git  libnice-devel \
   cmake3 libunwind-devel golang cmake doxygen graphviz gengetopt \
   lua lua-devel nginx

yum groupinstall "Development tools" -y

yum-builddep libmicrohttpd libmicrohttpd-devel libnice-devel -y

# Libsrtp
#old
cd
wget https://github.com/cisco/libsrtp/archive/v1.5.4.tar.gz
tar xfv v1.5.4.tar.gz
cd libsrtp-1.5.4
./configure --prefix=/usr --enable-openssl --enable-nss --libdir=/usr/lib64
make shared_library && make install
# recent
cd
wget https://github.com/cisco/libsrtp/archive/v2.2.0.tar.gz
tar xfv v2.2.0.tar.gz
cd libsrtp-2.2.0
./configure --prefix=/usr --enable-openssl --enable-nss --libdir=/usr/lib64
make shared_library &&  make install


# Boringssl
cd
git clone https://boringssl.googlesource.com/boringssl
cd boringssl
sed -i s/" -Werror"//g CMakeLists.txt
mkdir -p build
cd build
cmake3 -DCMAKE_CXX_FLAGS="-lrt" ..
make
cd ..
mkdir -p /opt/boringssl
cp -R include /opt/boringssl/
mkdir -p /opt/boringssl/lib
cp build/ssl/libssl.a /opt/boringssl/lib/
cp build/crypto/libcrypto.a /opt/boringssl/lib/

# usrtcp
cd
git clone https://github.com/sctplab/usrsctp
cd usrsctp
./bootstrap
./configure --prefix=/usr && make && make install

# libwebsockets
cd
git clone https://libwebsockets.org/repo/libwebsockets
cd libwebsockets
git checkout v2.4-stable
mkdir build
cd build
cmake -DLWS_MAX_SMP=1 -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_C_FLAGS="-fpic" ..
make && make install

# mqtt
cd
git clone https://github.com/eclipse/paho.mqtt.c.git
cd paho.mqtt.c
make && make install

# RabbitMQ
cd
git clone https://github.com/alanxz/rabbitmq-c
cd rabbitmq-c
git submodule init
git submodule update
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ..
make &&  make install

# Sofia sip
cd
wget https://pilotfiber.dl.sourceforge.net/project/sofia-sip/sofia-sip/1.12.11/sofia-sip-1.12.11.tar.gz
tar xf sofia-sip-1.12.11.tar.gz
cd sofia-sip-1.12.11
./configure
make && make install

# Librmicrohttpd
cd
yumdownloader --source  libmicrohttpd libmicrohttpd-doc libmicrohttpd-devel
cd /root/rpmbuild/SPECS
rpm -ivh ./libmicrohttpd-0.9.33-2.amzn2.0.2.src.rpm
cd /root/rpmbuild/SPECS
wget  https://mirror.cedia.org.ec/gnu/libmicrohttpd/libmicrohttpd-0.9.70.tar.gz -O /root/rpmbuild/SOURCES/libmicrohttpd-0.9.70.tar.gz
sed -i 's/0.9.33/0.9.70/g' libmicrohttpd.spec
sed -i 's/-tutorial.info/\*/g' libmicrohttpd.spec 
rpmbuild -bp libmicrohttpd.spec
rpmbuild -ba libmicrohttpd.spec
rpm -i /root/rpmbuild/RPMS/x86_64/libmicrohttpd-0.9.70-2.amzn2.0.2.x86_64.rpm
rpm -i /root/rpmbuild/RPMS/x86_64/libmicrohttpd-devel-0.9.70-2.amzn2.0.2.x86_64.rpm

#Libnice
yumdownloader --source libnice-devel
rpm -ivh ./libnice-0.1.3-4.amzn2.0.1.src.rpm
cd /root/rpmbuild/SPECS
sed -i 's/0.1.3/0.1.16/g' libnice.spec
wget https://libnice.freedesktop.org/releases/libnice-0.1.16.tar.gz  -O /root/rpmbuild/SOURCES/libnice-0.1.16.tar.gz
rpmbuild -bp libnice.spec
rpmbuild -ba libnice.spec
rpm -i /root/rpmbuild/RPMS/x86_64/libnice-0.1.16-4.amzn2.0.1.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libnice-devel-0.1.16-4.amzn2.0.1.x86_64.rpm


#  Janus
cd
git clone https://github.com/meetecho/janus-gateway.git
cd janus-gateway
## Checkout v0.9.5
git checkout v0.9.5
sh autogen.sh 
./configure --prefix=/opt/janus --enable-boringssl --enable-dtls-settimeout --enable-docs --enable-plugin-lua --disable-plugin-sip --disable-websockets --enable-rest --disable-mqtt --disable-rabbitmq
make && make install && make configs
EOF

cat <<EOF > /etc/systemd/system/janus.service
[Unit]
Description=Janus WebRTC Server
After=network.target

[Service]
Type=simple
ExecStart=/opt/janus/bin/janus  -C /opt/janus/etc/janus/janus.jcfg -A -L /tmp/janus.log
Restart=on-abnormal
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
EOF

cat <<EOF > /etc/nginx/conf.d/janus.conf
server {
    server_name janus.libreservices.host;
    root /root/janus-gateway/html;
    listen 80;
    location / {
    }  
    location /janus {
        proxy_pass http://localhost:8088/janus;
    }
    location /admin {
        proxy_pass http://localhost:7088/admin;
    }  
}
EOF

cat <<EOF > /root/configure.sh
#!/bin/sh
#Enable admin api
sed -i "s/admin_http = false/admin_http = true/g" /opt/janus/etc/janus/janus.transport.http.jcfg
#sed -i "s/8088/80/g" /opt/janus/etc/janus/janus.transport.http.jcfg

myip=$(curl ifconfig.co/ip -s)
sed -i "s/#stun_server/stun_server/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#stun_port/stun_port/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#rtp_port_range/rtp_port_range/g" /opt/janus/etc/janus/janus.jcfg
sed -i "s/#nat_1_1_mapping = \"1.2.3.4\"/nat_1_1_mapping = \"$myip\"/g" /opt/janus/etc/janus/janus.jcfg
systemctl --system daemon-reload
systemctl enable janus.service
systemctl start janus.service
systemctl start nginx
rsync -r /root/janus-gateway/html/ /usr/share/nginx/html/
EOF