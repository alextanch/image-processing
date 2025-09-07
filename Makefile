.PHONY: *

## checking code format
check:
	@echo "⚫ Checking code format..."
	isort homeworks
	ruff check homeworks
	ruff format homeworks
	
## remove python file artifacts
clean-pyc:
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '*.egg-info' -exec rm -fr {} +

## remove all artifacts
clean: clean-pyc
	rm -fr .ruff_cache
	find . -name '.DS_Store' -exec rm -fr {} +
	find . -name '*.toc' -exec rm -fr {} +
	find . -name '*.gz' -exec rm -fr {} +
	find . -name '*.snm' -exec rm -fr {} +
	find . -name '*.out' -exec rm -fr {} +
	find . -name '*.nav' -exec rm -fr {} +
	find . -name '*.log' -exec rm -fr {} +
	find . -name '*.fls' -exec rm -fr {} +
	find . -name '*.aux' -exec rm -fr {} +
	find . -name '*.vrb' -exec rm -fr {} +
	find . -name '*.thm' -exec rm -fr {} +
	find . -name '*.fdb_latexmk' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +
	rm -rf lectures/_minted
