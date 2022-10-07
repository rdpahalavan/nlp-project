# Generate Similar Words related to Context

## Sample code demonstrating the overview

Download pre-trained models here: [`Word2vec`](https://drive.google.com/uc?id=1kHrHFShYeWcI8zMnUMYb1B49Mz0DdJA3) and [`GloVe`](https://drive.google.com/uc?id=1IrvvAi0isS5zqekWgS3_KuhN-kDKuDRi).


### Usage

```
context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='bert')
```

where:
- context_name: the name of the context as string
- list_words: the list of words as list of strings
- model_name: 'word2vec' or 'glove' or 'bert' or 'gpt'

#### Output

```
{'calculation': 0.09977173805236816,
 'comparison': 0.09102193266153336,
 'calculations': 0.05838974565267563,
 'BMI': 0.056244466453790665,
 'measurement': 0.05379500240087509}
```
