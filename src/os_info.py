[metadata]
name = osinfopkg
version = 0.0.1
author = Mariana Camelia
author_email = marianacamelia817@gmail.com
description = OS Information Package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/MarianaCamelia/osinfopkg
project_urls =
    Bug Tracker = https://github.com/MarianaCamelia/osinfopkg/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.6

[options.packages.find]
where = src
