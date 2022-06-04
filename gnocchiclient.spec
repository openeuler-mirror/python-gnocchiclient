%global _empty_manifest_terminate_build 0
%global common_desc \
	gnocchiclient Python bindings to the Gnocchi APIThis is a client for Gnocchi \
	API
Name:           python-gnocchiclient
Version:        7.0.5
Release:        2
Summary:        Python client library for Gnocchi
License:        Apache-2.0
URL:            http://gnocchi.xyz/gnocchiclient
Source0:        https://files.pythonhosted.org/packages/9d/c8/1a254fb7128ed90d5b8f29d1f06fe18319d6c9ce83068379020394c52e98/gnocchiclient-%{version}.tar.gz
BuildArch:      noarch
%description
%{common_desc}

%package -n python3-gnocchiclient
Summary:        Python client library for Gnocchi
Provides:       python-gnocchiclient
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# General requires
BuildRequires:  python3-cliff
BuildRequires:  python3-ujson
BuildRequires:  python3-keystoneauth1
BuildRequires:  python3-six
BuildRequires:  python3-futurist
BuildRequires:  python3-iso8601
BuildRequires:  python3-monotonic
BuildRequires:  python3-dateutil
BuildRequires:  python3-debtcollector
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-osc-lib
# Tests running requires
BuildRequires:  python3-openstackclient
BuildRequires:  python3-pytest
#BuildRequires:  python3-pytest-xdist
# General requires
Requires:       python3-pbr
Requires:       python3-cliff
Requires:       python3-ujson
Requires:       python3-keystoneauth1
Requires:       python3-six
Requires:       python3-futurist
Requires:       python3-iso8601
Requires:       python3-monotonic
Requires:       python3-dateutil
Requires:       python3-debtcollector
Requires:       python3-sphinx
Requires:       python3-sphinx_rtd_theme
Requires:       python3-osc-lib

%description -n python3-gnocchiclient
%{common_desc}

%package help
Summary:        Python client library for Gnocchi
Provides:       python3-gnocchiclient-doc
%description help
%{common_desc}

%prep
%autosetup -n gnocchiclient-%{version}

%build
%py3_build


%install
%py3_install
install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
# %{__python3} setup.py test

%files -n python3-gnocchiclient -f filelist.lst
%dir %{python3_sitelib}/*


%files help -f doclist.lst
%{_docdir}/*

%changelog
* Mon May 30 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 7.0.5-2
- fix build issue

* Mon Nov 08 2021 OpenStack_SIG <openstack@openeuler.org> - 7.0.5-1
- Downgrade package python3-gnocchiclient to version 7.0.5-1

* Tue Jul 20 2021 OpenStack_SIG <openstack@openeuler.org> - 7.0.6-1
- Package Spec generate
