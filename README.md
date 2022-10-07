# Generate Similar Words related to Context

## Sample code demonstrating the overview of the project

Download pre-trained models here: [`Word2vec`](https://drive.google.com/uc?id=1kHrHFShYeWcI8zMnUMYb1B49Mz0DdJA3) and [`GloVe`](https://drive.google.com/uc?id=1IrvvAi0isS5zqekWgS3_KuhN-kDKuDRi).

The pre-trained models used for BERT and GPT are [`distilroberta-base`](https://huggingface.co/distilroberta-base) and [`gpt2`](https://huggingface.co/gpt2).


### Usage

``` python
context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='bert')
```

where:
- context_name: the name of the context as string
- list_words: the list of words as list of strings
- model_name: `word2vec` or `glove` or `bert` or `gpt`

#### Output

``` python
{'calculation': 0.09977173805236816,
 'comparison': 0.09102193266153336,
 'calculations': 0.05838974565267563,
 'BMI': 0.056244466453790665,
 'measurement': 0.05379500240087509}
```

#### Examples

``` python
>>> context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='word2vec')
{'Wellness': 0.5733888745307922,
 'Flu_Vaccination': 0.5551058053970337,
 'H#N#_Vaccination': 0.5550900101661682,
 'Inc_CHSI': 0.5415679812431335,
 'Primary_Care': 0.5376291275024414}

>>> context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='glove')
{'care': 0.7019988894462585,
 'nutrition': 0.6805460453033447,
 'loss': 0.6535139083862305,
 'medical': 0.6476573944091797,
 'benefits': 0.6456916928291321}
 
>>> context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='bert')
{'calculation': 0.09977173805236816,
 'comparison': 0.09102193266153336,
 'calculations': 0.05838974565267563,
 'BMI': 0.056244466453790665,
 'measurement': 0.05379500240087509}
 
>>> context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='gpt')
{'includes BMI': 0.01740393982310274,
 'weight loss': 0.02211393890070178,
 'weight maintenance': 0.02995329403445712,
 'waist measurement': 0.03529725379306155,
 'weight regain': 0.042867082342497295}
 
>>> context_related_words(context_name='Intrusion Detection', list_words=['IP address', 'Request', 'Service'], model_name='gpt')
{'network connection': 0.02570861714399338,
 'intruder identity': 0.04449651730999523,
 'device type': 0.04832347995175229,
 'malware infection': 0.04940384002065631,
 'Detection': 0.06588837669267192}
 
>>> context_related_words(context_name='Intrusion Detection', list_words=['IP address', 'Request', 'Service'], model_name='bert')
{'authentication': 0.215494304895401,
 'verification': 0.09136611223220825,
 'detection': 0.08709023892879486,
 'scanning': 0.025745250284671783,
 'filtering': 0.021444883197546005}
```
