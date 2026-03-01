pkgname = "git-pages"
pkgver = "0.9.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Static site server for use with Git forges"
license = "0BSD"
url = "https://codeberg.org/git-pages/git-pages"
source = f"https://codeberg.org/git-pages/git-pages/archive/v{pkgver}.tar.gz"
sha256 = "6d86eff26ed036ac77a136e7f4c2a31cd7f1860af97eed7bd0b2b2202114acd2"


def post_install(self):
    self.install_service(self.files_path / "git-pages")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
