%global package_speccommit 872357f7394c681f39181845c7146169e3cfbf78
%global usver 3
%global xsver 3
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global TO_VER_REL 4.17.3-3.xs8

Name: xen-livepatch
Summary: Live patches for Xen
Version: 3
Release: %{?xsrel}%{?dist}

Group: System Environment/Hypervisor
License: GPLv2
Source0: build-livepatches

# Sources for each base
Source10: series-4.17.3-1.xs8
Source11: series-4.17.3-2.xs8
Source12: xsa451-4.17.patch
Source13: cmp-legacy-in-max-policy.patch
# EndSources

BuildRequires: livepatch-build-tools >= 20240223-1

# BuildRequires for each base
BuildRequires: xen-lp-devel_4.17.3_1.xs8
BuildRequires: xen-lp-devel_4.17.3_2.xs8
# EndBuildRequires

# Provides for each live patch
Provides: livepatch(component/xen/base/4.17.3-1.xs8/to/4.17.3-3.xs8/base-buildid/133ed818bb68ac1a3341c9318dfdd3f118c5ba7d)
Provides: livepatch(component/xen/base/4.17.3-2.xs8/to/4.17.3-3.xs8/base-buildid/29eb4d131192552316819179cb39cecfa323c163)
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
* Mon Feb 26 2024 Roger Pau Monné <roger.pau@citrix.com> - 3-3
- Use a non-vetoing hook.

* Fri Feb 23 2024 Andrew Cooper <andrew.cooper3@citrix.com> - 3-2
- Rebuild against the correct version of livepatch-build-tools

* Fri Feb 23 2024 Andrew Cooper <andrew.cooper3@citrix.com> - 3-1
- Livepatch for:
    - XSA-451 CVE-2023-46841
    - Migration issue with VMs that previously saw CMP_LEGACY
  against Xen bases:
    - 4.17.3-1
    - 4.17.3-2

* Wed Jan 31 2024 Roger Pau Monné <roger.pau@citrix.com> - 2.0-2
- Bump max patch filename to 128.

* Mon Dec 4 2023 Andrew Cooper <andrew.cooper3@citrix.com> - 2.0-1
- Merge infrastructure to simplify builds

* Wed Jul 20 2022 Ming Lu <ming.lu@citrix.com> - 1.0.1-1
- Initial release

* Mon Nov 29 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.0.0-1
- Initial packaging
