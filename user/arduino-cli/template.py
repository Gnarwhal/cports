pkgname = "arduino-cli"
pkgver = "1.5.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
depends = ["gcompat"]
pkgdesc = "Arduino command line tool"
license = "GPL-3.0-or-later"
url = "https://docs.arduino.cc/arduino-cl"
source = (
    f"https://github.com/arduino/arduino-cli/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "262fbe874f62677d01eb15593144ca82bd6e7c2d0c00f82aa93949ab12924de6"
# cross: uses binary for completions
options = ["!cross"]


def post_configure(self):
    self.make_build_args.append(
        f"-ldflags="
        f"-X internal/version.versionString={pkgver}"
        f" -X internal/version.commit={pkgver}"
        f" -X internal/version.date={self.source_date_epoch}"
    )


def pre_check(self):
    from cbuild.util import golang

    SKIP_TESTS = [
        "internal/integrationtest",
        "internal/version",
        # require network
        "internal/arduino/monitor",
        "internal/arduino/resources",
        "internal/cli/arguments",
    ]
    self.make_check_args = [
        test
        for test in self.do(
            "go",
            "list",
            "./...",
            capture_output=True,
            env=golang.get_go_env(self),
        )
        .stdout.decode("utf-8")
        .split("\n")
        if True not in map(lambda skip: skip in test, SKIP_TESTS)
    ]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"arduino-cli.{shell}", "w") as f:
            self.do(
                f"{self.make_dir}/arduino-cli", "completion", shell, stdout=f
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"arduino-cli.{shell}", shell)
