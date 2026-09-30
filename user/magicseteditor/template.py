pkgname = "magicseteditor"
pkgver = "2.1.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "boost-devel",
    "hunspell-devel",
    "wxwidgets-devel",
]
checkdepends = ["perl"]
pkgdesc = "Design your own magic cards"
license = "GPL-2.0-or-later"
url = "https://magicseteditor.boards.net"
source = f"https://github.com/twanvl/MagicSetEditor2/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1342e54c770ed2123a54958fb5225faf5948945035ca14a03f4ad7449c7df9a0"
