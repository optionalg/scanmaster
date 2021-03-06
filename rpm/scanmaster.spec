%define name		scanmaster
%define release		1
%define version 	3.3.0
%define mybuilddir	%{_builddir}/%{name}-%{version}-root

BuildArch:		noarch
BuildRoot:		%{mybuilddir}
Summary:		the scanmaster suite of scripts
License: 		BSD
Name: 			%{name}
Version: 		%{version}
Release: 		%{release}
Source: 		%{name}-%{version}.tar.gz
Prefix: 		/usr
Group: 			Development/Tools

Requires:		expect python

%description
scanmaster is a set of scripts that allow you to ssh to a very large
number of hosts in parallel to run an arbitrary script on the remote side.
It works best if the scans can take advantage of a set of scanslave nodes
with access to shared NFS space, though that is not a hard requirement.

This is an admittedly poor RPM. Fixes and corrections would be most
welcome.

%prep
%setup -q

%build
mkdir -p %{mybuilddir}/usr/local/bin
mkdir -p %{mybuilddir}/usr/local/share/man/man1
mkdir -p %{mybuilddir}/usr/local/share/scanmaster/helpers

%install
install -c -m 555 src/autopw %{mybuilddir}/usr/local/bin/autopw
install -c -m 555 src/checkhosts %{mybuilddir}/usr/local/bin/checkhosts
install -c -m 555 src/scanhosts %{mybuilddir}/usr/local/bin/scanhosts
install -c -m 555 src/scanmaster %{mybuilddir}/usr/local/bin/scanmaster
install -c -m 555 src/scanslave %{mybuilddir}/usr/local/bin/scanslave
install -c -m 555 src/tkill.py %{mybuilddir}/usr/local/bin/tkill

install -c -m 555 helpers/generic-aggregator %{mybuilddir}/usr/local/share/scanmaster/helpers/generic-aggregator
install -c -m 555 helpers/generic-post %{mybuilddir}/usr/local/share/scanmaster/helpers/generic-post

install -c -m 444 doc/autopw.1 %{mybuilddir}/usr/local/share/man/man1/autopw.1
install -c -m 444 doc/checkhosts.1 %{mybuilddir}/usr/local/share/man/man1/checkhosts.1
install -c -m 444 doc/scanhosts.1 %{mybuilddir}/usr/local/share/man/man1/scanhosts.1
install -c -m 444 doc/scanmaster.1 %{mybuilddir}/usr/local/share/man/man1/scanmaster.1
install -c -m 444 doc/scanslave.1 %{mybuilddir}/usr/local/share/man/man1/scanslave.1
install -c -m 444 doc/tkill.1 %{mybuilddir}/usr/local/share/man/man1/tkill.1

install -c -m 444 CHANGES %{mybuilddir}/usr/local/share/scanmaster/CHANGES
install -c -m 444 LICENSE %{mybuilddir}/usr/local/share/scanmaster/LICENSE
install -c -m 444 README %{mybuilddir}/usr/local/share/scanmaster/README

%files
%defattr(0444,root,root)
%attr(0555,root,root) /usr/local/bin/autopw
%attr(0555,root,root) /usr/local/bin/checkhosts
%attr(0555,root,root) /usr/local/bin/scanhosts
%attr(0555,root,root) /usr/local/bin/scanmaster
%attr(0555,root,root) /usr/local/bin/scanslave
%attr(0555,root,root) /usr/local/bin/tkill

%attr(0555,root,root) /usr/local/share/scanmaster/helpers/generic-aggregator
%attr(0555,root,root) /usr/local/share/scanmaster/helpers/generic-post

%doc /usr/local/share/man/man1/autopw.1
%doc /usr/local/share/man/man1/checkhosts.1
%doc /usr/local/share/man/man1/scanhosts.1
%doc /usr/local/share/man/man1/scanmaster.1
%doc /usr/local/share/man/man1/scanslave.1
%doc /usr/local/share/man/man1/tkill.1

%doc /usr/local/share/scanmaster/CHANGES
%doc /usr/local/share/scanmaster/LICENSE
%doc /usr/local/share/scanmaster/README
