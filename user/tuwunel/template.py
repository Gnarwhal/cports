pkgname = "tuwunel"
pkgver = "1.8.0"
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
sha256 = "c037a7c47c140595cf2c65e9414e4da2487d1c7f9c69ed7a22fbdb02797758c0"
# read-only file system
options = ["!check"]


def post_install(self):
    self.install_service(self.files_path / "tuwunel")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_sysusers(self.files_path / "sysusers.conf")
