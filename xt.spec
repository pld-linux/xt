# TODO
# - try building it
Summary:	XSLT Processor in Java
Summary(pl.UTF-8):	Procesor XSLT napisany w Javie
Name:		xt
Version:	19991105
Release:	2
Vendor:		James Clark
License:	Free
Group:		Applications/Publishing/XML/Java
Source0:	ftp://ftp.jclark.com/pub/xml/%{name}.zip
# Source0-md5:	2ac9973f7f9cb2a480af94066f89568a
URL:		http://www.jclark.com/xml/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	xp
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XT is an implementation in Java of XSL Transformations. This version
of XT implements the PR-xslt-19991008 version of XSLT.

%description -l pl.UTF-8
XT to implementacja XSLT napisana w Javie. Ta wersja XT implementuje
XSLT w wersji PR-xslt-19991008.

%package demo
Summary:	Demo for %{name}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu %{name}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%prep
%setup -qc

%if 0
%build
required_jars="sax jaxp_parser_impl jaxp_transform_impl servlet"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
%javac -source 1.4 $(find com -name '*.java')
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
# jars
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc copying.txt *.htm
%{_javadir}/*.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
%endif
