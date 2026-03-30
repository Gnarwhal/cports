pkgname = "livekit"
pkgver = "1.13.10"
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
sha256 = "d1b93ced314b14654faceeb99627a79114b8ebe002bb5d620be4a185db83a4b2"
# requires network
options = ["!check"]


def install(self):
    self.install_bin(self.cwd / self.make_dir / "server", name="livekit-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "livekit")
