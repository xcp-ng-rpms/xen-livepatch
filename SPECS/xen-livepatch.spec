%global package_speccommit 0b8358186f35a0d39dc3261e54177121892b1bfb
%global usver 2.0
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global TO_VER_REL 10.18.xs8

Name: xen-livepatch
Summary: Live patches for Xen
Version: 2.0
Release: %{?xsrel}%{?dist}

Group: System Environment/Hypervisor
License: GPLv2
Source0: build-livepatches

# Sources for each base
# EndSources

BuildRequires: livepatch-build-tools

# BuildRequires for each base
# EndBuildRequires

# Provides for each live patch
# EndProvides

%description
Contains live patches to be applied against various Xen versions.


%build

BUILD_LIVEPATCHES="%{SOURCE0}"

PQDIR=%{_sourcedir} $BUILD_LIVEPATCHES %{TO_VER_REL}


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
* Mon Dec 4 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 2.0-1
- Merge infrastructure to simplify builds

* Wed Jul 20 2022 Ming Lu <ming.lu@citrix.com> - 1.0.1-1
- Initial release

* Mon Nov 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.0-1
- Initial packaging
