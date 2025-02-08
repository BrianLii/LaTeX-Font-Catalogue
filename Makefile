.PHONY: clean

catalogue.pdf: catalogue.tex
	xelatex \
		-interaction=nonstopmode \
		-file-line-error \
		-output-directory=.build \
		catalogue.tex
	cp .build/catalogue.pdf .

catalogue.tex: generate_catalogue.py template/catalogue.tex
	fc-list :charset=0061-007a family style file | \
	grep -E '.*/texlive/2024/texmf-dist/fonts/.*\.(ttf|otf):' | \
	tee fc-list-result | \
	python generate_catalogue.py

clean:
	rm -rf catalogue.tex catalogue.pdf