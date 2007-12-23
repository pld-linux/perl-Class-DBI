#
# Conditional build:
%bcond_with	tests	# perform "make test". needs MySQL server
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	DBI
Summary:	Class::DBI - simple database abstraction
Summary(pl.UTF-8):	Class::DBI - prosta abstrakcja bazodanowa
Name:		perl-Class-DBI
Version:	3.0.17
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-v%{version}.tar.gz
# Source0-md5:	df59962bab98a0d31bf1d04d7270831b
URL:		http://search.cpan.org/dist/Class-DBI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor >= 0.18
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-Date-Simple
BuildRequires:	perl-Ima-DBI >= 0.33-2
BuildRequires:	perl-UNIVERSAL-moniker >= 0.06
%endif
Requires:	perl-Class-Accessor => 0.18
Requires:	perl-Class-Data-Inheritable => 0.02
Requires:	perl-Ima-DBI => 0.30
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI provides a convenient abstraction layer to a database.

It not only provides a simple database to object mapping layer, but
can be used to implement several higher order database functions
(triggers, referential integrity, cascading delete etc.), at the
application level, rather than at the database.

%description -l pl.UTF-8
Class::DBI udostępnia wygodny poziom abstrakcji w dostępie do bazy
danych.

Udostępnia nie tylko prostą warstwę mapowania bazy na obiekt, ale może
także zostać użyty do zaimplementowania ważniejszych funkcji
bazodanowych (triggery, integralność referencyjna, kaskadowe usuwanie
itp.) na poziomie aplikacji, nie bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-v%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Class/DBI/Plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Class/DBI.pm
%{perl_vendorlib}/Class/DBI
%{_mandir}/man3/*
