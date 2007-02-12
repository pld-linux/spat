Summary:	A simple messaging client
Summary(pl.UTF-8):	Prosty klient komunikowania się
Name:		spat
Version:	1.0
Release:	1
License:	GPL
Vendor:		Codehost.com, Inc.
Group:		X11/Applications/Networking
Source0:	http://spat.codehost.com/%{name}-%{version}.src.tar.gz
# Source0-md5:	25b81ab1d7430ea93fef91a9151d0069
URL:		http://spat.codehost.com/
BuildRequires:	gnome-core-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spat! is a lightweight, GNOME compliant messaging application designed
and distributed by Codehost.com, Inc. This instant messaging system
was developed to easily install and run on a TCP/IP network.

%description -l pl.UTF-8
Spat! jest niewielką, zgodną z GNOME aplikacją napisaną i
dystrybuowaną przez Codehost.com, Inc. Ten system komunikowania się
był projektowany z myślą o łatwości instalacji i działaniu po sieci
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
install pixmaps/gnome-intranet.png $RPM_BUILD_ROOT%{_pixmapsdir}
install pixmaps/spat.png $RPM_BUILD_ROOT%{_pixmapsdir}

%files
%defattr(644,root,root,755)
%doc doc/FAQ AUTHORS
%{_sysconfdir}/CORBA/servers/spatd.gnorba
%attr(755,root,root) %{_bindir}/spat
%attr(755,root,root) %{_bindir}/spatd
%{_applnkdir}/Intranet/.directory
%{_applnkdir}/Intranet/spat.desktop
%{_datadir}/applets/Intranet/.directory
%{_datadir}/applets/Intranet/spatd.desktop
%{_pixmapsdir}/gnome-intranet.png
%{_pixmapsdir}/spat.png
%{_pixmapsdir}/spat/about.jpg
%{_pixmapsdir}/spat/away_with_msg.png
%{_pixmapsdir}/spat/ok.png

%clean
rm -rf $RPM_BUILD_ROOT
