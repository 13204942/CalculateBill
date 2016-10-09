# Bills Calculator
This python app is used to calculate bill when people share their bill together.
e.g. like electric bill, broadband bill or watrer bill

The UI design tutorial website:

http://doc.qt.io/qt-5/qtwidgets-layouts-basiclayouts-example.html
http://zetcode.com/gui/pysidetutorial/layoutmanagement/

## Design UI
![Alt text](/img/python_app.JPG?raw=true "UI")

## App Demo
![Alt text](/img/App_Demo.png?raw=true "UI")

## Run app on Mac
Go to /app folder and run this command in the shell:
```bash
python calculator.py
```

## Install Qt
Go to the official website to install Qt on Windows/Mac/Linux following the instructions
[http://doc.qt.io/qt-5/gettingstarted.html](http://doc.qt.io/qt-5/gettingstarted.html)

## Setting up PySide

### Windows
Installation of PySide on Windows is easy with the help of installer. Follow these steps for setting up PySide on Windows:

* Get the latest stable package compatible to your operating system architecture and the Python version installed from the releases page:

[http://qt-project.org/wiki/PySide_Binaries_Windows](http://qt-project.org/wiki/PySide_Binaries_Windows)

* Run the downloaded installer executable which will automatically detect the Python installation from your system.

* You are given an option to install PySide on the default path or at the path of your choice.

* Click on Next in the subsequent windows, and finally on Finish, PySide is installed successfully on your system.

### Mac OS X
The binaries for MAC OS X installers of PySide are available at:

[http://qt-project.org/wiki/PySide_Binaries_MacOSX](http://qt-project.org/wiki/PySide_Binaries_MacOSX)

Download the latest version compatible with your system and carry out installation as explained earlier.

You can also choose to install the PySide from the command line with the help of Homebrew or by using MacPorts. The commands are:

```bash
brew install pyside
port-install pyXX-pyside

replacing XX with your Python version
```

### Linux
Installing PySide on a Debian-based system is much easier with the synaptic package manager. Issuing the following command will fetch and install the latest stable version available in the aptitude distro:
```bash
sudo apt-get install python-pyside
```
On an RPM based system, you can use the RPM-based distro yum:
```bash
yum install python-pyside pyside-tools
```

## Build PySide
### Windows
Before starting to build PySide on Windows, ensure that the following prerequisites are installed:

* Qt 4.8 libraries for Windows from [http://releases.qt-project.org/qt4/source/qt-win-opensource-4.8.4-vs2008.exe](http://releases.qt-project.org/qt4/source/qt-win-opensource-4.8.4-vs2008.exe)

* CMake from [http://www.cmake.org/cmake/resources/software.html](http://www.cmake.org/cmake/resources/software.html)

* Git from [http://git-scm.com/download/win](http://git-scm.com/download/win)

* Python 2.6, 2.7, 3.2, or 3.3 from [http://www.python.org/download/](http://www.python.org/download/)

* OpenSSL from [http://slproweb.com/products/Win32OpenSSL.html](http://slproweb.com/products/Win32OpenSSL.html) (Optional)

Make sure that Git and CMake executable is set in your system PATH. Now, follow these steps to start building PySide:

 * Git clone the PySide repository from Github:
```bash
c:/> git clone https://github.com/PySide/pyside-setup.git pyside-setup
```
* Change your working directory to "pyside-setup":
```bash
c:/> cd pyside-setup
```
* Build the installer:
```bash
c:\> c:\Python27\python.exe setup.py bdist_wininst --msvc-version=9.0 --make=c:\Qt\4.8.4\bin\qmake.exe --openssl=c:\OpenSSL32bit\bin
```
* Upon successful installation, the binaries can be found in the sub-folder "dist":
```bash
c:\pyside-setup\dist
```
* On completion of these steps, the PySide should have been successfully built on your system.

### Linux

To build PySide on Linux, the following prerequisites must be available. Check if you have them already or download them using the following links.

Prerequisites
* CMake >= 2.6.0: [http://www.cmake.org/cmake/resources/software.html](http://www.cmake.org/cmake/resources/software.html)

* Qt libraries and development headers >= 4.6: [http://origin.releases.qt-project.org/qt4/source/qt-everywhere-opensource-src-4.8.4.tar.gz](http://origin.releases.qt-project.org/qt4/source/qt-everywhere-opensource-src-4.8.4.tar.gz)

* libxml2 and development headers >= 2.6.32: [http://www.xmlsoft.org/downloads.html](http://www.xmlsoft.org/downloads.html)

* libxslt and development headers >= 1.1.19: [http://xmlsoft.org/XSLT/downloads.html](http://xmlsoft.org/XSLT/downloads.html)

* Python libraries and development headers >= 2.5: [http://www.python.org/download/](http://www.python.org/download/)

PySide is a collection of four interdependent packages API Extractor, Generator Runner, Shiboken Generator, and Pyside Qt bindings. In order to build PySide, you have to download and install the packages mentioned previously in that order.

* API Extractor: A set of libraries used by the bindings generator to parse the header and typesystem files to create an internal representation of the API. [https://distfiles.macports.org/apiextractor/](https://distfiles.macports.org/apiextractor/)

* Generator Runner: Program that controls the bindings generation process according to the rules given by the user through headers, typesystem files, and generator frontends. It is dependent on the API Extractor. [https://distfiles.macports.org/generatorrunner/](https://distfiles.macports.org/generatorrunner/)

* Shiboken Generator: Plugin that creates the PySide bindings source files from Qt headers and auxiliary files (typesystems, global.h, and glue files). It is dependent on Generator Runner and API Extractor. [https://distfiles.macports.org/py-shiboken/](https://distfiles.macports.org/py-shiboken/)

* PySide Qt Bindings: Set of typesystem definitions and glue code that allows generations or a generation of Python Qt binding modules using the PySide tool chain. It is dependent on Shiboken and Generator Runner. [http://download.qt-project.org/official_releases/pyside/](http://download.qt-project.org/official_releases/pyside/)

Always make sure that you are downloading the packages mentioned previously and building them in the same order as mentioned, since each of the packages are interdependent. Follow these steps to build the packages:

Unzip the downloaded packages and change into the package directory:

```bash
tar –xvf <package_name>
cd <package_directory>
```
Create a build directory under the package directory and enter that directory:
```bash
mkdir build && cd build
```

Make the build using CMake:
```bash
cmake .. && make
```

On successful make, build and install the package:
```bash
sudo make install
```

Note that you require sudo permissions to install the packages.

To update the runtime linker cache, issue the following command:
```bash
sudo ldconfig
```
Once you follow these steps in order for each of the packages, the PySide should have been successfully built on your system.

### Mac OS X

Building PySide on a Mac system is the same as building it on Linux, except that Mac needs XCode-Developer tools to be installed as a prerequisite. The other prerequisites and building procedures are same as Linux.
