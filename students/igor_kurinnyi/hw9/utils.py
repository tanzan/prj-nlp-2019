import tokenize_uk
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='uk')


def tokenize_text(text):
    text = tokenize_uk.tokenize_text(text)

    tok_text = list()
    for par in text:
        jpar = [' '.join(sent) for sent in par]
        jpar = ' '.join(jpar)
        tok_text.append(jpar)

    tok_text = '\n\n'.join(tok_text)
    return tok_text


def lemmatize(text):
    tokens = [t for t in tokenize_uk.tokenize_words(text)]
    lemmas = [morph.parse(t)[0].normal_form for t in tokens]
    return ' '.join(lemmas)