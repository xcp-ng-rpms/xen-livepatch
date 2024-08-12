%global package_speccommit b92536e7e4c4c02336fb63c2b97584414e3ca08c
%global usver 4
%global xsver 1
%global xsrel %{xsver}%{?xscount}%{?xshash}
%global TO_VER_REL 4.17.4-6.xs8

Name: xen-livepatch
Summary: Live patches for Xen
Version: 4
Release: %{?xsrel}%{?dist}

Group: System Environment/Hypervisor
License: GPLv2
Source0: build-livepatches

# Sources for each base
Source10: series-4.17.4-1.xs8
Source11: series-4.17.4-2.xs8
Source12: series-4.17.4-3.xs8
Source13: series-4.17.4-4.xs8
Source14: series-4.17.4-5.xs8
Source15: xsa458.patch
# EndSources

BuildRequires: livepatch-build-tools >= 20240223-1

# BuildRequires for each base
BuildRequires: xen-lp-devel_4.17.4_1.xs8
BuildRequires: xen-lp-devel_4.17.4_2.xs8
BuildRequires: xen-lp-devel_4.17.4_3.xs8
BuildRequires: xen-lp-devel_4.17.4_4.xs8
BuildRequires: xen-lp-devel_4.17.4_5.xs8
# EndBuildRequires

# Provides for each live patch
Provides: livepatch(component/xen/base/4.17.4-1.xs8/to/4.17.4-6.xs8/base-buildid/0fb03584fd8735317754448cc995bba40efeec0b)
Provides: livepatch(component/xen/base/4.17.4-2.xs8/to/4.17.4-6.xs8/base-buildid/ebe415a18be34e73a45a4901121dee2729c8f860)
Provides: livepatch(component/xen/base/4.17.4-3.xs8/to/4.17.4-6.xs8/base-buildid/c09c5c4f62dbc94f6ad2ccba07a04123b34b8c22)
Provides: livepatch(component/xen/base/4.17.4-4.xs8/to/4.17.4-6.xs8/base-buildid/219ffc93c66cafcf3908f24279bc7c94670d8df3)
Provides: livepatch(component/xen/base/4.17.4-5.xs8/to/4.17.4-6.xs8/base-buildid/45d3d436b1ac9e107aa20268cf3414130a839321)
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
* Mon Jul  8 2024 Andrew Cooper <andrew.cooper3@citrix.com> - 4-1
- Livepatch for:
    - XSA-458 CVE-2024-31143
  against Xen bases:
    - 4.17.4-1
    - 4.17.4-2
    - 4.17.4-3
    - 4.17.4-4
    - 4.17.4-5

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
