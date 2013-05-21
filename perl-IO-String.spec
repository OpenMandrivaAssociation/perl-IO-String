%define upstream_name	 IO-String
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A Perl module to read from strings
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
IO::String is an IO::File (and IO::Handle) compatible class that read or
write data from in-core strings.  It is really just a simplification of
what I needed from Eryq's IO-stringy modules.  As such IO::String is a
replacement for IO::Scalar.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-4mdv2012.0
+ Revision: 765373
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-3
+ Revision: 763875
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.80.0-2
+ Revision: 676761
- rebuild

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 407787
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2009.0
+ Revision: 241560
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-2mdv2008.0
+ Revision: 86510
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode bz2 extension


* Mon Dec 12 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.08-1mdk
- 1.08

* Wed Oct 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.07-1mdk
- 1.07
- Fix URL, change summary

* Tue Sep 27 2005 Olivier Thauvin <nanardon@mandriva.org> 1.06-2mdk
- rebuild
- update url

* Tue Nov 09 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.06-1mdk
- 1.06

* Wed Apr 21 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.05-1mdk
- 1.05

* Sun Feb 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.04-1mdk
- 1.04
- perl 5.8.3 rebuild

* Thu Jan 08 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.03-1mdk
- 1.03
- perl 5.8.2 rebuild

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.02-5mdk
- Use %%makeinstall_std now that it works on klama
- Remove bad build options and don't use the %%make
  macro for test.

* Sat Aug 02 2003 Ben Reser <ben@reser.org> 1.02-4mdk
- Forgot DESTDIR on %%makeinstall

* Fri Aug 01 2003 Ben Reser <ben@reser.org> 1.02-3mdk
- Fix install for new perl
- Macrofication
- Fix man path
- unpackaged perllocal.pod

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.02-2mdk
- rebuild for new auto{prov,req}

* Fri Dec 27 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.02-1mdk
- 1.02

* Fri Nov 01 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.01-1mdk 
- first version of rpm.

