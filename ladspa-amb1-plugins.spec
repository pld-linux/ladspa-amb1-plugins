Summary:	AMB1 (third order ambisonics) LADSPA plugins
Summary(pl.UTF-8):	Wtyczki LADSPA AMB1 (dźwięku trójwymiarowego)
Name:		ladspa-amb1-plugins
Version:	0.3.0
Release:	1
License:	GPL v3+
Group:		Applications/Sound
Source0:	http://kokkinizita.linuxaudio.org/linuxaudio/downloads/AMB1-plugins-%{version}.tar.bz2
# Source0-md5:	eb030ca34e8923b825e97ac25b370226
Patch0:		%{name}-make.patch
URL:		http://kokkinizita.linuxaudio.org/linuxaudio/ladspa/index.html
BuildRequires:	ladspa-devel
BuildRequires:	libstdc++-devel
Requires:	ladspa-common
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/ladspa

%description
AMB1 (third order ambisonics) LADSPA plugins.

%description -l pl.UTF-8
Wtyczki LADSPA AMB1 (dźwięku trójwymiarowego).

%prep
%setup -q -n AMB1-plugins-%{version}
%patch0 -p1

%build
CPPFLAGS="%{rpmcppflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C source \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ladspa

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT \
	LADSPA_LIB_DIR=%{_libdir}/ladspa

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/ladspa/hoa1tools.so
