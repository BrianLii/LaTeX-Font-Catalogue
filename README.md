# LaTeX Font Catalogue
## Overview

The **LaTeX Font Catalogue** project provides a visual guide to fonts available in **Overleaf** and **TeX Live** environments.  

- **TeX Live**: Using `fontspec`, the project loads `.ttf` and `.otf` fonts (discovered via `fc-list`) and generates a PDF catalogue displaying each font family's name and appearance.  
- **Overleaf**: Supported OTF/TTF fonts for each letterform are listed in [this post](https://www.overleaf.com/learn/latex/Questions/Which_OTF_or_TTF_fonts_are_supported_via_fontspec%3F). To visualize them, I created separate PDFs (**Sans-serif.pdf, Serif.pdf, etc.**), each displaying the names and appearances of the corresponding fonts. The source code is packaged as a ZIP file for direct upload to Overleaf.  

Note: While the [TUG Font Catalogue](https://tug.org/FontCatalogue/) lists many fonts, a significant number are not included. There may also be discrepancies between the fonts listed there and those included in the current TeX Live installation, so you're encouraged to compare the two. This catalogue is designed for users who prefer not to install additional fonts when using a local TeX Live setup.

Lastly, If you find this catalogue useful, feel free to give it a star. Contributions via PR are always welcome!

## Overleaf Font Catalogue
- [Serif.pdf](generated/overleaf/Serif.pdf)
- [Sans-serif.pdf](generated/overleaf/Sans-serif.pdf)
- ... (more in [generated/overleaf](generated/overleaf/)) 


## TeX Live Font Catalogue
- [catalogue.pdf](generated/tex-live/catalogue.pdf)


## Build  

This project provides scripts to:  
1. Test the availability of fonts on Overleaf.  
2. Generate a font catalogue for your TeX Live installation.  

**Prerequisites:** Python, `make`  

### Overleaf  

To test and generate the Overleaf font catalogue:  

1. Navigate to the [overleaf](overleaf) directory.  
2. The font list from Overleaf is pre-copied. To update it, modify [fonts](overleaf/fonts).  
3. Run `make` to generate `overleaf.zip`.  
4. Upload `overleaf.zip` to Overleaf.  
5. In `main.tex`, select the desired letterform.  
6. Compile `main.tex` with `XeLaTeX` on Overleaf to generate the font catalogue PDFs.  

### TeX Live  

To generate the font catalogue for your local TeX Live installation:  

1. Navigate to the [tex-live](tex-live) directory.  
2. If needed, update the TeX Live path in the `Makefile` (e.g., replace `/texlive/2024` with your version).  
3. Run `make` to generate the catalogue.  


## Notes & Limitations
- **Important Reminder:**  
  Avoid attempting to load every TeX Live font in one go. Loading all fonts can cause memory issues in XeLaTeX or LuaLaTeX, resulting in misleading error messages.

- **Style Variants:**  
  Some font families include only Bold/Italic styles. Currently, only the first `.ttf` or `.otf` file discovered is displayed.
- **Automatic Classification:**  
  The `fc-list` tool does not indicate whether a font is serif or sans-serif, so the project cannot automatically mimic the classification seen in resources like the TUG Font Catalogue.
- **Future Enhancements:**  
  - Linking the individual PDFs with an index page for a single-document view.
  - Improved handling of multiple font styles within a family.
