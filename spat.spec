Summary:	A simple messaging client
Summary(pl):	Prosty klient komunikowania siê
Name:		spat
Version:	1.0
Release:	1
License:	GPL
Vendor:		Codehost.com, Inc.
Group:		X11/Applications/Networking
Source0:	http://spat.codehost.com/%{name}-%{version}.src.tar.gz
URL:		http://spat.codehost.com/
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Spat! is a lightweight, GNOME compliant messaging application designed
and distributed by Codehost.com, Inc. This instant messaging system
was developed to easily install and run on a TCP/IP network.

%description -l pl
Spat! jest niewielk±, zgodn± z GNOME aplikacj± napisan± i
dystrybuowan± przez Codehost.com, Inc. Ten system komunikowania siê
by³ projektowany z my¶l± o ³atwo¶ci instalacji i dzia³aniu po sieci
TCP/IP.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers \
	$RPM_BUILD_ROOT{%{_applnkdir}/Intranet,%{_datadir}/applets/Intranet}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PACKAGE_DOC_DIR=dummydoc

install Intranet.directory $RPM_BUILD_ROOT%{_applnkdir}/Intranet/.directory
install spat.desktop $RPM_BUILD_ROOT%{_applnkdir}/Intranet
install Intranet.directory $RPM_BUILD_ROOT%{_datadir}/applets/Intranet/.directory
install spatd.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Intranet
install spatd.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/CORBA/servers
install pixmaps/gnome-intranet.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
install pixmaps/spat.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

gzip -9nf doc/FAQ AUTHORS

%files
%defattr(644,root,root,755)
%doc doc/FAQ.gz AUTHORS.gz
%{_sysconfdir}/CORBA/servers/spatd.gnorba
%attr(755,root,root) %{_bindir}/spat
%attr(755,root,root) %{_bindir}/spatd
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
