Name:			mini18n
Version:		0.1
Release:		%mkrel 2

%define major		0
%define lib_name	%mklibname mini18n %{major}
%define devel_name	%mklibname mini18n -d

Summary:	A translation library
#License:	LGPLv2+
#strange license
#it was already distributed with yabause under GPLv2+
License:	GPLv2+
Group:		System/Libraries
URL:		http://yabause.sourceforge.net/
Source0:	http://downloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Mini18n is a small library to translate applications across multiple 
platforms.

%package -n %{lib_name}
Summary:	A small translation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{lib_name}
Library and data files for the mini18n package.

%package -n %{devel_name}
Summary:	Header files and static library from mini18n
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	mini18n-devel < %{version}-%{release}
Requires:	%{lib_name} = %{version}

%description -n	%{devel_name}
Library and includes files for developing programs translated with mini18n.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README example/{main.c,Makefile*}
%{_libdir}/*.so.*

%files -n %{devel_name}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so

