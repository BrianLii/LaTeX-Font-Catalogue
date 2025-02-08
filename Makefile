.PHONY: clean

catalogue.pdf: catalogue.tex
	xelatex \
		-interaction=nonstopmode \
		-file-line-error \
		-output-directory=.build \
		catalogue.tex
	cp .build/catalogue.pdf .

catalogue.tex: generate_catalague.py template/catalogue.tex
	fc-list :charset=0061-007a family style file | \
	grep "texlive/2024/texmf-dist/fonts/.*\.\(otf\|ttc\)" | \
	tee fc-list-result | \
	python generate_catalague.py

clean:
	rm -rf catalogue.tex catalogue.pdf