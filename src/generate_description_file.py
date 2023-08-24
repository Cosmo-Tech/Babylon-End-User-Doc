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
            content.append("<article markdown>")
            content.append("<div class=\"text\" markdown>")
            if _display_name := values.get('display_name'):
                content.append(f"### <a id=\"{key}\"></a>`{key}`<br/>{_display_name} {{ #{key} data-toc-label='{key}' }}")
            else:
                content.append(f"### {key}")
            content.append("---")
            if values.get('description') not in ['XXX', None]:
                content.append("What is this value ?")
                content.append(f":    {values.get('description')}")
                content.append("")
            if values.get('howto') not in ['XXX', None]:
                content.append("How to get a value to set here ?")
                content.append(f":    {values.get('howto')}  ")
            if values.get('example') not in ['XXX', None]:
                content.append("<div class=\"example\" markdown>")
                content.append(f"`{values.get('example')}`")
                content.append("</div>")
            content.append("</div>")
            content.append("</article>")
        content.append("")
        content.append('</main>')
        _md_file.writelines("\n".join(content))


generate_file("home")
