# 🗣️ What Is Yap?

**Yap** turns boring numeric IDs into **unique, memorable sentences** with Python.

Instead of:

```text
0106140103
```

you get:

> **"my grandpa plays pizza yesterday."**

Yeah, it's a little weird.

But you'll remember it. :)

---

# Why Yap?

Numeric IDs are great for computers, but not so great for humans.

Yap gives you a simple way to turn them into something **human-readable and memorable**.

```text
0106140103
      ↕
my grandpa plays pizza yesterday.
```

No database required.

---

# Features

* 🎲 Generate random Yap sentences
* 🔢 Convert sentences → IDs
* 🔄 Convert IDs → sentences
* ✅ Input validication
* 🗄️ No database required

---

# Usage

### Generate a sentence

```python
from yap import Yap

sentence = Yap.sentence()

print(sentence)
```

Output:

```text
their uncle reads coffee tomorrow.
```

### Sentence → ID

```python
Yap.to_id("my grandpa plays pizza yesterday.")
```

Output:

```text
0106140103
```

### ID → Sentence

```python
Yap.from_id("0106140103")
```

Output:

```text
my grandpa plays pizza yesterday.
```

---

# How Does It Work?

Each sentence has five parts:

```text
Possessive adjective
        +
Family noun
        +
Verb
        +
Object
        +
Time adverb
```

Each word has a position in its list, which becomes a two-digit number.

For example:

```text
my          → 01
grandpa     → 06
plays       → 14
pizza       → 01
yesterday   → 03
```

Result:

```text
0106140103
```

---

# Requirements

* Python 3.x
* No external dependencies

---

# 🔐 Security Note

Yap is **memorable, not magical.**

It's not a password generator, secret key generator, or anything like that.

Use it for **public, non-sensitive stuff** like posts, products, links, and demos.

Basically:

> If someone finds your Yap, don't panic.
> Just don't use it to protect your bank account. :)

---

# 🚧 Project Status

Yap is still a small project, and it's just getting started.

More words and features are coming :)

