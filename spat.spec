#
# Spat spec file
#
Summary: A simple messageing client.
Name: spat
Version: 1.0 
Release: 1
Copyright: Codehost.com, Inc. 
Group: Applications/Networking
Source: http://spat.codehost.com/spat-1.0.src.tar.gz
URL: http://spat.codehost.com
Vendor: Codehost.com, Inc.
Packager: Jess Mahan <jess@codehost.com>

%description
Spat! is a lightweight, GNOME compliant messaging application designed 
and distributed by Codehost.com, Inc.  This instant messaging system was 
developed to easily install and run on a TCP/IP network.

%prep
rm -rf $RPM_BUILD_DIR/spat-1.0
zcat $RPM_BUILD_DIR/spat-1.0.src.tar.gz | tar -xvf -

%build
cd spat-1.0
./configure
make 

%install
cd spat-1.0
make install
if [ ! -d /usr/share/gnome/apps/Intranet/ ]
then mkdir /usr/share/gnome/apps/Intranet 
fi
if [ ! -d /usr/share/applets/Intranet/ ]
then mkdir /usr/share/applets/Intranet
fi
cp -f Intranet.directory /usr/share/gnome/apps/Intranet/.directory
cp -f spat.desktop /usr/share/gnome/apps/Intranet
cp -f Intranet.directory /usr/share/applets/Intranet/.directory
cp -f spatd.desktop /usr/share/applets/Intranet
cp -f spatd.gnorba /etc/CORBA/servers/
cp -f pixmaps/gnome-intranet.png /usr/share/pixmaps
cp -f pixmaps/spat.png /usr/share/pixmaps

%files
%doc spat-1.0/doc/FAQ
%doc spat-1.0/doc/INSTALL

/etc/CORBA/servers/spatd.gnorba
/usr/local/bin/spat
/usr/local/bin/spatd
/usr/share/gnome/apps/Intranet/.directory
/usr/share/gnome/apps/Intranet/spat.desktop
/usr/share/applets/Intranet/.directory
/usr/share/applets/Intranet/spatd.desktop
/usr/share/pixmaps/gnome-intranet.png
/usr/share/pixmaps/spat.png
/usr/share/pixmaps/spat/about.jpg
/usr/share/pixmaps/spat/away_with_msg.png
/usr/share/pixmaps/spat/ok.png
