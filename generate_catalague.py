import json
import re
import os
from sys import stdin


def generate_catalogue(font_list):
    font_entries = ""
    for font in font_list:
        font_entry = r"""
\samepage
\noindent\verb|%FONT_NAME%|\\
\begingroup
\setmainfont{%FONT_FILE%}
\resizebox{\ifdim\width>\textwidth\textwidth\else\width\fi}{!}{\hspace{4mm}{\LARGE the brown fox jumps over the lazy dog.}}
\endgroup
"""
        font_entry = font_entry.replace(r"%FONT_FILE%", os.path.basename(font["path"]))
        font_entry = font_entry.replace(r"%FONT_NAME%", os.path.basename(font["name"]))
        font_entries += font_entry

    with open("template/catalogue.tex", "r") as catalogue_template:
        catalogue_template = catalogue_template.read()
    with open("catalogue.tex", "w") as catalogue:
        catalogue.write(catalogue_template.replace(r"%FONT_ENTRIES%", font_entries))


def parse_fc_list():
    fc_pattern = r"(?P<path>.+?): (?P<name>[^:]+):style=(?P<style>.+)"
    font_dict = {}

    for line in stdin:
        match = re.match(fc_pattern, line)
        if match:
            font_data = match.groupdict()
            font_name = font_data["name"].split(",")[0]  # Extract primary name
            font_name = font_name.replace(r"\-", "-")
            font_name = font_name.replace(r"\\040", " ")
            font_data["name"] = font_name

            if font_name not in font_dict:
                font_dict[font_name] = font_data

    return sorted(font_dict.values(), key=lambda font: font["name"].lower())


if __name__ == "__main__":
    font_list = parse_fc_list()
    generate_catalogue(font_list)
