cat <<EOF > /root/build.sh
#!/bin/sh
# Requirements

yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum-config-manager --enable epel

yum install -y libmicrohttpd-devel jansson-devel \
   openssl-devel libsrtp-devel sofia-sip-devel glib2-devel \
   opus-devel libogg-devel libcurl-devel pkgconfig gengetopt \
   libconfig-devel libtool autoconf automake git  libnice-devel \
   cmake3 libunwind-devel golang cmake doxygen graphviz gengetopt \
   lua lua-devel

yum groupinstall "Development tools" -y

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


#  Janus
cd
git clone https://github.com/meetecho/janus-gateway.git
cd janus-gateway
## Checkout v0.9.4 
git checkout v0.9.4
sh autogen.sh 
./configure --prefix=/opt/janus --enable-boringssl --enable-dtls-settimeout --enable-docs --enable-plugin-lua --disable-plugin-sip --disable-websockets
make && make install
EOF