Summary:	Content creation tools for Palm users
Summary(pl):	Program do konwersji tekstu z/do formatów Palm OS
Name:		pyrite-publisher
Version:	2.1.0
Release:	0
Source0:	http://www.pyrite.org/dist/%{name}-%{version}.tar.gz
License:	BSD-like (see docs)
Group:		Development/Libraries
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Vendor:		Rob Tillotson <rob@pyrite.org>
Url:		http://www.pyrite.org/

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

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
