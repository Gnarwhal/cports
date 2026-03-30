pkgname = "lk-jwt-service"
pkgver = "0.5.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Service to issue LiveKit JWTs for MatrixRTC"
license = "AGPL-3.0-or-later"
url = "https://github.com/element-hq/lk-jwt-service"
source = f"https://github.com/element-hq/lk-jwt-service/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "db3e2fa8be9df3d5620bc57697c5dffb83d470eb5b58f3f12906e8c63ea5eeff"


def post_install(self):
    self.install_license("LICENSE")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "lk-jwt-service")
