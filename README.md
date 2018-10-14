# A Simple Python Script Packaged as a MacOS Application

This project simply provides an example of how to package a
Python program as a MacOS application. It is mostly for my
own reference in case I forget how to do this in the future.

Basic structure:

```
  - MyMacPyApp.app/
    - Contents/
      - app.py - the Python script that will run when the app is launched.
      - MacOS/
        - MyMacPyApp - An executable bash script that launches app.py
```

The naming is important - the launcher script must be named
the same as the application, without the .app extension.

Any resources the app needs can be housed in the `Contents/` directory or
subdirectories thereof.
