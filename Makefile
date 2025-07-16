.PHONY: generate
generate:
	python ./scripts/generator.py

lint:
	pylint ./scripts/generator.py

.PHONY: clean
clean:
	rm -rf ./generated/*
