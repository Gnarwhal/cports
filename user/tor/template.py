pkgname = "tor"
pkgver = "0.4.9.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-gpl",
]
hostmakedepends = [
    "asciidoc",
    "automake",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "libevent-devel",
    "openssl3-devel",
    "xz-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
checkdepends = [
    "bash",
]
pkgdesc = "Anonymizing overlay network"
license = "BSD-3-Clause"
url = "https://gitlab.com/torproject/tor"
source = f"{url}/-/archive/tor-{pkgver}/tor-tor-{pkgver}.tar.gz"
sha256 = "56c5687b19ff8437718ab34271c84e2ddee8948bdc8e46bf1d5751e676a125f0"


def post_install(self):
    self.install_file("src/config/torrc.sample.in", "etc/tor", name="torrc")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "tor")
    self.install_license("LICENSE")
