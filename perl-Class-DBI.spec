%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI
Summary:	Class::DBI -- Simple Database Abstraction
Summary(pl):	Class::DBI -- prosta abstrakcja bazodanowa
Name:		perl-Class-DBI
Version:	0.89
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-require.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl(Class::Accessor)          => 0.16
Requires:	perl(Class::Data::Inheritable) => 0.02
Requires:	perl(Ima::DBI)                 => 0.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI provides a convenient abstraction layer to a database.

It not only provides a simple database to object mapping layer, but
can be used to implement several higher order database functions
(triggers, referential integrity, cascading delete etc.), at the
application level, rather than at the database.

%description -l pl
Class::DBI udost�pnia wygodny poziom abstrakcji w dost�pie do bazy
danych.

Udost�pnia nie tylko prost� warstw� mapowania bazy na obiekt, ale mo�e
tak�e zosta� u�yty do zaimplementowania wa�niejszych funkcji
bazodanowych (triggery, integralno�� referencyjna, kaskadowe usuwanie
itp.) na poziomie aplikacji, nie bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
