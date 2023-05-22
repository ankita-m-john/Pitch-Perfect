#%matplotlib inline
import torchvision.datasets as dataset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
import matplotlib.pyplot as plt
import torchvision.utils
import numpy as np
import random
from PIL import Image
import torch
from torch.autograd import Variable
import PIL.ImageOps    
import torch.nn as nn
from torch import optim
import torch.nn.functional as F
from songrec import SiameseNetwork

train_dir ='D:/Main Project/Pitch-Perfect/plots/song.png'
test_dir = 'D:/Main Project/Pitch-Perfect/plots/song1.png'   

print("Alia1")

image1 = Image.open(train_dir)
image2 = Image.open(test_dir)

class Siamese(Dataset):
    print("Alia2")
    def __init__(self, image1, image2, transform = None, invert = False):
        self.image1 = image1
        self.image2 = image2
        self.transform = transform
        self.invert = invert

    def __getitem__(self, index):
        sample_1=self.image1
        sample_2=self.image2
        img_1 = sample_1.convert("L")
        img_2 = sample_2.convert("L")

        if self.invert:
            img_1 = PIL.ImageOps.invert(img_1)
            img_2 = PIL.ImageOps.invert(img_2)
        
        if self.transform:
            img_1 = self.transform(img_1)
            img_2 = self.transform(img_2)  

        return img_1, img_2, torch.from_numpy(np.array([int(sample_1 != sample_2)], dtype = np.float32))  
    
siamese_dataset = Siamese(image1=image1, image2=image2,
                                 transform=transforms.Compose([transforms.Resize((100, 100)), transforms.ToTensor()]), 
                                 invert=False)
print("Alia3")
def imshow(img, text=None):
    np_img = img.numpy()
    plt.axis("off")
    if text:
        plt.text(75, 8, text, style='italic', fontweight='bold', bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
    plt.imshow(np.transpose(np_img, (1, 2, 0)))
    plt.show()    

# def show_plot(iteration,loss):
#     print("Alia4")
#     plt.plot(iteration,loss)
#     plt.show()

class SiameseNetwork(nn.Module):
    def __init__(self):
        super(SiameseNetwork, self).__init__()
        print("Alia5")
        self.reflection_pad = nn.ReflectionPad2d(1)
        self.conv1 = nn.Conv2d(1, 4, kernel_size=3)
        self.conv2 = nn.Conv2d(4, 8, kernel_size=3)
        self.conv3 = nn.Conv2d(8, 8, kernel_size=3) 
        self.relu = nn.ReLU(inplace=True)
        self.batch_norm1 = nn.BatchNorm2d(4)
        self.batch_norm2 = nn.BatchNorm2d(8) 
        self.fc1 = nn.Linear(8 * 100 * 100, 500)
        self.fc2 = nn.Linear(500, 500)
        self.fc3 = nn.Linear(500, 5)
        
    def forward_one_branch(self, x):
        x = self.batch_norm1(self.relu(self.conv1(self.reflection_pad(x))))
        x = self.batch_norm2(self.relu(self.conv2(self.reflection_pad(x))))        
        x = self.batch_norm2(self.relu(self.conv3(self.reflection_pad(x))))   
        x = x.view(x.size()[0], -1)
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))        
        x = self.fc3(x)
        
        return x
        
    def forward(self, input1, input2):
        output1 = self.forward_one_branch(input1)
        output2 = self.forward_one_branch(input2)     
        
        return output1, output2
    

model = torch.load("D:/Main Project/Pitch-Perfect/SNN model/ModelSNN.pth", map_location=torch.device('cpu'))

model = SiameseNetwork()

a,_,_=siamese_dataset[0]
a = a.unsqueeze(0)    
_,b,label=siamese_dataset[1]
b = b.unsqueeze(0)   


merged = torch.cat((a,b), 0)
output1, output2 = model(Variable(a), Variable(b))
distance = F.pairwise_distance(output1, output2)
#imshow(torchvision.utils.make_grid(merged), 'Similarity: {:.2f}'.format(distance.item()))
# imshow(torchvision.utils.make_grid(merged), 'Similarity: {:.2f}'.format(100-(100*(distance.item())))) Undo this to see
Score = (100-(100*(distance.item())))
print(Score)
#imshow(torchvision.utils.make_grid(merged), 'Similarity: {:.2f}'.format(100-(100*(distance.item()/0.5))))