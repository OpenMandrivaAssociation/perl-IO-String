%define modname	IO-String
%define modver	1.08

Summary:	A Perl module to read from strings
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
IO::String is an IO::File (and IO::Handle) compatible class that read or
write data from in-core strings.  It is really just a simplification of
what I needed from Eryq's IO-stringy modules.  As such IO::String is a
replacement for IO::Scalar.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/IO
%{_mandir}/man3/IO::String.3pm*

