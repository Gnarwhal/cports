pkgname = "lk-jwt-service"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = [
    "dinit-chimera",
    "linux-headers",
]
pkgdesc = "Service to issue LiveKit JWTs for MatrixRTC"
license = "AGPL-3.0-or-later"
url = "https://github.com/element-hq/lk-jwt-service"
source = f"https://github.com/element-hq/lk-jwt-service/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "40c3bb24616e27bd0d2854859b593bb79f2c7832d9202b998957998d6d5ca79b"


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.44.0")


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "lk-jwt-service")
