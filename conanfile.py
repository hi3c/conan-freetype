from conans import ConanFile, CMake, tools, AutoToolsBuildEnvironment
import os


class FreetypeConan(ConanFile):
    name = "freetype"
    version = "2.8"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        tools.download("http://download.savannah.gnu.org/releases/freetype/freetype-2.8.tar.bz2", "freetype.tar.bz2")
        tools.unzip("freetype.tar.bz2")
        os.remove("freetype.tar.bz2")

    def build(self):
        atbe = AutoToolsBuildEnvironment(self)
        atbe.fpic = True
        atbe.configure(configure_dir="freetype-2.8", args=["--with-bzip2=no", "--with-png=no", "--with-harfbuzz=no", "--with-zlib=no"])
        atbe.make()

    def package(self):
        self.copy("*.h", dst="include", src="freetype-2.8/include")
        self.copy("*.lib", dst="lib", keep_path=False)

        if self.options.shared:
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so", dst="lib", keep_path=False)
            self.copy("*.dylib", dst="lib", keep_path=False)
        else:
            self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["freetype"]
