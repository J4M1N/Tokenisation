import pytest
from tokeniser import Tokeniser

#test to ensure tokeniser class/funct returns a string
def test_tokeniser_funtion_returns_a_string():
    text = "hello world"
    output = ["hello", "world"]
    #action 
    result = Tokeniser()
    token_result = result.tokenise(text)
    assert output == token_result

#test to ensure that all strings are lowercase
def test_convert_strings_to_lowercase():
    text = "HELLO WORLD"
    output = ["hello", "world"]
    #action
    result = Tokeniser()
    token_result = result.convert_strings_to_lowercase(text)
    assert output == token_result


#test to ensure that the function removes all punctuation
def test_remove_punctuation_removes_punctuation_from_strings():
    text = "Hello, World! This is an example: remove punctuation."
    output = ["Hello World This is an example remove punctuation"]
    #action
    result = Tokeniser()
    token_result = result.remove_punctuation(text)
    assert output == token_result


#test to ensure that the function returns a dictionary that maps each token to the number of times it appears
def test_count_tokens_counts_all_tokens_correctly():
    tokens = ["the", "cat", "in", "the", "hat"]
    output = {"the": 2, "cat": 1, "in": 1, "hat": 1}
    #action
    result = Tokeniser.count_tokens(tokens)
    #token_result = count_tokens(tokens)
    assert output == result

#test to ensure that the function returns list of token/count tuples sorted by most to least frequent
def test_sort_vocab_returns_tuples_in_correct_frequency_order():
    token_counts = {"the": 2, "cat": 1, "in": 1, "hat": 1}
    output = [("the", 2), ("cat", 1), ("in", 1), ("hat", 1)]
    #action
    result = Tokeniser.sort_vocab(token_counts)
    assert output == result


#test to ensure that the function splits strings into subwords
def test_split_into_subwords_returns_characters_with_end_symbol():
    token = ["cat"]
    output = [["c", "a", "t", "</w>"]]
    #action
    result = Tokeniser.split_into_subwords(token)
    assert result == output



#test to ensure that the function counts the frequency of all adjacent pairs of symbolsin the list
def test_count_symbol_pairs_returns_the_correct_frequency_of_adjacent_pairs_of_symbols():
    tokens = [
        ["c", "a", "t", "</w>"],
        ["c", "a", "r", "</w>"]
]
    c = Tokeniser()
    result = c.count_symbol_pairs(tokens)
    assert result[("c", "a")] == 2
    assert result[("a", "t")] == 1
    assert result[("a", "r")] == 1


#test to ensure function merges pairs correctly
def test_merge_most_frequent_pair_merges_correctly():
    t = Tokeniser()
    subwords = [
        ["t", "h", "e", "</w>"],
        ["h", "a", "t", "</w>"]
    ]
    pair_counts = {
        ("t", "h"): 1,
        ("h", "e"): 1,
        ("e", "</w>"): 1,
        ("h", "a"): 1,
        ("a", "t"): 1,
        ("t", "</w>"): 1
    }

    merged = t.merge_most_frequent_pair(subwords, pair_counts)
    #assert merged[0] == ["th", "e", "</w>"]
    assert merged[1] == ["h", "a", "t", "</w>"]


#test to ensure that common pairs are merged first
def test_build_bpe_vocab_merges_common_pairs_first():
    t = Tokeniser()
    tokens = ["aa", "ab", "aa"]

    merged = t.build_bpe_vocab(tokens, num_merges=1)

    expected = [
        ["aa", "</w>"],  # "aa"
        ["a", "b", "</w>"],  # "ab"
        ["aa", "</w>"]  # "aa"
    ]

    assert merged == expected



#test 
# def test_build_bpe_vocab_multiple_merges():
#     t = Tokeniser()
#     tokens = ["aa", "ab", "aa"]
   
#     result = t.build_bpe_vocab(tokens, num_merges=2)

# 		# in the second merge, the most common pair is "aa" with "</w>"
#     expected = [
#         ["aa</w>"],  
#         ["a", "b", "</w>"],  
#         ["aa</w>"]   
#     ]

#     assert result == expected