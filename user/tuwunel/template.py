pkgname = "tuwunel"
pkgver = "2.0.0"
pkgrel = 0
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
source = f"https://github.com/matrix-construct/tuwunel/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2244077e5a9edbf328256bda30797fcd04cf8556da24ae57cb598cbe075f9196"
# read-only file system
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "tuwunel")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
