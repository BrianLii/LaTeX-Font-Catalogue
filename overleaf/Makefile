FONT_FILES = Blackletter Cursive Handwriting Heavy-faces Monospaced Sans-serif Serif
OUTPUT_DIR = .build/overleaf

.PHONY: clean all

all: overleaf.zip

$(OUTPUT_DIR)/%.tex: fonts/%.txt generate_overleaf.py
	mkdir -p $(OUTPUT_DIR)
	python generate_overleaf.py < $< > $@

overleaf.zip: $(FONT_FILES:%=$(OUTPUT_DIR)/%.tex) main.tex
	zip -j overleaf.zip $(OUTPUT_DIR)/*.tex main.tex

clean:
	rm -rf .build