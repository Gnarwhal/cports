pkgname = "kanidm"
pkgver = "1.11.2"
pkgrel = 0
build_style = "cargo"
make_env = {
    "KANIDM_BUILD_PROFILE": "release_linux",
}
make_build_args = [
    "--features",
    "tpm,unix",
    "--package",
    "daemon",
    "--package",
    "kanidm-ipa-sync",
    "--package",
    "kanidm_tools",
    "--package",
    "kanidm_unix_int",
    "--package",
    "nss_kanidm",
    "--package",
    "pam_kanidm",
]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "dinit-chimera",
    "linux-pam-devel",
    "sqlite-devel",
    "tpm2-tss-devel",
    "udev-devel",
]
pkgdesc = "Identity management platform"
license = "MPL-2.0"
url = "https://kanidm.com"
source = f"https://github.com/kanidm/kanidm/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a8ed31203e5f8c036b9cb261c85ddac19291bc6ca16981495495cd9621c56529"
# too lazy to figure out
options = ["!check"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.clear_vendor_checksums(self, "aws-lc-sys-0.44.0")


def install(self):
    from cbuild.util import cargo

    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_bin(cargo.target_path(self, "kanidm"))
    self.install_completion(
        cargo.target_path(self, "build/completions/_kanidm"),
        "zsh",
        "kanidm",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidm.bash"),
        "bash",
        "kanidm",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidm.fish"),
        "fish",
        "kanidm",
    )

    self.install_bin(cargo.target_path(self, "kanidmd"))
    self.install_bin(cargo.target_path(self, "kanidm-ipa-sync"))
    self.install_completion(
        cargo.target_path(self, "build/completions/_kanidmd"),
        "zsh",
        "kanidmd",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidmd.bash"),
        "bash",
        "kanidmd",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidmd.fish"),
        "fish",
        "kanidmd",
    )
    self.install_service(self.files_path / "kanidmd")
    self.install_dir("usr/share/kanidm/ui/hpkg")
    self.cp(
        "server/core/static/*",
        self.destdir / "usr/share/kanidm/ui/hpkg",
        recursive=True,
        glob=True,
    )

    self.install_lib(
        cargo.target_path(self, "libnss_kanidm.so"),
        name="libnss_kanidm.so.2",
    )
    self.install_file(
        cargo.target_path(self, "libpam_kanidm.so"),
        "usr/lib/security",
        name="pam_kanidm.so",
    )
    self.install_bin(cargo.target_path(self, "kanidm_ssh_authorizedkeys"))
    self.install_bin(
        cargo.target_path(self, "kanidm_ssh_authorizedkeys_direct")
    )
    self.install_bin(cargo.target_path(self, "kanidm-unix"))
    self.install_bin(cargo.target_path(self, "kanidm_unixd"))
    self.install_bin(cargo.target_path(self, "kanidm_unixd_tasks"))
    self.install_completion(
        cargo.target_path(self, "build/completions/_kanidm_ssh_authorizedkeys"),
        "zsh",
        "kanidm_ssh_authorizedkeys",
    )
    self.install_completion(
        cargo.target_path(
            self, "build/completions/_kanidm_ssh_authorizedkeys_direct"
        ),
        "zsh",
        "kanidm_ssh_authorizedkeys_direct",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/_kanidm_unix"),
        "zsh",
        "kanidm-unix",
    )
    self.install_completion(
        cargo.target_path(
            self, "build/completions/kanidm_ssh_authorizedkeys.bash"
        ),
        "bash",
        "kanidm_ssh_authorizedkeys",
    )
    self.install_completion(
        cargo.target_path(
            self, "build/completions/kanidm_ssh_authorizedkeys_direct.bash"
        ),
        "bash",
        "kanidm_ssh_authorizedkeys_direct",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidm_unix.bash"),
        "bash",
        "kanidm-unix",
    )
    self.install_completion(
        cargo.target_path(
            self, "build/completions/kanidm_ssh_authorizedkeys.fish"
        ),
        "fish",
        "kanidm_ssh_authorizedkeys",
    )
    self.install_completion(
        cargo.target_path(
            self, "build/completions/kanidm_ssh_authorizedkeys_direct.fish"
        ),
        "fish",
        "kanidm_ssh_authorizedkeys_direct",
    )
    self.install_completion(
        cargo.target_path(self, "build/completions/kanidm_unix.fish"),
        "fish",
        "kanidm-unix",
    )
    self.install_service(self.files_path / "kanidm-unixd")
    self.install_service(self.files_path / "kanidm-unixd-tasks")


@subpackage("kanidm-clients")
def _(self):
    self.subdesc = "client to interact with kanidm identity management server"
    self.install_if = [self.parent]

    def install():
        self.take("cmd:kanidm")

    return install


@subpackage("kanidm-server")
def _(self):
    self.subdesc = "server for identity management"
    self.install_if = [self.parent]

    def install():
        self.take("cmd:kanidmd")
        self.take("cmd:kanidm-ipa-sync")
        self.take("usr/lib/dinit.d/kanidmd")
        self.take("usr/share/kanidm")

    return install


@subpackage("kanidm-unixd-clients")
def _(self):
    self.subdesc = (
        "localhost resolver to resolve posix identities to a kanidm instance"
    )
    self.install_if = [self.parent]

    def install():
        self.take("lib:libnss_kanidm.so.2")
        self.take("usr/lib/security/pam_kanidm.so")
        self.take("cmd:kanidm_ssh_authorizedkeys")
        self.take("cmd:kanidm_ssh_authorizedkeys_direct")
        self.take("cmd:kanidm-unix")
        self.take("cmd:kanidm_unixd")
        self.take("cmd:kanidm_unixd_tasks")
        self.take("usr/lib/dinit.d/kanidm-unixd")
        self.take("usr/lib/dinit.d/kanidm-unixd-tasks")

    return install
