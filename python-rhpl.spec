Summary: Library of Python code used by installation and configuration tools
Name: python-rhpl
Version: 0.212
Release: %mkrel 1
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
Conflicts: kudzu < 1.2.0, hwdata < 0.169
Conflicts: wireless-tools < 28-0.pre8.5
Conflicts: kbd < 1.12-21

%description
The rhpl package contains Python code used throughout the system.

%prep
%setup -q -n rhpl-%{version}

%build
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang rhpl

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rhpl.lang
%defattr(-,root,root)
%doc README COPYING
%{python_sitearch}/rhpl

