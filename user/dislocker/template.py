pkgname = "dislocker"
pkgver = "0.7.3_git20260831"
pkgrel = 0
_gitrev = "0706462db88efe8df88150e4c3e4332b808f4581"
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
source = f"https://github.com/Aorimn/dislocker/archive/{_gitrev}.tar.gz"
sha256 = "e48061012aafac5c5f37e453e91a1dc94bd32af67e9313d17689c7935bb07b57"
