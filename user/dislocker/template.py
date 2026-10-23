pkgname = "dislocker"
pkgver = "0.7.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIB_INSTALL_DIR=/usr/lib",
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "fuse-devel",
    "mbedtls-devel-static",
    "ruby-devel",
]
pkgdesc = "FUSE driver to read/write Windows' BitLocker-ed volumes"
license = "GPL-2.0-or-later"
url = "https://github.com/Aorimn/dislocker"
source = (
    f"https://github.com/Aorimn/dislocker/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e48061012aafac5c5f37e453e91a1dc94bd32af67e9313d17689c7935bb07b57"
