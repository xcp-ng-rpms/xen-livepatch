%global package_speccommit a7fdf1873f75cc14c5c867936323c20d82b3dff0
%global package_srccommit v1.0.1

%global TO_VER_REL 10.18.xs8

Name: xen-livepatch
Summary: Live patches for Xen
Version: 1.0.1
Release: 1%{?xsrel}%{?dist}

Group: System Environment/Hypervisor
License: GPLv2
Source0: xen-livepatch-1.0.1.tar.gz

BuildRequires: livepatch-build-tools
BuildRequires: elfutils

# BuildRequires for each base
# END

%description
Contains live patches to be applied against various Xen versions.


%prep
%autosetup -p1


%build
./build-livepatches %{TO_VER_REL}


%install
install -d -m 755 "%{buildroot}/usr/lib/xen-livepatch"

if ls out/* > /dev/null 2>&1; then
    for lp in out/*/*.livepatch; do
        chmod 755 "${lp}"
        ln -sf "$(basename ${lp})" "$(dirname ${lp})/livepatch.livepatch"
    done

    mv out/* "%{buildroot}/usr/lib/xen-livepatch"
fi


%files
%defattr(-,root,root)
%{_usr}/lib/xen-livepatch


%changelog
* Wed Jul 20 2022 Ming Lu <ming.lu@citrix.com> - 1.0.1-1
- Initial release

* Mon Nov 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.0-1
- Initial packaging
