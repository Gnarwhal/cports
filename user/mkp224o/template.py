pkgname = "mkp224o"
pkgver = "1.7.0"
pkgrel = 0
build_style = "gnu_configure"
make_check_target = "test"
hostmakedepends = [
    "automake",
]
makedepends = [
    "libsodium-devel",
]
pkgdesc = "Vanity address generator for ed25519 onion services"
license = "CC0-1.0"
url = "https://github.com/cathugger/mkp224o"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e7bda8517206a1786d97c793a2b7ad91be88e73ed2e7d9aad986f3bd5e3fdb5e"
hardening = ["cfi", "vis"]


def install(self):
    self.install_bin("build/mkp224o")
