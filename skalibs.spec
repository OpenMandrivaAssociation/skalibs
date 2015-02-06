%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	The skarnet.org development library
Name:		skalibs
Version:	0.47
Release:	4
License:	BSD
Group:		Development/Other
Url:		http://www.skarnet.org/software/skalibs/
Source0:	http://www.skarnet.org/software/%{name}/%{name}-%{version}.tar.gz

%description
skalibs is a package centralizing the public-domain C
development files used for building other skarnet.org software.

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for skalibs
Group:		Development/C

%description devel
skalibs is a package centralizing the public-domain C
development files used for building other skarnet.org software.

skalibs can also be used as a sound basic start for C
development.  There are a lot of general-purpose libraries out
there; but if your main goal is to produce small and secure C
code, you will like skalibs.

skalibs contains exclusively public-domain code.  So you can
redistribute it as you want, and it does not prevent you from
distributing any of your executables.

%files devel
%doc %{name}-%{version}/package/CHANGES
%doc %{name}-%{version}/package/README
%doc %{name}-%{version}/doc/*.html
%dir %{_includedir}/%{name}
%dir %{_libdir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}/*.a

#----------------------------------------------------------------------------

%prep
%setup -q -n prog

%build
pushd %{name}-%{version}
    package/compile
popd

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_includedir}/%{name}

pushd %{name}-%{version}
    for i in `cat package/include` ;  do
        install -m 0755 include/$i %{buildroot}%{_includedir}/%{name}/
    done

    for i in `cat package/library` ;  do
        install -m 0755 library/$i %{buildroot}%{_libdir}/%{name}/
    done
popd

