pkgname = "forgejo-runner"
pkgver = "13.2.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X code.forgejo.org/forgejo/runner/v11/internal/pkg/ver.version=v{pkgver}"
]
make_check_args = [
    "-skip",
    "Test_runCreateRunnerFile|Test_ping",
    "./...",
]
hostmakedepends = ["go"]
makedepends = ["dinit-chimera", "podman-dinit"]
depends = ["podman"]
pkgdesc = "Daemon that runs CI jobs for Forgejo"
license = "MIT"
url = "https://code.forgejo.org/forgejo/runner"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "c5596ecdf5336b5c4777109a373ba675130324104618ce34952f28682a44c948"
# requires docker containers
options = ["!check"]


def install(self):
    self.install_bin(
        f"{self.cwd}/{self.make_dir}/runner", name="forgejo-runner"
    )
    self.install_file(
        self.files_path / "docker_host.env", "usr/share/forgejo-runner"
    )
    self.install_service(self.files_path / "forgejo-runner")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_license("LICENSE")
