%define modname	IO-String

Summary:	A Perl module to read from strings
Name:		perl-%{modname}
Version:	1.08
Release:	1
License:	GPLv2
Group:		Development/Perl
Url:		https://metacpan.org/pod/IO::String
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{modname}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

%description
IO::String is an IO::File (and IO::Handle) compatible class that read or
write data from in-core strings.  It is really just a simplification of
what I needed from Eryq's IO-stringy modules.  As such IO::String is a
replacement for IO::Scalar.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/IO
%{_mandir}/man3/IO::String.3pm*
