# textgen
Few experiments with text generation

## How to run

JSON files can be executed using [simple-grammar](https://github.com/adrianogil/simplegrammar)

```bash
simple-grammar japanese/n5/2023/02/11/basic_sentences.json
```

## Markov-chain generator

Generate text from any UTF-8 plain-text corpus without extra dependencies:

```bash
PYTHONPATH=src/python python -m textgen.markov corpus.txt --words 40 --seed 17
PYTHONPATH=src/python python -m textgen.markov corpus.txt --order 2 --words 80
```

`--order` controls how many preceding tokens form each chain state. The same
corpus, options, and `--seed` produce the same generated text.
