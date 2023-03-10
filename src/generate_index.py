from typing import IO

import mkdocs_gen_files

from Babylon.version import VERSION

_md_file: IO
with mkdocs_gen_files.open("index.md", "w") as _md_file, \
        open("templates/index.md") as index_template, \
        open("README.md") as readme:
    _index: list[str] = index_template.readlines()
    _readme_content = readme.readlines()
    for _line in _index:
        if "--README--" in _line:
            _md_file.writelines(_readme_content[1:])
            continue
        _md_file.write(_line.replace("%%VERSION%%", VERSION))
