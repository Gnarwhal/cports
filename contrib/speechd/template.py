pkgname = "speechd"
pkgver = "0.11.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-espeak-ng",
    "--without-baratinoo",
    "--without-flite",
    "--without-ibmtts",
    "--without-kali",
    "--without-voxin",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "espeak-ng-devel",
    "glib-devel",
    "libdotconf-devel",
    "libpulse-devel",
    "libsndfile-devel",
]
depends = ["python-pyxdg"]
pkgdesc = "High level interface to speech synthesis"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/brailcom/speechd"
source = f"{url}/releases/download/{pkgver}/speech-dispatcher-{pkgver}.tar.gz"
sha256 = "1ce4759ffabbaf1aeb433a5ec0739be0676e9bdfbae9444a7b3be1b2af3ec12b"
# strcasestr
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}


@subpackage("speechd-devel")
def _devel(self):
    return self.default_devel()
