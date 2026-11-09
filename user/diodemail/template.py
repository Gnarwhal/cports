pkgname = "diodemail"
pkgver = "1.1.0"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/server"]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Send-only smtp server"
license = "GPL-3.0-or-later"
url = "https://forge.monodon.me/Gnarwhal/diodemail"
source = f"https://forge.monodon.me/Gnarwhal/diodemail/archive/v{pkgver}.tar.gz"
sha256 = "91c4071df158e15905b251af692d83a78d191f637900a62d89722cba31a186ff"


def install(self):
    self.install_bin("build/server", name="diodemail")
    self.install_service(self.files_path / "diodemail")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
