"""A small dependency-free Markov-chain text generator."""

import argparse
import re
from collections import defaultdict
from pathlib import Path
from random import Random


TOKEN_PATTERN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*|[^\w\s]", re.UNICODE)
WORD_PATTERN = re.compile(r"^[^\W_]+(?:['’][^\W_]+)*$", re.UNICODE)
SENTENCE_ENDINGS = frozenset((".", "!", "?"))
NO_SPACE_BEFORE = frozenset((".", ",", "!", "?", ";", ":", "%", ")", "]", "}"))
NO_SPACE_AFTER = frozenset(("(", "[", "{"))


def tokenize(text):
    """Split Unicode text into words and punctuation tokens."""

    return TOKEN_PATTERN.findall(text)


def detokenize(tokens):
    """Join tokens with readable spacing around common punctuation."""

    output = ""
    previous = None
    for token in tokens:
        if not output or token in NO_SPACE_BEFORE or previous in NO_SPACE_AFTER:
            output += token
        else:
            output += " " + token
        previous = token
    return output


class MarkovChain:
    """An order-N token chain trained from an in-memory corpus."""

    def __init__(self, tokens, order=1):
        if order < 1:
            raise ValueError("Markov order must be at least 1")
        if len(tokens) <= order:
            raise ValueError(
                "Corpus must contain more tokens than the Markov order"
            )

        self.order = order
        self.transitions = defaultdict(list)
        self.starts = []

        first_context = tuple(tokens[:order])
        self.starts.append(first_context)
        for index in range(len(tokens) - order):
            context = tuple(tokens[index:index + order])
            next_token = tokens[index + order]
            self.transitions[context].append(next_token)

            if index > 0 and tokens[index - 1] in SENTENCE_ENDINGS:
                self.starts.append(context)

    @classmethod
    def from_text(cls, corpus, order=1):
        """Train a Markov chain from plain text."""

        if corpus is None or not corpus.strip():
            raise ValueError("Corpus must not be empty")
        return cls(tokenize(corpus), order=order)

    def generate(self, max_words=50, seed=None):
        """Generate at most ``max_words`` words using an optional seed."""

        if max_words < 1:
            raise ValueError("Maximum words must be at least 1")

        random_generator = Random(seed)
        context = random_generator.choice(self.starts)
        generated = list(context)

        while self._word_count(generated) < max_words:
            choices = self.transitions.get(context)
            if not choices:
                break
            generated.append(random_generator.choice(choices))
            context = tuple(generated[-self.order:])

        while generated and self._word_count(generated) > max_words:
            generated.pop()
        return detokenize(generated)

    @staticmethod
    def _word_count(tokens):
        return sum(bool(WORD_PATTERN.match(token)) for token in tokens)


def generate_text(corpus, max_words=50, order=1, seed=None):
    """Train a chain and generate text in one call."""

    return MarkovChain.from_text(corpus, order=order).generate(
        max_words=max_words,
        seed=seed,
    )


def build_parser():
    parser = argparse.ArgumentParser(
        description="Generate text from a UTF-8 corpus using a Markov chain",
    )
    parser.add_argument("corpus", help="path to a plain-text corpus")
    parser.add_argument(
        "--words",
        type=int,
        default=50,
        help="maximum generated words; defaults to 50",
    )
    parser.add_argument(
        "--order",
        type=int,
        default=1,
        help="number of preceding tokens in each state; defaults to 1",
    )
    parser.add_argument("--seed", type=int, help="reproducible random seed")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        corpus = Path(args.corpus).read_text(encoding="utf-8")
        generated = generate_text(
            corpus,
            max_words=args.words,
            order=args.order,
            seed=args.seed,
        )
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))
    print(generated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
