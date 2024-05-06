from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, X, y, transform=None) -> None:
        self.X = X
        self.y = y
        self.transform = transform
    
    def __len__(self): #lenを適用したときの挙動を定義
        return len(self.X)
    
    def __getitem__(self, idx): #indexingしたときの挙動
        X = self.X[idx]
        y = self.y[idx]

        if self.transform:
            X = self.transform(X)
        
        return X, y
    

