# Generate Similar Words related to Context

## Sample code demonstrating the overview

Download pre-trained models here: [`Word2vec`](https://drive.google.com/uc?id=1kHrHFShYeWcI8zMnUMYb1B49Mz0DdJA3) and [`GloVe`](https://drive.google.com/uc?id=1IrvvAi0isS5zqekWgS3_KuhN-kDKuDRi).


### Usage

```
context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='word2vec')
```

where:
- context_name: the name of the context as string
- list_words: the list of words as list of strings
- model_name: 'word2vec' or 'glove' or 'bert' or 'gpt'
