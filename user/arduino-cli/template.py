pkgname = "arduino-cli"
pkgver = "1.5.1"
pkgrel = 0
build_style = "go"
make_build_args = [f"-ldflags=-X version.versionString={pkgver}"]
hostmakedepends = ["go"]
pkgdesc = "Arduino command line tool"
license = "GPL-3.0-or-later"
url = "https://docs.arduino.cc/arduino-cl"
source = (
    f"https://github.com/arduino/arduino-cli/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "262fbe874f62677d01eb15593144ca82bd6e7c2d0c00f82aa93949ab12924de6"
