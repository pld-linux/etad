Summary:	Power management software for ETA UPS
Summary(pl.UTF-8):   Program zarządzający zasilaczami UPS firmy ETA
Name:		etad
Version:	1.0
Release:	1
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.eta.com.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	0e9c2b96a24153ad23bf0c2c7680dbd5
Source1:	%{name}.init
Source2:	%{name}.config
Patch0:		%{name}.patch
URL:		http://www.eta.com.pl/
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UPS power management under Linux for ETA Products. It allows your
computer/server to run during power problems for a specified length of
time or the life of the batteries in your UPS and then properly
executes a controlled shutdown during an extended power failure.

%description -l pl.UTF-8
Program zarządzający zasilaczami UPS firmy ETA. Umożliwia on pracę
komputera w trakcie problemów z zasilaniem przez określony czas z
jednoczesną kontrolą stanu naładowania baterii, a następnie
przeprowadza kontrolowane wyłącznie systemu w razie przedłużającej się
awarii zasilania.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig,/etc/rc.d/init.d}

install etad do_haltnow $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/etad
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/etad

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add etad

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del etad
fi

%files
%defattr(644,root,root,755)
%doc README manual.html
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/etad
%attr(754,root,root) /etc/rc.d/init.d/etad
