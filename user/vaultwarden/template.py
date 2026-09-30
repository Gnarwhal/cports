pkgname = "vaultwarden"
pkgver = "1.37.3"
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
sha256 = "64a3cd2117e82f226c01a9eb2d3a59b5629b527438d1f9cd0a85c9883c7a9b39"


def post_install(self):
    self.install_license("LICENSE.txt")
