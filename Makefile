BOOK	:= parabolized-navier-stokes

all:	docs

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install -U pip
	pip install -r requirements.txt
	cp /files/tikzmagic.py .direnv/python3.9.7/lib/python3.9/site-packages

.PHONY: docs
docs:
	jupyter-book build $(BOOK)/
	cp -R $(BOOK)/_build/html/ docs

.PHONY: nb
nb:
	cd $(BOOK) && \
		jupyter notebook
