pkgname = "mautrix-discord"
pkgver = "0.7.6"
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
sha256 = "beff1dc0c7dec609df363fc929654295dbfa2b4660e832fea598cdf712c77936"


def post_install(self):
    self.install_service(self.files_path / "mautrix-discord")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_license("LICENSE")
