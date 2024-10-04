# RDP URL Handler

A cross-platform RDP URL handler that processes `rdp://` URLs and launches the ThinCast RDP client.

## Features

- Supports both MacOS and Ubuntu Linux.
- Parses `rdp://` URLs and extracts parameters.
- Generates `.rdp` files based on parameters.
- Launches ThinCast RDP client with the generated `.rdp` file.
- Runs silently in the background with logging.
- Seamless installation without manual intervention.

## Requirements

- **ThinCast RDP Client** must be installed on the system.
- For **Ubuntu Linux**:
  - `xdg-utils` package (installed automatically).

## Building and Installing

### MacOS

#### Building the Application

1. **Install Python 3.8 or higher** (if not already installed).

2. **Install Poetry** for dependency management:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

4. **Clone the repository** and navigate to the project directory.

5. **Install dependencies**:

   ```bash
   poetry install
   ```

6. **Build the executable** using PyInstaller and the provided spec file:

    ```bash
    pyinstaller RDPURLHandler.spec
    ```

    - This command will generate the application in the `dist` and `build` directories.

#### Creating the Installer

1. **Copy the `postinstall` script** into a `scripts` directory. (Skip this if it's already in the `scripts` directory).

2. **Build the installer package**:

   ```bash
   pkgbuild \
     --root dist/RDPURLHandler.app \
     --identifier com.yourcompany.rdpurlhandler \
     --version 1.0.0 \
     --install-location /Applications \
     --scripts scripts \
     RDPURLHandler.pkg
   ```

3. **Install the package**:

   - Users can install `RDPURLHandler.pkg` by double-clicking it.
   - **Prerequisites** - ThinCast RDP Client must be installed on the system.

### Ubuntu Linux

#### Building the Application

1. **Install Python 3.8 or higher** (if not already installed).

2. **Install Poetry**:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install PyInstaller**:

   ```bash
   pip install pyinstaller
   ```

4. **Clone the repository** and navigate to the project directory.

5. **Install dependencies**:

   ```bash
   poetry install
   ```

6. **Build the executable** using PyInstaller:

   ```bash
   pyinstaller --onefile --name rdp_url_handler rdp_handler/main.py
   ```

   - The executable `rdp_url_handler` will be in the `dist` directory.

#### Creating the `.deb` Package

1. **Create the directory structure**:

   ```bash
   mkdir -p rdp-url-handler/usr/local/bin
   mkdir -p rdp-url-handler/DEBIAN
   ```

2. **Copy the executable**:

   ```bash
   cp dist/rdp_url_handler rdp-url-handler/usr/local/bin/
   ```

3. **Create the `control` file** in `rdp-url-handler/DEBIAN/`:

   ```bash
   # rdp-url-handler/DEBIAN/control

   Package: rdp-url-handler
   Version: 1.0.0
   Section: utils
   Priority: optional
   Architecture: amd64
   Depends: xdg-utils
   Maintainer: Your Name <you@example.com>
   Description: RDP URL Handler for Ubuntu
    A cross-platform RDP URL handler that processes rdp:// URLs and launches the ThinCast RDP client.
   ```

4. **Copy the `postinst` script** to `rdp-url-handler/DEBIAN/` and set permissions:

   ```bash
   chmod 755 rdp-url-handler/DEBIAN/postinst
   ```

5. **Build the `.deb` package**:

   ```bash
   dpkg-deb --build rdp-url-handler
   ```

   - This creates `rdp-url-handler.deb`.

6. **Install the package**:

   ```bash
   sudo dpkg -i rdp-url-handler.deb
   ```
   - **Prerequisites** - ThinCast RDP Client must be installed on the system.
   - Dependencies are installed automatically.
   - URL scheme registration happens during installation.

## Usage

- **After installation**, clicking on an `rdp://` URL will automatically:

  - Launch the RDP URL Handler.
  - Generate an `.rdp` file based on the URL parameters.
  - Open the ThinCast RDP client with the generated `.rdp` file.

- **Example URL**:

  ```
  rdp://v=172.105.58.129:3389&username=macrometa&f=true
  ```

## Logs

- **MacOS**: `~/Library/Logs/RDPURLHandler/rdp_url_handler.log`
- **Ubuntu Linux**: `~/.rdpurlhandler/logs/rdp_url_handler.log`

## Uninstallation

### MacOS

- **Clear URL handler registration** (optional):

  ```bash
  /System/Library/Frameworks/CoreServices.framework/Frameworks/LaunchServices.framework/Support/lsregister -u /Applications/RDPURLHandler.app
  ```

- **Remove the application**:

  ```bash
  sudo rm -rf /Applications/RDPURLHandler.app
  ```

### Ubuntu Linux

- **Uninstall the package**:

  ```bash
  sudo dpkg -r rdp-url-handler
  ```

- **Clear URL handler registration** (handled automatically during removal).
