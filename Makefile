.PHONY: *
	
## remove all artifacts
clean: 
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

	