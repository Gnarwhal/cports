pkgname = "livekit"
pkgver = "1.13.3"
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
sha256 = "9cb7e2664757ad1e15deb3de49d854df4435390f9e49597040b61ff7ba0ded4e"
# requires network
options = ["!check"]


def install(self):
    self.install_bin(self.cwd / self.make_dir / "server", name="livekit-server")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "livekit")
