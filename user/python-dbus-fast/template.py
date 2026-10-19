pkgname = "python-dbus-fast"
pkgver = "5.2.0"
pkgrel = 0
build_style = "python_pep517"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-poetry-core",
    "python-setuptools",
]
makedepends = [
    "python-devel",
]
depends = ["python"]
checkdepends = [
    "dbus",
    "python-covdefaults",
    "python-gobject",
    "python-pytest-asyncio",
    "python-pytest-cov",
    "python-pytest-timeout",
]
pkgdesc = "DBus library for python"
license = "MIT"
url = "https://pypi.org/project/dbus-fast"
source = f"https://github.com/Bluetooth-Devices/dbus-fast/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ef317b8a891b16c5733e0de15e3aa753a958ef89786cc77e17e328ceab4935e3"


def post_prepare(self):
    # Requires pytest_codspeed
    self.rm("tests/benchmarks", recursive=True)


def post_install(self):
    self.install_license("LICENSE")
