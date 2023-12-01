# (str) Package name
package.name = ER_Files

# (str) Package domain (needed for android/ios packaging)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,pyzbar,opencv

# (list) Permissions
android.permissions = CAMERA

# (list) Application binary compiled with these modules included
# comma separated e.g. include_prerecompiled = sdl2_ttf,pymunk
include_prerecompiled = sdl2_ttf,sdl2_image,pyzbar,opencv

# (str) Title of your application
title = YourAppTitle

# (str) Application versioning (method 1)
version = 0.1

# (list) Application source code
source.include_exts = py,png,jpg,kv,atlas

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy
# requirements.source.sdl2 = ../../sdl2
# ...

# (list) Garden requirements
#garden_requirements =
# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services =

# (str) Application build tool
#app_build_tool = pyqtdeploy

# (str) P4A is fully integrated
#p4a.source_dir = %(source.dir)s
#p4a.source.include_exts = .py,.pyx,.pyd,.so,.xml
#p4a.arch = armeabi-v7a
#p4a.bootstrap = sdl2

# (int) Target Android API, should be as high as possible.
# Make sure to do a short test when switching to a higher API level
#api.level = 27

# (int) Android NDK version to use
#android.ndk = 19c

# (int) Android NDK API to use. This is the minimum API your app will work on.
#android.ndk_api = 19

# (int) Android SDK version to use
#android.sdk = 27

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
#android.app_theme = @android:style/Theme.NoTitleBar
