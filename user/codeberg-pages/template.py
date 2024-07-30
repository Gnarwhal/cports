pkgname = "codeberg-pages"
pkgver = "6.4"
pkgrel = 0
build_style = "go"
make_check_args = [
    "-skip",
    # Requires network connection
    "TestHandlerPerformance",
]
hostmakedepends = ["go"]
makedepends = [
    "dinit-chimera",
    "sqlite-devel",
]
go_build_tags = [
    "libsqlite3",
    "sqlite",
    "sqlite_unlock_notify",
]
pkgdesc = "Serve static pages from Gitea/Forgejo repositories"
license = "EUPL-1.2"
url = "https://docs.codeberg.org/codeberg-pages"
source = f"https://codeberg.org/Codeberg/pages-server/archive/v{pkgver}.tar.gz"
sha256 = "9d5e1990ee9fcc04edd7cb9f62d20bb676cec53337f1f413bd55cc16ac7c2d59"
env = {}

if self.profile().arch == "riscv64":
    # https://github.com/golang/go/issues/64875
    env["CGO_ENABLED"] = "1"


def post_install(self):
    self.install_bin("build/pages", name="codeberg-pages")
    self.install_license("LICENSE")

    self.install_file(self.files_path / "envfile", "usr/share/codeberg-pages")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "codeberg-pages")
