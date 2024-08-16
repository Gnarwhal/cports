pkgname = "sshare"
pkgver = "2.0.0"
pkgrel = 1
build_style = "python_pep517"
make_build_env = {
    "SETUPTOOLS_SCM_PRETEND_VERSION": pkgver,
}
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
    "python-wheel",
]
pkgdesc = "Upload files to a server via ssh"
license = "GPL-3.0-or-later"
url = "https://forge.monodon.me/Gnarwhal/sshare"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "5a9c22191b0ab5e6e4cd2021150f719845df93acb44ab42f2379f91666f9f1c7"
# no tests
options = ["!check"]
