Summary: nethserver-docker install docker
%define name nethserver-docker
Name: %{name}
%define version 0.1.0
%define release 1
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Requires: docker-ce
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Docker containers and tooling make building and shipping applications dramatically easier and faster.

%changelog
* Tue May 09 2017 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post
%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%config(noreplace) /etc/yum.repos.d/docker-ce.repo
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING
