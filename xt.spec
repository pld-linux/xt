Summary:	XSLT Processor in Java
Summary(pl.UTF-8):   Procesor XSLT napisany w Javie
Name:		xt
Version:	19991105
Release:	1
Vendor:		James Clark
License:	Free
Group:		Applications/Publishing/XML/Java
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
# Source0-md5:	2ac9973f7f9cb2a480af94066f89568a
URL:		http://www.jclark.com/xml/
# this is not exactly true but I'd better add this ...
BuildRequires:	unzip
Requires:	xp
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_datadir}/java/classes
%define		_jredir		%{_libdir}/jre

%description
XT is an implementation in Java of XSL Transformations. This version
of XT implements the PR-xslt-19991008 version of XSLT.

%description -l pl.UTF-8
XT to implementacja XSLT napisana w Javie. Ta wersja XT implementuje
XSLT w wersji PR-xslt-19991008.

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
chmod -R a+rX *

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install %{name}.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copying.txt demo *.htm
%{_javaclassdir}/*
