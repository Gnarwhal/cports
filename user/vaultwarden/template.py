pkgname = "vaultwarden"
pkgver = "1.37.5"
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
sha256 = "6be37dcc95b91a058ecbe614f1a7acff68ca8d23dc2c016cec18517c7173e4cc"


def post_install(self):
    self.install_license("LICENSE.txt")
