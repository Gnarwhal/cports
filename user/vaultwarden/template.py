pkgname = "vaultwarden"
pkgver = "1.37.4"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--features",
    "postgresql sqlite s3",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "postgresql16-client-devel",
    "sqlite-devel",
    "zstd-devel",
]
pkgdesc = "Password manager"
license = "AGPL-3.0-or-later"
url = "https://vaultwarden.com"
source = f"https://github.com/dani-garcia/vaultwarden/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d31a3ef5456619cfe424f0586f4ecadd186e22513a93bbeab6bc2f09cda803a7"


def post_install(self):
    self.install_license("LICENSE.txt")
