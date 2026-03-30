pkgname = "livekit"
pkgver = "1.13.11"
pkgrel = 0
build_style = "go"
make_build_args = ["./cmd/server"]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Multi-user conferencing based on WebRTC"
license = "Apache-2.0"
url = "https://livekit.com"
source = (
    f"https://github.com/livekit/livekit/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c8d9b7ba9d66c8b5f314a438c0c2493815e7e70085e37706b888cab3c4ab8f8d"
# requires network
options = ["!check"]


def install(self):
    self.install_bin(self.cwd / self.make_dir / "server", name="livekit-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "livekit")
