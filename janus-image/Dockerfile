FROM amazonlinux:2

LABEL maintainer="Docker <paul@kristianpaul.org>"

RUN set -x \
    && yum install yum-utils wget -y \
    && yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum-config-manager --enable epel\
    && yum install -y jansson-devel gnutls-devel libgcrypt-devel\
    openssl-devel libsrtp-devel sofia-sip-devel glib2-devel \
    opus-devel libogg-devel libcurl-devel pkgconfig gengetopt \
    libconfig-devel libtool autoconf automake git  libnice-devel \
    cmake3 libunwind-devel golang cmake doxygen graphviz gengetopt \
    lua-devel nginx\
    && yum groupinstall "Development tools" -y\
    && yum-builddep libmicrohttpd libmicrohttpd-devel libnice-devel -y\
    && cd\
    && wget https://github.com/cisco/libsrtp/archive/v1.5.4.tar.gz\
    && tar xfv v1.5.4.tar.gz\
    && cd libsrtp-1.5.4\
    && ./configure --prefix=/usr --enable-openssl --enable-nss --libdir=/usr/lib64\
    && make shared_library && make install\
    && cd\
    && wget https://github.com/cisco/libsrtp/archive/v2.2.0.tar.gz\
    && tar xfv v2.2.0.tar.gz\
    && cd libsrtp-2.2.0\
    && ./configure --prefix=/usr --enable-openssl --enable-nss --libdir=/usr/lib64\
    && make shared_library &&  make install\
    && cd\
    && git clone https://boringssl.googlesource.com/boringssl\
    && cd boringssl\
    && sed -i s/" -Werror"//g CMakeLists.txt\
    && mkdir -p build\
    && cd build\
    && cmake3 -DCMAKE_CXX_FLAGS="-lrt" ..\
    && make\
    && cd ..\
    && mkdir -p /opt/boringssl\
    && cp -R include /opt/boringssl/\
    && mkdir -p /opt/boringssl/lib\
    && cp build/ssl/libssl.a /opt/boringssl/lib/\
    && cp build/crypto/libcrypto.a /opt/boringssl/lib/\
    && cd\
    && git clone https://github.com/sctplab/usrsctp\
    && cd usrsctp\
    && ./bootstrap\
    && ./configure --prefix=/usr && make && make install\
    && cd\
    && git clone https://libwebsockets.org/repo/libwebsockets\
    && cd libwebsockets\
    && git checkout v2.4-stable\
    && mkdir build\
    && cd build\
    && cmake -DLWS_MAX_SMP=1 -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_C_FLAGS="-fpic" ..\
    && make && make install\
    && cd\
    && git clone https://github.com/eclipse/paho.mqtt.c.git\
    && cd paho.mqtt.c\
    && make && make install\
    && cd\
    && git clone https://github.com/alanxz/rabbitmq-c\
    && cd rabbitmq-c\
    && git submodule init\
    && git submodule update\
    && mkdir build && cd build\
    && cmake -DCMAKE_INSTALL_PREFIX=/usr ..\
    && make &&  make install\
    && cd\
    && wget https://pilotfiber.dl.sourceforge.net/project/sofia-sip/sofia-sip/1.12.11/sofia-sip-1.12.11.tar.gz\
    && tar xf sofia-sip-1.12.11.tar.gz\
    && cd sofia-sip-1.12.11\
    && ./configure\
    && make && make install\
    && cd\
    && yumdownloader --source  libmicrohttpd libmicrohttpd-doc libmicrohttpd-devel\
    && rpm -ivh ./libmicrohttpd-0.9.33-2.amzn2.0.2.src.rpm\
    && cd /root/rpmbuild/SPECS\
    && wget  https://mirror.cedia.org.ec/gnu/libmicrohttpd/libmicrohttpd-0.9.70.tar.gz -O /root/rpmbuild/SOURCES/libmicrohttpd-0.9.70.tar.gz\
    && sed -i 's/0.9.33/0.9.70/g' libmicrohttpd.spec\
    && sed -i 's/-tutorial.info/\*/g' libmicrohttpd.spec \
    && rpmbuild -bp libmicrohttpd.spec\
    && rpmbuild -ba libmicrohttpd.spec\
    && rpm -i /root/rpmbuild/RPMS/x86_64/libmicrohttpd-0.9.70-2.amzn2.0.2.x86_64.rpm\
    && rpm -i /root/rpmbuild/RPMS/x86_64/libmicrohttpd-devel-0.9.70-2.amzn2.0.2.x86_64.rpm\
    && yumdownloader --source libnice-devel\
    && rpm -ivh ./libnice-0.1.3-4.amzn2.0.1.src.rpm\
    && cd /root/rpmbuild/SPECS\
    && sed -i 's/0.1.3/0.1.16/g' libnice.spec\
    && wget https://libnice.freedesktop.org/releases/libnice-0.1.16.tar.gz  -O /root/rpmbuild/SOURCES/libnice-0.1.16.tar.gz\
    && rpmbuild -bp libnice.spec\
    && rpmbuild -ba libnice.spec\
    && yum install -y /root/rpmbuild/RPMS/x86_64/libnice-*.rpm\
    && cd\
    && git clone https://github.com/meetecho/janus-gateway.git\
    && cd janus-gateway\
    && git checkout v0.9.5\
    && sh autogen.sh \
    && ./configure --prefix=/opt/janus --enable-boringssl --enable-dtls-settimeout --enable-docs --enable-plugin-lua --disable-plugin-sip --disable-websockets --enable-rest --disable-mqtt --disable-rabbitmq\
    && make && make install && make configs \
    && cd && rm -rf *

    COPY run.sh /run.sh

    EXPOSE 80 7088

    CMD  /run.sh
