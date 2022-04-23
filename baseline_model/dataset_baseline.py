import torch
from collections import Counter
import pandas as pd

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class Dataset(torch.utils.data.Dataset):
    def __init__(self, sequence_length):
        self.sequence_length = sequence_length
        self.words = self.load_words()
        self.uniq_words = self.get_uniq_words()

        self.index_to_word = {index: word for index, word in enumerate(self.uniq_words)}
        self.word_to_index = {word: index for index, word in enumerate(self.uniq_words)}
        self.words_indexes = [self.word_to_index[w] for w in self.words]

    def load_words(self):
        train_df = pd.read_csv('clean_tweets.csv')
        text = train_df.tweet.str.cat(sep=' ')
        return(text.split(' '))

    def get_uniq_words(self):
        word_counts = Counter(self.words)
        return sorted(word_counts, key=word_counts.get, reverse=True)
    
    def __len__(self):
        return(len(self.words_indexes) - self.sequence_length)

    def __getitem__(self, index):
        return (
            torch.tensor(self.words_indexes[index:index+self.sequence_length]).to(device),
            torch.tensor(self.words_indexes[index+1:index+self.sequence_length+1]).to(device),
        )
