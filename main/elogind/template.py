pkgname = "elogind"
pkgver = "246.10"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dman=true",
    "-Drootlibexecdir=/usr/libexec/elogind",
    "-Dhalt-path=/usr/bin/halt",
    "-Dreboot-path=/usr/bin/reboot",
    "-Dcgroup-controller=elogind",
    "-Ddefault-hierarchy=unified",
    "-Ddefault-kill-user-processes=false",
    "-Dutmp=false",
]
hostmakedepends = [
    "meson", "docbook-xsl-nons", "gettext-tiny", "gperf", "xsltproc",
    "bsdm4", "pkgconf", "shadow"
]
makedepends = [
    "acl-devel", "eudev-devel", "gettext-tiny-devel", "libcap-devel",
    "libseccomp-devel", "linux-pam-devel"
]
checkdepends = ["bash"]
pkgdesc = "Standalone version of logind"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/elogind/elogind"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c490dc158c8f5bca8d00ecfcc7ad5af24d1c7b9e59990a0b3b1323996221a922"

# TODO: service

def post_install(self):
    # compat symlinks
    self.install_link("libelogind.pc", "usr/lib/pkgconfig/libsystemd.pc")
    self.install_link(
        "libelogind.pc", "usr/lib/pkgconfig/libsystemd-logind.pc"
    )
    self.install_link("elogind", "usr/include/systemd")
    # extra includes
    self.install_file("src/systemd/sd-id128.h", "usr/include")
    self.install_file("src/systemd/_sd-common.h", "usr/include")
    # wrapper
    self.install_file(
        self.files_path / "elogind.wrapper", "usr/libexec/elogind",
        mode = 0o755
    )

@subpackage("elogind-devel")
def _devel(self):
    return self.default_devel(man = True)

@subpackage("libelogind")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (library)"
    return self.default_libs()
