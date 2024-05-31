pkgname = "plasma-workspace"
pkgver = "6.0.5"
pkgrel = 1
build_style = "cmake"
# TODO: -DINSTALL_SDDM_WAYLAND_SESSION=ON experiments?
configure_args = ["-DGLIBC_LOCALE_GEN=OFF"]
make_check_args = [
    "-E",
    "(^tasksmodeltest$"  # failing test_moveLauncherBug472524() & test_moveBug444816()
    + "|shelltest"  # SEGFAULT in initTestCase(), Invalid home screen package + missing org.kde.desktopcontainment (plasmoid)?
    + "|tst_triangleFilter"  # needs installed org.kde.plasma.private.kicker QML module
    + "|systemtraymodeltest"  # testPlasmoidModel() seems to have another case of broken QFINDTESTDATA, systemtraymodeltest.cpp(79)
    + "|testimagefinder"  # ImageFinder doesn't find testdata/default/.BUG460287/*.webp for some reason, test_imagefinder.cpp(64)
    + "|testimagelistmodel"  # ^ probably same as above, test_imagelistmodel.cpp(81)
    + "|testpackageimagelistmodel"  # just SEGFAULTS after testPackageListModelRemoveBackground(), broken kio? test_packagelistmodel.cpp(262)
    + "|testimageproxymodel"  # looks like same issue as testimagefinder & testimagelistmodel
    + "|testslidemodel"  # ^ same as above
    + "|testimagebackend"  # cannot find org.kde.plasma.wallpapers.image QML module, try QML2_IMPORT_PATH?
    + "|testimagefrontend)",  # ^ same as above
    "-j1",  # parallel causes a bunch of flaky tests
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "xwfb-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "spirv-tools",
]
makedepends = [
    "breeze-devel",
    "fontconfig-devel",
    "karchive-devel",
    "kauth-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdeclarative-devel",
    "kded-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kidletime-devel",
    "kio-devel",
    "kitemmodels-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kpipewire-devel",
    "krunner-devel",
    "kscreenlocker-devel",
    "kstatusnotifieritem-devel",
    "ksvg-devel",
    "ktexteditor-devel",
    "ktextwidgets-devel",
    "kunitconversion-devel",
    "kuserfeedback-devel",
    "kwallet-devel",
    "kwayland-devel",
    "kwin-devel",
    "layer-shell-qt-devel",
    "libcanberra-devel",
    "libice-devel",
    "libkexiv2-devel",
    "libkscreen-devel",
    "libksysguard-devel",
    "libplasma-devel",
    "libqalculate-devel",
    "libsm-devel",
    "networkmanager-qt-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "plasma-activities-stats-devel",
    "plasma-wayland-protocols",
    "plasma5support-devel",
    "prison-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "xcb-util-devel",
    # TODO: KF6Baloo
    # TODO: KF6Holidays
    # TODO: AppStreamQt (main/appstream + -Dqt=true)
    # NOTE: make sure PolkitQt6-1 doesn't get pulled in?! just -DGLIBC_LOCALE_GEN=OFF
    # TODO: AppMenuGtkModule?
    # TODO: SeleniumWebDriverATSPI? (GUI accessibility tests)
]
checkdepends = [
    "dbus",
    "python-gobject",
    "xwayland-run",
]
depends = [
    "iso-codes",
    "kirigami-addons",
    # "kio-extras",
    # "kio-fuse",
    "kquickcharts",
    "kwin",
    "xwayland",
]
pkgdesc = "KDE Plasma Workspace"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "(GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.1-or-later AND GPL-2.0-or-later AND MIT AND LGPL-2.1-only AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND LGPL-2.0-only"
url = "https://api.kde.org/plasma/plasma-workspace/html"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-workspace-{pkgver}.tar.xz"
sha256 = "c54d2d5adf5eb2feef7092b9217f1ed59c98e369f9b5d7b12dd77365f4eb7ac9"
# FIXME: cfi breaks at least 3 tests
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSES/MIT.txt")


@subpackage("plasma-workspace-devel")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (development files)"
    # libkrdb.so unversined, avoid plasma-workspace pulling in plasma-workspace-devel
    return [
        "usr/include",
        "usr/lib/libcolorcorrect.so",
        "usr/lib/libkfontinst*.so",
        "usr/lib/libkmpris.so",
        "usr/lib/libkworkspace6.so",
        "usr/lib/libnotificationmanager.so",
        "usr/lib/libtaskmanager.so",
        "usr/lib/libweather_ion.so",
        "usr/lib/cmake",
    ]