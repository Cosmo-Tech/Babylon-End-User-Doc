from typing import IO

import mkdocs_gen_files
import yaml


def generate_file(file_type: str):
    _md_file: IO
    with mkdocs_gen_files.open(f"guides/{file_type}.md", "w") as _md_file, \
            open(f"data/{file_type}.yaml") as _file_data:
        _items = yaml.safe_load(_file_data)
        content = list()
        content.append(f"# {file_type.capitalize()} configuration values")
        content.append("")
        content.append("")
        content.append('<main class="grid" markdown>')
        for key, values in _items.items():
            content.extend(f"""<article markdown>
<div class="text" markdown>
### {key}
---
What is this value ?
:    {values.get('description')}

How to get a value to set here ?  
:    {values.get('howto')}  
<div class="example" markdown>
`{values.get('example')}`
</div>
</div>
</article>""".split('\n'))
        content.append("")
        content.append('</main>')
        _md_file.writelines("\n".join(content))


generate_file("deployment")
generate_file("platform")
