from random import choice

# Sentence components

possessive_adjectives = [
    "my", "your", "his", "her",
    "its", "our", "your", "their"
]

family_nouns = [
    "father", "mother", "son", "daughter", "sister",
    "grandpa", "grandma", "grandson", "granddaughter",
    "uncle", "aunt", "cousin", "husband", "wife"
]

verbs = [
    "eats", "drinks", "goes", "comes", "sees", "looks",
    "watches", "reads", "writes", "speaks", "listens",
    "plays", "works", "studies", "sleeps", "runs",
    "walks", "buys", "makes"
]

objects = [
    "pizza", "book", "car", "water", "coffee",
    "food", "apple", "phone", "computer", "movie",
    "song", "letter", "message", "ball", "game",
    "homework", "music", "cake", "sandwich",
    "story"
]

time_adverbs = [
    "today", "tomorrow", "yesterday", "now", "tonight",
    "soon", "later", "already", "still", "yet", "always",
    "usually", "often", "sometimes", "rarely",
    "never", "early", "late", "recently", "soon"
]


class Yap:

    @staticmethod
    def sentence():

        """Generate and return a random sentence."""
        
        pa = choice(possessive_adjectives)
        fa = choice(family_nouns)
        ve = choice(verbs)
        ob = choice(objects)
        ta = choice(time_adverbs)
        
        generated_sentence = f"{pa} {fa} {ve} {ob} {ta}."

        return generated_sentence

    @staticmethod
    def to_id(sentence: str):

        """Convert a sentence into its numeric ID."""

        # Validication
        if not isinstance(sentence, str):
            raise TypeError("Give me sentence first :)")

        # Normalization
        sentence = sentence.strip().removesuffix(".")

        # Unpack sentence

        try:
            pa, fa, ve, ob, ta = sentence.split()
        except ValueError:
            raise ValueError("cannot unpack your sentence :)")

        # Convert words to numbers
        
        try:
            num_pa = possessive_adjectives.index(pa) + 1
            num_pa = str(num_pa).zfill(2)
            
            num_fa = family_nouns.index(fa) + 1
            num_fa = str(num_fa).zfill(2)
            
            num_ve = verbs.index(ve) + 1
            num_ve = str(num_ve).zfill(2)
            
            num_ob = objects.index(ob) + 1
            num_ob = str(num_ob).zfill(2)
            
            num_ta = time_adverbs.index(ta) + 1
            num_ta = str(num_ta).zfill(2)
        except ValueError:
            raise ValueError("Invalid sentence")
        
        # Wrapping numbers
        
        numerical_id = f"{num_pa}{num_fa}{num_ve}{num_ob}{num_ta}"
        
        return numerical_id

