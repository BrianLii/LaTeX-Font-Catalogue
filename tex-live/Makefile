.PHONY: clean

catalogue.pdf: catalogue.tex
	mkdir -p .build
	xelatex \
		-interaction=nonstopmode \
		-file-line-error \
		-output-directory=.build \
		catalogue.tex
	cp .build/catalogue.pdf .

catalogue.tex: generate_catalogue.py template/catalogue.tex
	mkdir -p .build
	fc-list :charset=0061-007a family style file | \
	grep -E '.*/texlive/2024/texmf-dist/fonts/.*\.(ttf|otf):' | \
	tee .build/fc-list-result.txt | \
	python generate_catalogue.py

clean:
	rm -rf .build