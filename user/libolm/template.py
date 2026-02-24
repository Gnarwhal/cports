pkgname = "libolm"
pkgver = "3.2.16"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "Implementation of the olm and megolm cryptographic ratchets"
license = "Apache-2.0"
url = "https://gitlab.matrix.org/matrix-org/olm"
source = f"{url}/-/archive/{pkgver}/olm-{pkgver}.tar.gz"
sha256 = "1e90f9891009965fd064be747616da46b232086fe270b77605ec9bda34272a68"


@subpackage("libolm-devel")
def _(self):
    return self.default_devel()
