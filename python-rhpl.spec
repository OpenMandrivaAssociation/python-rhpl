Summary: Library of Python code used by installation and configuration tools
Name: python-rhpl
Version: 0.212
Release: %mkrel 7
Source0: rhpl-%{version}.tar.bz2
License: GPLv2+
Group: Development/Python
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Provides: rhpl = %{version}-%{release}
BuildRequires: gettext
%py_requires -d
%ifnarch s390 s390x
BuildRequires: libiw-devel
%endif
Conflicts: kudzu < 1.2.0
# FIXME: we provide this in ldetect-lst, but unversioned
#Conflicts: hwdata < 0.169
Conflicts: wireless-tools < 28-0.pre8.5
# FIXME: we provide this version, but not sure about the release
#Conflicts: kbd < 1.12-21

%description
The rhpl package contains Python code used throughout the system.

%prep
%setup -q -n rhpl-%{version}

%build
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang rhpl

%clean
rm -rf %{buildroot}

%files -f rhpl.lang
%defattr(-,root,root)
%doc README COPYING
%{python_sitearch}/rhpl

