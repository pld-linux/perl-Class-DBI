%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI
Summary:	Class::DBI - simple database abstraction
Summary(pl):	Class::DBI - prosta abstrakcja bazodanowa
Name:		perl-Class-DBI
Version:	0.93
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cd7324478efa0a568bfcf72fbd1b3b6a
Patch0:		%{name}-require.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
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
Class::DBI udostêpnia wygodny poziom abstrakcji w dostêpie do bazy
danych.

Udostêpnia nie tylko prost± warstwê mapowania bazy na obiekt, ale mo¿e
tak¿e zostaæ u¿yty do zaimplementowania wa¿niejszych funkcji
bazodanowych (triggery, integralno¶æ referencyjna, kaskadowe usuwanie
itp.) na poziomie aplikacji, nie bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
