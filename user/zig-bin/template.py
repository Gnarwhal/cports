pkgname = "zig-bin"
pkgver = "0.17.0"
pkgrel = 0
depends = ["!zig"]
pkgdesc = "Zig programming language"
license = "MIT"
url = "https://ziglang.org"
source = (
    f"https://ziglang.org/download/{pkgver}/zig-x86_64-linux-{pkgver}.tar.xz"
)
sha256 = "1cbe9df9f27e6b78d14ccbca43b6703a404ef79ef1c463de901d7f088d4e2026"


def install(self):
    self.install_license("LICENSE")
    self.install_bin("zig")
    self.cp(
        "lib",
        self.destdir / "usr/lib/zig",
        recursive=True,
    )
