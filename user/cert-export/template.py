pkgname = "cert-export"
pkgver = "0.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["dinit-chimera"]
pkgdesc = "Export certs from caddy for use with other applications"
license = "MIT"
url = "https://forge.monodon.me/Gnarwhal/cert-export"
source = (
    f"https://forge.monodon.me/Gnarwhal/cert-export/archive/v{pkgver}.tar.gz"
)
sha256 = "54fb922b09fa5a0a18bfc2f3e957e883c54fbb8b4e32f1c4aa5235fdfcc7420a"


def post_install(self):
    from cbuild.util import cargo

    self.install_license("LICENSE")

    self.install_completion(
        cargo.target_path(self, "completions/cert-export.bash"), "bash"
    )
    self.install_completion(
        cargo.target_path(self, "completions/_cert-export"), "zsh"
    )
    self.install_completion(
        cargo.target_path(self, "completions/cert-export.fish"), "fish"
    )

    self.install_service(self.files_path / "cert-export")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_file("config.example.toml", "usr/share/examples/cert-export")
