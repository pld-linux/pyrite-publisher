%include	/usr/lib/rpm/macros.python
Summary:	Content creation tools for Palm users
Summary(pl):	Program do konwersji tekstu z/do formatów Palm OS
Name:		pyrite-publisher
Version:	2.1.1
Release:	1
License:	BSD-like (see docs)
Vendor:		Rob Tillotson <rob@pyrite.org>
Group:		Development/Libraries
Source0:	http://www.pyrite.org/dist/%{name}-%{version}.tar.gz
# Source0-md5:	c468ededf9439228ffe9312e2475e50d
URL:		http://www.pyrite.org/
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python-modules
Requires:	python >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc *.pdb

%description
Pyrite Publisher is a content conversion tool for Palm Computing
Platform users. Or to put it more simply, Pyrite Publisher takes
information in a common format like HTML and converts it to something
you can use on your Palm organizer.

%description -l pl
Pyrite Publisher jest programem do konwersji tekstów dla u¿ytkowników
komputerów z Palm OS. Albo, wyra¿aj±c siê pro¶ciej, Pyrite Publisher
pozwala przekszta³ciæ informacje w zwyk³ym formacie takim jak HTML na
co¶, co mo¿na czytaæ na organizerach z Palm OS.

%prep
%setup -q

%build
env CFLAGS="%{rpmcflags}" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
install -D doc/pyrpub.1 $RPM_BUILD_ROOT%{_mandir}/man1/pyrpub.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.* doc/*.pdb doc/pyrite-publisher/*
%attr(755,root,root) %{_bindir}/pyrpub
%dir %{py_sitedir}/PyritePublisher
%attr(755,root,root) %{py_sitedir}/PyritePublisher/*.so
%{py_sitedir}/PyritePublisher/*.pyc
%{_mandir}/man1/*
