pkgname = "tuwunel"
pkgver = "1.9.2"
pkgrel = 1
build_wrksrc = "./src/main"
build_style = "cargo"
make_install_args = ["--frozen"]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
    "rust-bindgen",
    "rust-rustfmt",
]
makedepends = [
    "dinit-chimera",
    "liburing-devel",
    "linux-headers",
    "zstd-devel",
]
pkgdesc = "Matrix homeserver"
license = "Apache-2.0"
url = "https://matrix-construct.github.io/tuwunel"
# source = f"https://github.com/matrix-construct/tuwunel/archive/refs/tags/v{pkgver}.tar.gz"
source = (
    "https://github.com/matrix-construct/tuwunel/archive/refs/heads/main.tar.gz"
)
sha256 = "806826debd06dc01d9c709dafe60b680492a670f41a1dd0149cf681ff5111b36"
# read-only file system
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "tuwunel")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
