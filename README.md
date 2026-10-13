# Yap

Yap is a small Python library for turning numeric IDs into short, memorable sentences.

The idea is simple: instead of sharing an ID like `0106140103`, you can share a sentence that's easier to remember and type.

## How it works

Yap builds sentences from five word lists:

- Possessive adjective
- Family member
- Verb
- Object
- Adverb of time

Each word has a numeric index. The indexes are combined to create an ID, and the process can be reversed to get the original sentence.

For example, `my grandpa plays pizza yesterday` can be represented by a numeric ID based on the positions of its words in the lists.

## Installation

Install the package using pip:

```bash
pip install git+https://github.com/motahasf/yap.git
```

## Usage

```python
from yap import Yap

# Generate a random sentence
sentence = Yap.sentence()
print(sentence)

# Convert a sentence to an ID
id_ = Yap.to_id(sentence)
print(id_)

# Convert an ID back to a sentence
print(Yap.from_id(id_))
```

## Why?

I wanted to experiment with a simple way to make numeric IDs easier to remember and share. Yap is the result.

It's intentionally small and doesn't require external dependencies.

## Limitations

Yap isn't designed for passwords, secret tokens, or anything that needs to be secure. The sentences are just another representation of an ID, not encryption.

## License

See the LICENSE file for details.
