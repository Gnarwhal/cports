pkgname = "forgejo-runner"
pkgver = "12.13.0"
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
sha256 = "8df4c2f5ce6b5736e23568e27e27069155d6dc186e9fa383fd2ef1fc744f5525"
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
