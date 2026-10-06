pkgname = "arduino-cli"
pkgver = "1.6.0"
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
sha256 = "d513a9fbac5a30e63dde600d3e44e3376d68a7e2c11e9c692c1afa9b479479b4"
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
