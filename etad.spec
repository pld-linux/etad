Summary:	Power management software for ETA UPS
Summary(pl):	Program zarz±dzaj±cy zasilaczami UPS firmy ETA.
Name:		etad
Version:	1.0
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.eta.com.pl/download/%{name}-%{version}.tar.gz
Source1:	%{name}.init
Source2:	%{name}.config
Patch0:		%{name}.patch
URL:		http://www.eta.com.pl/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
UPS power management under Linux for ETA Products. It allows your
computer/server to run during power problems for a specified length of
time or the life of the batteries in your UPS and then properly
executes a controlled shutdown during an extended power failure.

%description -l pl
Program zarz±dzaj±cy zasialaczami UPS firmy ETA. Umo¿liwia on pracê
komputera w trakcie problemów z zasilaniem przez okre¶lony czas z
jednoczesn± kontrol± stanu na³adowania baterii, a nastêpnie
przeprowadza kontrolowane wy³±cznie systemu w razie przed³u¿aj±cej siê
awarii zasilania.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},/etc/sysconfig,/etc/rc.d/init.d}

install etad do_haltnow $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/etad
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/etad

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
%chkconfig_add

%preun
%chkconfig_del

%files
%defattr(644,root,root,755)
%doc README
%doc manual.html
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %config(noreplace) /etc/sysconfig/etad
%attr(754,root,root) /etc/rc.d/init.d/etad
