pkgname = "mautrix-discord"
pkgver = "0.7.7"
pkgrel = 0
_gitrev = "19e26674e6624a02bced982aafe845cb20e43827"
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.Tag=v{pkgver} -X main.Commit={_gitrev}",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "libolm-devel"]
pkgdesc = "Matrix bridge for discord"
license = "AGPL-3.0-or-later"
url = "https://go.mau.fi/mautrix-discord"
source = (
    f"https://github.com/mautrix/discord/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b44840d152e0775d9804927300353ef165e386cd6723dca0bb89d431dccd6bde"


def post_install(self):
    self.install_service(self.files_path / "mautrix-discord")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE")
