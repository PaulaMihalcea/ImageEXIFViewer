# IEViewer: a Python image & EXIF viewer
## Author: Paula Mihalcea
#### Università degli Studi di Firenze

---

![](https://img.shields.io/github/repo-size/paulamihalcea/IEViewer)

This project aims to build a simple, yet fully functional and failsafe (to an extent) **image and EXIF viewer** using the **Python** programming language and the **PyQt5** GUI toolkit.

**[EXIF](cipa.jp/std/documents/download_e.html?DC-008-Translation-2019-E "EXIF")** (Exchangeable Image File Format) is a standard that specifies the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras. The specification uses the existing file formats with the addition of specific metadata tags, which cover a broad spectrum:
- date and time information;
- camera settings, such as the camera model and make, and information that varies with each image (e.g. orientation, aperture, shutter speed, focal length, metering mode, and ISO speed information);
- a thumbnail for previewing the picture on the camera's LCD screen, in file managers, or in photo manipulation software;
- descriptions;
- copyright information.

<sup>(adapted from [Wikipedia](https://en.wikipedia.org/wiki/Exif "Wikipedia"))</sup>

## Features
The program features the following operations:
- **Open** and **display an image** in one of the supported formats.
- **Show** any available **EXIF data** (JPEG and PNG images only).
- **Rotate** the image (180°, 90° clock wise, 90° counter clock wise).
- **Reset** the image to its original orientation (if rotated).
- **Save** the rotated image.

All operations can be accessed from either the **tool bar** or the **menu bar**, and are accompanied by meaningful icons. Additionally, a **status bar** at the bottom of the window displays a short description for each button when hovered over.

### GPS Data
Whenever the EXIF data of an image also contains **GPS data**, the program processes it in order to generate a hyperlink on which the user can double-click in order to open in the browser a **[Google Maps](https://www.google.com/maps/) page centered at the GPS coordinates** contained in the EXIF data.

<img src="https://github.com/PaulaMihalcea/IEViewer/blob/master/screenshots/gps_2.png" width="50%" height="50%">

### Supported file formats
<table>
    <tr>
        <td>
            <table>
                <tr>
                    <th><b>Format</b></th>
                    <th><b>Support</b></th>
                </tr>
                <tr>
                    <td>BMP</td>
                    <td>Read/Write</td>
                </tr>
                <tr>
                    <td>GIF</td>
                    <td>Read</td>
                </tr>
                <tr>
                    <td>JPG</td>
                    <td>Read/Write</td>
                </tr>
                <tr>
                    <td>JPEG</td>
                    <td>Read/Write</td>
                </tr>
                <tr>
                    <td>PNG</td>
                    <td>Read/Write</td>
                </tr>
            </table>
        </td>
        <td>
            <table>
                <tr>
                    <th><b>Format</b></th>
                    <th><b>Support</b></th>
                </tr>
                <tr>
                    <td>PBM</td>
                    <td>Read</td>
                </tr>
                <tr>
                    <td>PGM</td>
                    <td>Read</td>
                </tr>
                <tr>
                    <td>PPM</td>
                    <td>Read/Write</td>
                </tr>
                <tr>
                    <td>XBM</td>
                    <td>Read/Write</td>
                </tr>
                <tr>
                    <td>XPM</td>
                    <td>Read/Write</td>
                </tr>
            </table>
        </td>
    </tr>
</table>

## Installation
Being a Python application, IEViewer has a few basic requirements in order to be up and running. In order to install them, the [pip](https://packaging.python.org/key_projects/#pip "pip") package installer is recommended, as it allows for the automatic installation of all requirements. Nonetheless, the latter have been listed in order to simplify an eventual manual installation.

1. Download the repository and navigate to its folder.

2. Install the requirements using `pip`:

    ```
    pip install --upgrade -r requirements.txt
    ```

### Requirements
Please note that the following versions are to be intended as minimum.

| Package | Version |
| :------------ | :------------ |
| Python | 3.8 |
| Pillow | 8.2.0 |
| PyQt | 5.9.2 |

## Usage
- **Linux:** Run IEViewer from the terminal:

    ```
    python3 main.py
    ```
   
- **Windows:** You can either run IEViewer from the terminal just like on Linux, or you can modify the given `IEViewer.bat` file with the full path to your Python 3 executable and the full path to the IEViewer `main.py` script.

    *For example, if Python 3 has been installed to `C:\ProgramData\Anaconda3\python.exe` and `main.py` can be found in `C:\Users\Username\IEViewer\`, then the `IEViewer.bat` file will be:*

    ```
    "C:\ProgramData\Anaconda3\python.exe" "C:\Users\Username\IEViewer\main.py"
    pause
    ```

## Technical details
**IEViewer** has been programmed in the **[Python](https://www.python.org/ "Python")** language, and uses the **[PyQt5](https://riverbankcomputing.com/software/pyqt "PyQt5")** library for its graphical user interface.

It features a complete [Model View Controller](https://martinfowler.com/eaaDev/uiArchs.html#ModelViewController "Model View Controller") design pattern, partially complemented with the [Observer](https://martinfowler.com/eaaDev/MediatedSynchronization.html "Observer") pattern:
- **Model**, `model.py`: contains all the information needed to process the image and its EXIF data (if available), including the actual image object used by the other components.
- **View**, `view.py`: defines the main window's appearance and connects its buttons to controller functions; it also is a subject for the controller in the Observer pattern.
- **Controller**, `controller.py`: loads and saves the image (manages the I/O); it is an observer of the view subject.

Additional script files include:
- `observer.py`: a basic, manual implementation of the Observer design pattern;
- `widgets.py`: an overhaul of all the PyQt5 widgets used by the view, appropriately customized for this application.

## License
Licensed under the **CC BY-NC-SA 4.0 License** (IEViewer) and the **GNU GPL v3 License** & **Riverbank Commercial License** (PyQt5). More details in the `LICENSE.md` file.
