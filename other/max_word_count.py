import re

# returns the max words in any sentence
def solution(S):
    sentences = re.split("\.|\!|\?", S)
    num_sentences = len(sentences)
    sentence_word_lists = []
    # remove any empty words
    for i in range(num_sentences):
        words = sentences[i].strip().split(" ")
        non_empty_words = filter(lambda w: len(w) > 0, words)
        sentence_word_lists.append(non_empty_words)
    max_len = 0
    for i in range(num_sentences):
        num_words_in_sentence = len(sentence_word_lists[i])
        if num_words_in_sentence > max_len: max_len = num_words_in_sentence
    return max_len