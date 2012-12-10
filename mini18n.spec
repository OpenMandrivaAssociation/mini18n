%define major		0
%define lib_name	%mklibname mini18n %{major}
%define devel_name	%mklibname mini18n -d


Name:		mini18n
Version:	0.1
Release:	3
Summary:	A translation library
#License:	LGPLv2+
#strange license
#it was already distributed with yabause under GPLv2+
License:	GPLv2+
Group:		System/Libraries
URL:		http://yabause.sourceforge.net/
Source0:	http://downloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz

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
%makeinstall

%files -n %{lib_name}
%doc AUTHORS ChangeLog README example/{main.c,Makefile*}
%{_libdir}/*.so.*

%files -n %{devel_name}
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so


%changelog
* Mon Aug 01 2011 Andrey Bondrov <abondrov@mandriva.org> 0.1-2mdv2012.0
+ Revision: 692652
- imported package mini18n


* Sat Jan 17 2009 Guillaume Bedot <littletux@zarb.org> 0.1-1mdv2009.1
- First package of mini18n for PLF
