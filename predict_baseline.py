import torch
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def predict(dataset, model, text, next_words=100):
    model.eval()

    words = text.lower().split(' ')
    state_h, state_c = model.init_state(len(words))

    for i in range(0, next_words):
        try:
            x = torch.tensor([[dataset.word_to_index[w] for w in words[i:]]]).to(device)
        except:
            words_index = []
            for w in words[i:]:
                if w in dataset.word_to_index:
                    words_index.append(dataset.word_to_index[w])
                else:
                    words_index.append(0)
            x = torch.tensor([words_index]).to(device)
        y_pred, (state_h, state_c) = model(x, (state_h, state_c))

        last_word_logits = y_pred[0][-1]
        p = torch.nn.functional.softmax(last_word_logits, dim=0).detach().cpu().numpy()
        word_index = np.random.choice(len(last_word_logits), p=p)
        words.append(dataset.index_to_word[word_index])

    words[0] = words[0][0].upper() + words[0][1:]
    return " ".join(words)