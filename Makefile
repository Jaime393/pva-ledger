repro:
	python3 cli.py record README.md

reproduce:
	python3 cli.py record README.md

dev:
	python cli.py --help

test:
	python3 -m unittest discover -s tests -v
