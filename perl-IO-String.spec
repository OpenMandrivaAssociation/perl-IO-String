%define real_name	IO-String
%define name		perl-%{real_name}
%define version		1.08
%define release		%mkrel 2

Summary:	A Perl module to read from strings
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Requires:	perl
BuildRequires:	perl-devel
Buildroot:	%{_tmppath}/%{name}-root
URL:		http://search.cpan.org/dist/%{real_name}/
Source:		http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{real_name}-%{version}.tar.bz2
BuildArch:	noarch

%description
IO::String is an IO::File (and IO::Handle) compatible class that read or
write data from in-core strings.  It is really just a simplification of
what I needed from Eryq's IO-stringy modules.  As such IO::String is a
replacement for IO::Scalar.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/IO
%_mandir/man3/IO::String.3pm*

