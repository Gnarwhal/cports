pkgname = "obs-vaapi"
pkgver = "0.4.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libdir=lib/obs-plugins",
    "-Ddefault_library=shared",
]
hostmakedepends = [
    "cmake",
    "meson",
    "pkgconf",
]
makedepends = [
    "gst-plugins-base-devel",
    "obs-studio-devel",
    "pciutils-devel",
]
pkgdesc = "Gstreamer VAAPI OBS plugin"
license = "GPL-2.0-or-later"
url = "https://github.com/fzwoch/obs-vaapi"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "4c6a835f3e02511e07bce6ad2e23e6735864aaf43c52697caa2aa24c0f4dbf6d"
hardening = ["vis", "!cfi"]
