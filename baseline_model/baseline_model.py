import torch.nn as nn
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

class BaselineModel(nn.Module):
    def __init__(self, dataset, lstm_size=128, embedding_dim=128, num_layers=3):
        super(BaselineModel, self).__init__()
        self.lstm_size = lstm_size
        self.embedding_dim = embedding_dim
        self.num_layers=3

        vocab_size = len(dataset.uniq_words)

        self.embedding = nn.Embedding(
                num_embeddings=vocab_size,
                embedding_dim=self.embedding_dim
        )
        self.lstm = nn.LSTM(
            input_size = self.embedding_dim,
            hidden_size = self.lstm_size,
            num_layers=self.num_layers,
            dropout=0.2
        )
        self.fc = nn.Linear(self.lstm_size, vocab_size)

    def forward(self, x, prev_state):
        embed = self.embedding(x)
        output, state = self.lstm(embed, prev_state)
        logits = self.fc(output)
        return(logits, state)
    
    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.lstm_size).to(device),
                torch.zeros(self.num_layers, sequence_length, self.lstm_size).to(device))

