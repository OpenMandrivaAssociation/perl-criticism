%define upstream_name    criticism
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl pragma to enforce coding standards and best-practices
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::String)
BuildRequires:	perl(Perl::Critic)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

Provides:	perl(criticism)

%description
This pragma enforces coding standards and promotes best-practices by
running your file through Perl::Critic before every execution. In a
production system, this usually isn't feasible because it adds a lot of
overhead at start-up. If you have a separate development environment, you
can effectively bypass the 'criticism' pragma by not installing
Perl::Critic in the production environment. If Perl::Critic can't be
loaded, then 'criticism' just fails silently.

Alternatively, the 'perlcritic' command-line (which is distributed with
Perl::Critic) can be used to analyze your files on-demand and has some
additional configuration features. And Test::Perl::Critic provides a nice
interface for analyzing files during the build process.

If you'd like to try Perl::Critic without installing anything, there is a
web-service available at the http://perlcritic.com manpage. The web-service
does not yet support all the configuration features that are available in
the native Perl::Critic API, but it should give you a good idea of what it
does. You can also invoke the perlcritic web-service from the command line
by doing an HTTP-post, such as one of these:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 656834
- rebuild for updated spec-helper

* Thu Sep 02 2010 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 575420
- adding a provides
- import perl-criticism

