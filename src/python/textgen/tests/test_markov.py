import re

import pytest

from textgen import markov


CORPUS = "The cat sleeps. The cat eats. The dog runs."


def test_tokenize_and_detokenize_preserve_words_and_punctuation():
    tokens = markov.tokenize("L'été arrive, enfin!")

    assert tokens == ["L'été", "arrive", ",", "enfin", "!"]
    assert markov.detokenize(tokens) == "L'été arrive, enfin!"


def test_seeded_generation_is_reproducible():
    first = markov.generate_text(CORPUS, max_words=8, seed=23)
    second = markov.generate_text(CORPUS, max_words=8, seed=23)

    assert first == second
    assert len(re.findall(r"[^\W_]+(?:['’][^\W_]+)*", first)) <= 8


def test_higher_order_chain_uses_requested_context_size():
    chain = markov.MarkovChain.from_text(CORPUS, order=2)

    assert chain.order == 2
    assert chain.transitions[("The", "cat")] == ["sleeps", "eats"]


def test_generation_starts_at_a_sentence_boundary():
    chain = markov.MarkovChain.from_text(CORPUS)

    assert set(chain.starts) == {("The",)}
    assert chain.generate(max_words=1, seed=5) == "The"


@pytest.mark.parametrize(
    ("corpus", "order", "message"),
    [
        ("", 1, "Corpus must not be empty"),
        ("one", 1, "more tokens than the Markov order"),
        ("one two", 0, "Markov order must be at least 1"),
    ],
)
def test_invalid_training_inputs_have_clear_errors(corpus, order, message):
    with pytest.raises(ValueError, match=message):
        markov.MarkovChain.from_text(corpus, order=order)


def test_generate_rejects_non_positive_word_limit():
    chain = markov.MarkovChain.from_text(CORPUS)

    with pytest.raises(ValueError, match="Maximum words must be at least 1"):
        chain.generate(max_words=0)


def test_cli_reads_utf8_corpus_and_prints_generated_text(tmp_path, capsys):
    corpus_path = tmp_path / "corpus.txt"
    corpus_path.write_text("Olá mundo. Olá Python.", encoding="utf-8")

    exit_code = markov.main(
        [str(corpus_path), "--words", "4", "--order", "1", "--seed", "7"]
    )

    assert exit_code == 0
    assert capsys.readouterr().out.strip()
