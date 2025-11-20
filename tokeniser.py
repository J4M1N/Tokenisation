import re
import string 
from typing import List, Tuple, Dict
from collections import defaultdict
from collections import Counter
class Tokeniser:
    
    END_OF_WORD_SYMBOL = "</w>"
    
    def tokenise(self, text: str):
        return text.split()


    def convert_strings_to_lowercase(self, text:str):
        #list = []
        lowercase_string = text.lower().split()          #split(text.lower())
        return lowercase_string
        
    def remove_punctuation(self, text:str):  
        list = [] 
        clean_punct = ''.join([char for char in text if char not in string.punctuation])
        list.append(clean_punct)
        return list
    

    def count_tokens(tokens: list[str]) -> dict[str, int]:
        token_count = {}
        for token in tokens:
            if token in token_count:
                token_count[token] += 1
            else:
                token_count[token] = 1
        return token_count
    

    def sort_vocab(token_counts: dict[str, int]) -> list[tuple[str, int]]:
        sorted_tokens = sorted(token_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_tokens
    

    def split_into_subwords(tokens: list[str]) -> list[list[str]]:
        return [list(token) + ["</w>"] for token in tokens]
        #words = list
        #return [list(word) + ["</w>"] for word in words]


    def count_symbol_pairs(self, subword_tokens):
        pair_counts = {}
    
        for token_list in subword_tokens:
            pair_counts = defaultdict(int)
        
        for token_list in subword_tokens:
            for i in range(len(token_list) - 1):
                pair = (token_list[i], token_list[i + 1])
                pair_counts[pair] += 1

        return dict(pair_counts)
        #      for i in range(len(token_list) - 1):
        #         pair = (token_list[i], token_list[i + 1])
        #         pair_counts[pair] += 1
        
        # return pair_counts
    def merge_most_frequent_pair(
    self,
    subword_tokens: list[list[str]],
    pair_counts: dict[tuple[str, str], int]		
) -> list[list[str]]:
        if not pair_counts:
            return subword_tokens, None

        most_frequent_pair = max(pair_counts.items(), key=lambda x: x[1])[0]
        first, second = most_frequent_pair
        merged_token = first + second
        merged_tokens = []
        skip = False
        for tokens in subword_tokens:
            new_tokens = []
            i = 0
            
        while i < len(tokens):
                if i < len(tokens) - 1 and (tokens[i], tokens[i+1]) == most_frequent_pair:
                    new_tokens.append(tokens[i] + tokens[i+1])
                    i += 2 
                else:
                    new_tokens.append(tokens[i])
                    i += 1
                    merged_tokens.append(new_tokens)

        return merged_tokens
    

    def build_bpe_vocab(
    self,
    tokens: list[str],
    num_merges: int
) -> list[list[str]]:
        vocab = Counter()
        for token in tokens:
            word = tuple(token) + ("</w>",)
            vocab[word] += 1

        for _ in range(num_merges):
            pairs = set()
        prev_char = word[0]
        for char in word[1:]:
            pairs.add((prev_char, char))
            prev_char = char
        #return pairs
            pairs = Counter()
        for word, freq in vocab.items():
            for pair in pairs(word):
                pairs[pair] += freq

            if not pairs:
                break
            best_pair = max(pairs, key=pairs.get)
            new_vocab = {}
            for word, freq in vocab.items():
                new_word = []
                i = 0
                while i < len(word):
                    if i < len(word) - 1 and (word[i], word[i+1]) == best_pair:
                        new_word.append(word[i] + word[i+1])
                        i += 2
                    else:
                        new_word.append(word[i])
                        i += 1
                new_vocab[tuple(new_word)] = freq
            vocab = new_vocab
            final_vocab = {"".join(word): freq for word, freq in vocab.items()}
        return final_vocab