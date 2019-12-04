#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OpenSSL-ECDSA
Summary:	Crypt::OpenSSL::ECDSA - Perl extension for OpenSSL ECDSA (Elliptic Curve Digital Signature Algorithm)
Summary(pl.UTF-8):	Crypt::OpenSSL::ECDSA - implementacja algorytmu ECDSA w Perlu
Name:		perl-Crypt-OpenSSL-ECDSA
Version:	0.07
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ee0afce54f5a2bfc47b336a7400eca2
Patch0:		Crypt-OpenSSL-ECDSA-0.08-Port-to-OpenSSL-1.1.0.patch
URL:		http://search.cpan.org/dist/Crypt-OpenSSL-ECDSA/
BuildRequires:	openssl-devel >= 0.9.8a
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-OpenSSL-EC >= 1.01
%endif
Requires:	perl-Crypt-OpenSSL-EC >= 1.01
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an interface to the ECDSA (Elliptic Curve Digital
Signature Algorithm) functions in OpenSSL. Tested against OpenSSL 1.0.2

%description -l pl.UTF-8
Ten moduł dostarcza interfejs do funkcji implementujących algorytm
ECDSA z biblioteki OpenSSL. Testowane z OpenSSLem w wersji 1.0.2.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/OpenSSL/ECDSA.pm
%dir %{perl_vendorarch}/auto/Crypt/OpenSSL/ECDSA
%{perl_vendorarch}/auto/Crypt/OpenSSL/ECDSA/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/OpenSSL/ECDSA/ECDSA.so
%{_mandir}/man3/Crypt::OpenSSL::ECDSA.3pm*
