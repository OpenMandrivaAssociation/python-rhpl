Summary:	Library of Python code used by installation and configuration tools
Name:		python-rhpl
Version:	0.212
Release:	9
Source0:	rhpl-%{version}.tar.bz2
License:	GPLv2+
Group:		Development/Python
Provides:	rhpl = %{version}-%{release}
BuildRequires:	gettext
BuildRequires:	python-devel
%ifnarch s390 s390x
BuildRequires:	libiw-devel
%endif
Conflicts:	kudzu < 1.2.0
# FIXME: we provide this in ldetect-lst, but unversioned
#Conflicts: hwdata < 0.169
Conflicts:	wireless-tools < 28-0.pre8.5
# FIXME: we provide this version, but not sure about the release
#Conflicts: kbd < 1.12-21

%description
The rhpl package contains Python code used throughout the system.

%prep
%setup -q -n rhpl-%{version}

%build
%make


%install
%makeinstall_std

%find_lang rhpl

%files -f rhpl.lang
%defattr(-,root,root)
%doc README COPYING
%{python_sitearch}/rhpl
