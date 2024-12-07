[app]

# (str) Title of your application
title = Learning Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,wav,mp3

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,jsonschema,kivy==2.0.0rc4,kivy_garden.graph, https://github.com/kivymd/KivyMD/archive/master.zip, materialyoucolor,exceptiongroup,asyncgui,asynckivy,pillow,altair,absl-py==2.1.0
,aiohappyeyeballs==2.4.0
,aiohttp==3.10.5
,aiosignal==1.3.1
,altair==5.4.1
,anaconda==0.0.1.1
,annotated-types==0.7.0
,anyio==4.6.0
,appdirs==1.4.4
,arrow==1.3.0
,asgiref==3.8.0
,asttokens==2.4.1
,astunparse==1.6.3
,attrs==24.2.0
,beautifulsoup4==4.12.3
,binaryornot==0.4.4
,blinker==1.8.2
,build==1.2.2.post1
,buildozer==1.5.0
,CacheControl==0.14.1
,cachetools==5.5.0
,catboost==1.2.7
,certifi==2024.7.4
,cffi==1.17.1
,chardet==5.2.0
,charset-normalizer==3.3.2
,click==8.1.7
,cmake==3.30.5
,colorama==0.4.6
,comm==0.2.2
,comtypes==1.4.8
,contourpy==1.3.0
,cookiecutter==2.6.0
,cryptography==43.0.3
,cycler==0.12.1
,Cython==0.29.19
,dataclasses-json==0.6.7
,debugpy==1.8.7
,decorator==5.1.1
,distlib==0.3.9
,distro==1.9.0
,Django==5.0.3
,django-cors-headers==4.3.1
,django-rest-framework==0.1.0
,djangorestframework==3.15.0
,dm-tree==0.1.8
,docstring_parser==0.16
,docutils==0.21.2
,et-xmlfile==1.1.0
,etils==1.10.0
,executing==2.1.0
,fastjsonschema==2.20.0
,filelock==3.16.1
,firebase-admin==6.6.0
,Flask==3.0.3
,Flask-Cors==5.0.0
,flatbuffers==24.3.25
,fonttools==4.54.1
,frozenlist==1.4.1
,fsspec==2024.9.0
,gast==0.6.0
,gitdb==4.0.11
,GitPython==3.1.43
,google-api-core==2.22.0
,google-api-python-client==2.151.0
,google-auth==2.36.0
,google-auth-httplib2==0.2.0
,google-auth-oauthlib==1.2.1
,google-cloud-core==2.4.1
,google-cloud-firestore==2.19.0
,google-cloud-storage==2.18.2
,google-crc32c==1.6.0
,google-pasta==0.2.0
,google-resumable-media==2.7.2
,googleapis-common-protos==1.65.0
,graphviz==0.20.3
,greenlet==3.1.1
,grpcio==1.68.1
,grpcio-status==1.68.1
,h11==0.14.0
,h5py==3.12.1
,httpcore==1.0.5
,httplib2==0.22.0
,httpx==0.27.2
,huggingface-hub==0.25.0
,idna==3.7
,immutabledict==4.2.0
,importlib_resources==6.4.5
,iniconfig==2.0.0
,ipykernel==6.29.5
,ipython==8.28.0
,itsdangerous==2.2.0
,jdk==0.0.6
,jedi==0.19.1
,Jinja2==3.1.4
,jiter==0.5.0
,joblib==1.4.2
,jsonpatch==1.33
,jsonpointer==3.0.0
,jsonschema==4.23.0
,jsonschema-specifications==2023.12.1
,jupyter_client==8.6.3
,jupyter_core==5.7.2
,keras==3.6.0
,Kivy==2.3.0
,kivy-deps.angle==0.4.0
,kivy-deps.glew==0.3.1
,kivy-deps.sdl2==0.7.0
,Kivy-Garden==0.1.5
,kiwisolver==1.4.7
,langchain==0.3.0
,langchain-community==0.3.0
,langchain-core==0.3.5
,langchain-text-splitters==0.3.0
,langsmith==0.1.125
,libclang==18.1.1
,lightgbm==4.5.0
,Markdown==3.7
,markdown-it-py==3.0.0
,MarkupSafe==2.1.5
,marshmallow==3.22.0
,matplotlib==3.9.2
,matplotlib-inline==0.1.7
,mdurl==0.1.2
,ml-dtypes==0.4.1
,MouseInfo==0.1.3
,msal==1.31.0
,msgpack==1.1.0
,multidict==6.1.0
,mypy-extensions==1.0.0
,namex==0.0.8
,narwhals==1.8.2
,nbformat==5.10.4
,nest-asyncio==1.6.0
,nltk==3.9.1
,numpy==1.26.4
,oauthlib==3.2.2
,openai==1.47.0
,opencv-contrib-python==4.10.0.84
,opencv-python==4.10.0.84
,openpyxl==3.1.5
,opt_einsum==3.4.0
,optree==0.13.0
,orjson==3.10.7
,packaging==24.1
,pandas==2.2.2
,parso==0.8.4
,pexpect==4.9.0
,pillow==10.4.0
,platformdirs==4.3.6
,plotly==5.22.0
,pluggy==1.5.0
,promise==2.3
,prompt_toolkit==3.0.48
,proto-plus==1.25.0
,protobuf==5.28.2
,psutil==6.0.0
,psycopg2==2.9.10
,ptyprocess==0.7.0
,pure_eval==0.2.3
,pyarrow==17.0.0
,pyasn1==0.6.1
,pyasn1_modules==0.4.1
,PyAudio==0.2.14
,PyAutoGUI==0.9.54
,pycparser==2.22
,pydantic==2.9.2
,pydantic-settings==2.5.2
,pydantic_core==2.23.4
,pydeck==0.9.1
,PyGetWindow==0.0.9
,Pygments==2.18.0
,PyJWT==2.9.0
,PyMsgBox==1.0.9
,pymssql==2.3.1
,PyMuPDF==1.24.13
,pyodbc==5.2.0
,pyparsing==3.2.0
,pyperclip==1.9.0
,pypiwin32==223
,pyproject_hooks==1.2.0
,PyRect==0.2.0
,PyScreeze==0.1.30
,pytest==8.3.3
,python-dateutil==2.9.0.post0
,python-dotenv==1.0.1
,python-for-android==2024.1.21
,python-slugify==8.0.4
,pyttsx3==2.98
,pytweening==1.2.0
,pytz==2024.1
,pywhatkit==5.4
,pywin32==308
,PyYAML==6.0.2
,pyzmq==26.2.0
,referencing==0.35.1
,regex==2024.9.11
,requests==2.32.3
,requests-oauthlib==2.0.0
,rich==13.8.1
,rpds-py==0.20.0
,rsa==4.9
,safetensors==0.4.5
,scikit-learn==1.5.2
,scipy==1.14.1
,seaborn==0.13.2
,setuptools==75.2.0
,sh==2.1.0
,simple-parsing==0.1.6
,six==1.16.0
,smmap==5.0.1
,sniffio==1.3.1
,soupsieve==2.5
,SpeechRecognition==3.11.0
,SQLAlchemy==2.0.35
,sqlparse==0.4.4
,stack-data==0.6.3
,streamlit==1.38.0
,tenacity==8.5.0
,tensorboard==2.18.0
,tensorboard-data-server==0.7.2
,tensorflow==2.18.0
,tensorflow-datasets==4.9.7
,tensorflow-metadata==1.16.1
,tensorflow_intel==2.18.0
,termcolor==2.5.0
,text-unidecode==1.3
,threadpoolctl==3.5.0
,tokenizers==0.19.1
,toml==0.10.2
,tomli_w==1.1.0
,tornado==6.4.1
,tqdm==4.66.5
,traitlets==5.14.3
,transformers==4.44.2
,types-python-dateutil==2.9.0.20241003
,typing-inspect==0.9.0
,typing_extensions==4.12.2
,tzdata==2024.1
,uritemplate==4.1.1
,urllib3==2.2.2
,virtualenv==20.27.1
,watchdog==4.0.2
,wcwidth==0.2.13
,Werkzeug==3.0.3
,wheel==0.44.0
,wikipedia==1.4.0
,wrapt==1.16.0
,wsl==0.12
,xgboost==2.1.1
,yarl==1.11.1
,zipp==3.20.2

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 2.3.0

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
#android.permissions = android.permission.INTERNET, (name=android.permission.WRITE_EXTERNAL_STORAGE;maxSdkVersion=18)

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 31

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <manifest><application> tag of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) Full name including package path of the Java class that implements Python Service
# use that parameter to set custom Java class which extends PythonService
#android.service_class_name = org.kivy.android.PythonService

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk assets directory.
# Either form may be used, and assets need not be in 'source.include_exts'.
# 1) android.add_assets = source_asset_relative_path
# 2) android.add_assets = source_asset_path:destination_asset_relative_path
#android.add_assets =

