from torch import nn, optim
from torch.utils.data import DataLoader

def train(dataset, model, batch_size, max_epochs):
    model.train()

    dataloader = DataLoader(dataset, batch_size=batch_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(max_epochs):
        state_h, state_c = model.init_state(dataset.sequence_length)

        for batch, (x,y) in enumerate(dataloader):
            optimizer.zero_grad()

            y_pred, (state_h, state_c) = model(x, (state_h, state_c))
            loss = criterion(y_pred.transpose(1,2), y)

            state_h = state_h.detach()
            state_c = state_c.detach()

            loss.backward()
            optimizer.step()

            if batch % 100 == 0:
                print({ 'epoch': epoch, 'batch': batch, 'loss': loss.item() })
