#
# Spat spec file
#
Summary:	A simple messageing client.
Name:		spat
Version:	1.0 
Release:	1
Copyright:	Codehost.com, Inc. 
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://spat.codehost.com/%{name}-%{version}.src.tar.gz
URL:		http://spat.codehost.com
Vendor:		Codehost.com, Inc.

%description
Spat! is a lightweight, GNOME compliant messaging application designed
and distributed by Codehost.com, Inc. This instant messaging system
was developed to easily install and run on a TCP/IP network.

%prep
rm -rf $RPM_BUILD_DIR/spat-1.0
zcat $RPM_BUILD_DIR/spat-1.0.src.tar.gz | tar -xvf -

%build
cd spat-1.0
./configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
cd spat-1.0
%{__make} install
if [ ! -d %{_applnkdir}/Intranet/ ]
then mkdir %{_applnkdir}/Intranet 
fi
if [ ! -d %{_datadir}/applets/Intranet/ ]
then mkdir %{_datadir}/applets/Intranet
fi
cp -f Intranet.directory %{_applnkdir}/Intranet/.directory
cp -f spat.desktop %{_applnkdir}/Intranet
cp -f Intranet.directory %{_datadir}/applets/Intranet/.directory
cp -f spatd.desktop %{_datadir}/applets/Intranet
cp -f spatd.gnorba %{_sysconfdir}/CORBA/servers/
cp -f pixmaps/gnome-intranet.png %{_datadir}/pixmaps
cp -f pixmaps/spat.png %{_datadir}/pixmaps

%files
%defattr(644,root,root,755)
%doc spat-1.0/doc/FAQ
%doc spat-1.0/doc/INSTALL

%{_sysconfdir}/CORBA/servers/spatd.gnorba
%{_prefix}/local/bin/spat
%{_prefix}/local/bin/spatd
%{_applnkdir}/Intranet/.directory
%{_applnkdir}/Intranet/spat.desktop
%{_datadir}/applets/Intranet/.directory
%{_datadir}/applets/Intranet/spatd.desktop
%{_datadir}/pixmaps/gnome-intranet.png
%{_datadir}/pixmaps/spat.png
%{_datadir}/pixmaps/spat/about.jpg
%{_datadir}/pixmaps/spat/away_with_msg.png
%{_datadir}/pixmaps/spat/ok.png

%clean
rm -rf $RPM_BUILD_ROOT