# (list) Put these files or directories in the apk res directory.
# The option may be used in three ways, the value may contain one or zero ':'
# Some examples:
# 1) A file to add to resources, legal resource names contain ['a-z','0-9','_']
# android.add_resources = my_icons/all-inclusive.png:drawable/all_inclusive.png
# 2) A directory, here  'legal_icons' must contain resources of one kind
# android.add_resources = legal_icons:drawable
# 3) A directory, here 'legal_resources' must contain one or more directories, 
# each of a resource kind:  drawable, xml, etc...
# android.add_resources = legal_resources
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
#android.enable_androidx = True

# (list) add java compile options
# this can for example be necessary when importing certain java libraries using the 'android.gradle_dependencies' option
# see https://developer.android.com/studio/write/java8-support for further information
# android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

# (list) Gradle repositories to add {can be necessary for some android.gradle_dependencies}
# please enclose in double quotes 
# e.g. android.gradle_repositories = "maven { url 'https://kotlin.bintray.com/ktor' }"
#android.add_gradle_repositories =

# (list) packaging options to add 
# see https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.PackagingOptions.html
# can be necessary to solve conflicts in gradle_dependencies
# please enclose in double quotes 
# e.g. android.add_packaging_options = "exclude 'META-INF/common.kotlin_module'", "exclude 'META-INF/*.kotlin_module'"
#android.add_packaging_options =

