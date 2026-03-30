pkgname = "livekit"
pkgver = "1.13.7"
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
sha256 = "b42f34b095dff22639a40256c3f98fd563fdbce5d497e449ceb06ee010de88c5"
# requires network
options = ["!check"]


def install(self):
    self.install_bin(self.cwd / self.make_dir / "server", name="livekit-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "livekit")
