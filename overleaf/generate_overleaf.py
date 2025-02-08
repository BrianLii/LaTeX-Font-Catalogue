import os
from sys import stdin, stdout


def generate_catalogue(font_list):
    font_entries = ""
    for font in font_list:
        font_entry = r"""\samepage
\noindent\verb|%FONT_NAME%|\\
\begingroup
\setmainfont{%FONT_NAME%}
\resizebox{\ifdim\width>\textwidth\textwidth\else\width\fi}{!}{\hspace{4mm}{\LARGE the brown fox jumps over the lazy dog.}}
\endgroup"""

        if font.endswith("(NOT SUPPORTED)"):
            font_entry = r"\noindent\verb|%FONT_NAME%|\\"
        
        font_entry = font_entry.replace(r"%FONT_NAME%", os.path.basename(font)) + "\n\n"
        font_entries += font_entry
    stdout.write(font_entries)


if __name__ == "__main__":
    generate_catalogue([line.strip() for line in stdin])
