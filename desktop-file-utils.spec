Summary: Utilities for manipulating .desktop files
Name: desktop-file-utils
Version: 0.15
Release: 9%{?dist}
URL: http://www.freedesktop.org/software/desktop-file-utils
Source0: http://www.freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Development/Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: glib2-devel >= 2.12.0
BuildRequires: emacs

%description
.desktop files are used to describe an application for inclusion in
GNOME or KDE menus.  This package contains desktop-file-validate which
checks whether a .desktop file complies with the specification at
http://www.freedesktop.org/standards/, and desktop-file-install
which installs a desktop file to the standard directory, optionally
fixing it up in the process.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README NEWS
%{_bindir}/*
%{_datadir}/emacs/site-lisp/

%changelog
* Fri May 14 2010 Ray Strode <rstrode@redhat.com> 0.15-9
- Drop prov file completely
  Resolves: #592332

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.15-8.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Richard Hughes <rhughes@redhat.com> - 0.15-6
- Panu seems to be shipping the prov file in rpmbuild. Remove it here until we
  work out where it belongs.

* Wed Feb 04 2009 Richard Hughes <rhughes@redhat.com> - 0.15-5
- Panu merged the rpm bits for this feature, but we've got a new provides
  filename. Respin this package with the new name.

* Thu Jan 22 2009 Richard Hughes <rhughes@redhat.com> - 0.15-4
- Rename desktop-mime-type.prov to desktop_mime_type.prov and add the tiny
  macros.desktop_mime_type file so that we can trivially patch rpm to enable
  this new functionality.

* Fri May 02 2008 Richard Hughes <rhughes@redhat.com> - 0.15-3
- Add desktop-mime-type.prov so that we can automatically
  generate mimetype provides for packages at build time.
  This lets us do some cool things with PackageKit in the future.

* Wed Mar 19 2008 Ray Strode <rstrode@redhat.com> - 0.15-2
- Drop old unneeded obsoletes on desktop-file-validator
(bug 225681)

* Tue Mar  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.15-1
- Update to 0.15
- Drop upstreamed patch

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.14-3
- Autorebuild for GCC 4.3

* Thu Dec  6 2007 Ray Strode <rstrode@redhat.com> 0.14-2
- make icon extension a warning not an error

* Fri Nov 30 2007 Christopher Stone <chris.stone@gmail.com> 0.14-1
- Upstream sync
- Remove no longer needed short option patch

* Wed Aug 15 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-3
- Make the -m option work (#232761)

* Mon Aug  6 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-2
- Update license field

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 0.13-1
- Update to 0.13, which features a completely rewritten validator

* Thu Mar 08 2007 Florian La Roche <laroche@redhat.com> - 0.12-4
- remove empty post/preun scripts completely

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-3
- drop some rm -f cruft
- don't call update-desktop-database from %%post or %%postun

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-2
- make --vendor optional

* Tue Nov 28 2006 Ray Strode <rstrode@redhat.com> - 0.12-1
- Update to 0.12

* Fri Oct 27 2006 Ray Strode <rstrode@redhat.com> - 0.11-4
- commit the fix attempted in 0.11-2 and 0.11-3 to the right
  function...

* Fri Oct 27 2006 Ray Strode <rstrode@redhat.com> - 0.11-3
- actually apply the patch written in 0.11-2

* Thu Oct 26 2006 Ray Strode <rstrode@redhat.com> - 0.11-2
- make desktop file validation non-fatal until we
  add support for categories beginning with X- and clean up
  our menu system to not require invalid categories
  (bug 212048)

* Mon Oct 23 2006 Matthias Clasen <mclasen@redhat.com> - 0.11-1
- Update to 0.11

* Wed Jul 26 2006 Jesse Keating <jkeating@redhat.com> - 0.10-7
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.10-6.1
- bump again for double-long bug on ppc(64)

* Fri Feb 10 2006 Ray Strode <rstrode@redhat.com> - 0.10-6
- call update-desktop-database in %%preun (bug 180898)
- don't fail if update-desktop-database fails
- don't use %%makeinstall

* Fri Feb 10 2006 Ray Strode <rstrode@redhat.com> - 0.10-5
- call update-desktop-database in %%post (bug 180898)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.10-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Jan 22 2006 Ray Strode <rstrode@redhat.com> - 0.10-4
- don't use uninitialized memory (bug 178591)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Aug 31 2005 Ray Strode <rstrode@redhat.com> - 0.10-3
- bump build requires for glib to 2.2.0 (bug #146585).

* Thu May 12 2005 Ray Strode <rstrode@redhat.com> - 0.10-2
- Add build requires for emacs (bug #141297).

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> - 0.10-1
- Update to 0.10

* Mon Oct 18 2004 Miloslav Trmac <mitr@redhat.com> - 0.9-2
- Output error message instead of assertion failure (#134934)

* Tue Sep 28 2004 Mark McLoughlin <markmc@redhat.com> 0.9-1
- Update to 0.9, remove upstreamed patches

* Mon Sep 27 2004 Ray Strode <rstrode@redhat.com> 0.8-6
- Swap if and else in egg_desktop_entries_get_locale_encoding
  to prevent allocating massive amounts of unneeded ram.

* Mon Sep 27 2004 Ray Strode <rstrode@redhat.com> 0.8-5
- Swap if and else in egg_desktop_entries_get_locale_country
  to prevent allocating massive amounts of unneeded ram.

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> 0.8-4
- Fix the fix for --remove-show-in option

* Thu Sep 23 2004 Ray Strode <rstrode@redhat.com> 0.8-3
- Fix --remove-show-in option

* Mon Sep 13 2004 Dan Williams <dcbw@redhat.com> 0.8-2
- Fix RH #131983 (annoying log message about "entries != NULL")

* Fri Sep  3 2004 Mark McLoughlin <markmc@redhat.com> 0.8-1
- Update to 0.8

* Sat Jul 31 2004 Dan Williams <dcbw@redhat.com> 0.7-1
- Update to 0.7

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Mar  1 2004 Dan Williams <dcbw@redhat.com> 0.4-2
- Fix RH #117201, initial comment fails validation
- Add in, but do not use, Frederic Crozat's freedesktop.org
    menu-spec 0.8 patch

* Thu Feb 19 2004 Mark McLoughlin <markmc@redhat.com> 0.4-1
- Update to 0.4

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Sep  3 2003 Havoc Pennington <hp@redhat.com> 0.3-10
- fix for #103276 (int/size_t issue) from twoerner

* Mon Jul  7 2003 Alexander Larsson <alexl@redhat.com> 0.3-9
- Rebuild

* Mon Jun 23 2003 Havoc Pennington <hp@redhat.com> 0.3-8
- rebuild

* Thu Jun  5 2003 Jonathan Blandford <jrb@redhat.com> 0.3-6
- Backport patch to allow @MODIFIER in locale keys

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec  6 2002 Havoc Pennington <hp@redhat.com>
- rebuild

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- fix more error messages

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- remove old symlinks before creating new ones, chills out 
  a lot of error messages

* Tue Aug  6 2002 Havoc Pennington <hp@redhat.com>
- version 0.3

* Wed Jul 24 2002 Havoc Pennington <hp@redhat.com>
- 0.2.95 cvs snap, should fix OnlyShowIn

* Mon Jul 22 2002 Havoc Pennington <hp@redhat.com>
- 0.2.94 cvs snap, adds --print-available

* Tue Jul  9 2002 Havoc Pennington <hp@redhat.com>
- 0.2.93 cvs snap with a crash fixed, and corrects [KDE Desktop Entry]

* Fri Jun 21 2002 Havoc Pennington <hp@redhat.com>
- 0.2.92 cvs snap with --remove-key and checking for OnlyShowIn
  and missing trailing semicolons on string lists

* Fri Jun 21 2002 Havoc Pennington <hp@redhat.com>
- 0.2.91 cvs snap with --copy-name-to-generic-name and
  --copy-generic-name-to-name

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 0.2.90 cvs snap with --delete-original fixed

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 0.2

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 09 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu May  9 2002 Havoc Pennington <hp@redhat.com>
- initial build
