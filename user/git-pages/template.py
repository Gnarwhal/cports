pkgname = "git-pages"
pkgver = "0.10.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
makedepends = ["dinit-chimera"]
pkgdesc = "Static site server for use with Git forges"
license = "0BSD"
url = "https://codeberg.org/git-pages/git-pages"
source = f"https://codeberg.org/git-pages/git-pages/archive/v{pkgver}.tar.gz"
sha256 = "667b141c7865a416c790bdddeb545072bfd857b78fb7df4e85bdee4385bbc1f9"


def post_install(self):
    self.install_service(self.files_path / "git-pages")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