# (list) Java classes to add as activities to the manifest.
#android.add_activities = com.example.ExampleActivity

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
#android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.manifest.intent_filters =

# (list) Copy these files to src/main/res/xml/ (used for example with intent-filters)
#android.res_xml = PATH_TO_FILE,

# (str) launchMode to set for the main activity
#android.manifest.launch_mode = standard

# (str) screenOrientation to set for the main activity.
# Valid values can be found at https://developer.android.com/guide/topics/manifest/activity-element
#android.manifest.orientation = fullSensor

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so
#android.add_libs_armeabi_v7a = libs/android-v7/*.so
#android.add_libs_arm64_v8a = libs/android-v8/*.so
#android.add_libs_x86 = libs/android-x86/*.so
#android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
#android.wakelock = False

# (list) Android application meta-data to set (key=value format)
#android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
#android.library_references =

# (list) Android shared libraries which will be added to AndroidManifest.xml using <uses-library> tag
#android.uses_library =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
#android.logcat_pid_only = False

# (str) Android additional adb arguments
#android.adb_args = -H host.docker.internal

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]
# android.manifest_placeholders = [:]

# (bool) Skip byte compile for .py files
# android.no-byte-compile-python = False

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) The format used to package the app for debug mode (apk or aar).
# android.debug_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
#p4a.url =

# (str) python-for-android fork to use in case if p4a.url is not specified, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
#p4a.port =

# Control passing the --use-setup-py vs --ignore-setup-py to p4a
# "in the future" --use-setup-py is going to be the default behaviour in p4a, right now it is not
# Setting this to false will pass --ignore-setup-py, true will pass --use-setup-py
# NOTE: this is general setuptools integration, having pyproject.toml is enough, no need to generate
# setup.py if you're using Poetry, but you need to add "toml" to source.include_exts.
#p4a.setup_py = false

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
#p4a.extra_args =



#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the URL and branch of a git checkout:
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

# Another platform dependency: ios-deploy
# Uncomment to use a custom checkout
#ios.ios_deploy_dir = ../ios_deploy
# Or specify URL and branch
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0

# (bool) Whether or not to sign the code
ios.codesign.allowed = false

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) The development team to use for signing the debug version
#ios.codesign.development_team.debug = <hexstring>

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing the release version
#ios.codesign.development_team.release = <hexstring>

# (str) URL pointing to .ipa file to be installed
# This option should be defined along with `display_image_url` and `full_size_image_url` options.
#ios.manifest.app_url =

# (str) URL pointing to an icon (57x57px) to be displayed during download
# This option should be defined along with `app_url` and `full_size_image_url` options.
#ios.manifest.display_image_url =

# (str) URL pointing to a large icon (512x512px) to be used by iTunes
# This option should be defined along with `app_url` and `display_image_url` options.
#ios.manifest.full_size_image_url =


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
# bin_dir = ./bin

#    -----------------------------------------------------------------------------
#    List as sections
#
#    You can define all the "list" as [section:key].
#    Each line will be considered as a option to the list.
#    Let's take [app] / source.exclude_patterns.
#    Instead of doing:
#
#[app]
#source.exclude_patterns = license,data/audio/*.wav,data/images/original/*
#
#    This can be translated into:
#
#[app:source.exclude_patterns]
#license
#data/audio/*.wav
#data/images/original/*
#


#    -----------------------------------------------------------------------------
#    Profiles
#
#    You can extend section / key with a profile
#    For example, you want to deploy a demo version of your application without
#    HD content. You could first change the title to add "(demo)" in the name
#    and extend the excluded directories to remove the HD content.
#
#[app@demo]
#title = My Application (demo)
#
#[app:source.exclude_patterns@demo]
#images/hd/*
#
#    Then, invoke the command line with the "demo" profile:
#
#buildozer --profile demo android debug
