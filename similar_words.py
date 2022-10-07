### install the required packages
# pip install gensim
# pip install torch
# pip install transformers datasets
# pip install yake

import pprint
import yake
from transformers import pipeline
from gensim.models import KeyedVectors
from difflib import SequenceMatcher

word_vectors = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
glove_vectors = KeyedVectors.load_word2vec_format('glove.42B.300d.word2vec.txt')

masked_model = pipeline(task="fill-mask", model='distilroberta-base')
generation_model = pipeline(task="text-generation", model='gpt2')


def context_related_words(context_name, list_words, model_name):
    output_similar_dict = {}
    list_to_fed = [context_name] + list_words + [context_name]

    if model_name == 'word2vec':
        similar_words = word_vectors.most_similar(positive=list_to_fed)
    elif model_name == 'glove':
        list_to_fed = [word.lower() for word in list_to_fed]
        similar_words = glove_vectors.most_similar(positive=list_to_fed)

    if model_name == 'word2vec' or model_name == 'glove':
        for result in similar_words:
            flag = True
            for word in list_to_fed:
                if SequenceMatcher(None, result[0], word).ratio() > 0.7:
                    flag = False
            if flag and len(output_similar_dict) < 5:
                output_similar_dict[result[0]] = result[1]

    if model_name == 'bert':

        string_to_fed = f"In {context_name}, {', '.join(list_words)} are used for <mask>."
        similar_words = masked_model(string_to_fed, top_k=10)
        for result in similar_words:
            flag = True
            for word in list_to_fed:
                if SequenceMatcher(None, result['token_str'].strip(), word).ratio() > 0.7:
                    flag = False
            if flag and len(output_similar_dict) < 5:
                output_similar_dict[result['token_str'].strip()] = result['score']

    elif model_name == 'gpt':

        string_to_fed = f"In {context_name}, {', '.join(list_words)} are used for"
        similar_words = generation_model(string_to_fed, max_length=25, num_return_sequences=5, pad_token_id=50256)
        keyword_extractor = yake.KeywordExtractor(lan='en', n=2, top=10)
        for result in similar_words:
            keywords = keyword_extractor.extract_keywords(result['generated_text'])
            for keyword in keywords:
                flag = True
                for word in list_to_fed:
                    if SequenceMatcher(None, keyword[0], word).ratio() > 0.7:
                        flag = False
                if flag and len(output_similar_dict) < 5:
                    output_similar_dict[keyword[0]] = keyword[1]
                    break
        output_similar_dict = dict(sorted(output_similar_dict.items(), key=lambda item: item[1]))

    return output_similar_dict


pprint.pprint(context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='word2vec'))
pprint.pprint(context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='glove'))
pprint.pprint(context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='bert'))
pprint.pprint(context_related_words(context_name='Health', list_words=['Weight', 'Height'], model_name='gpt'))
