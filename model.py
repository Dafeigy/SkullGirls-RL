import torch.nn as nn
import torch
import cv2
import numpy as np


class SeqView(nn.Module):
    '''
    Use build-in function  `view()` in `nn.Sequential()`
    '''
    def __init__(self, *args) -> None:
        super(SeqView, self).__init__()
        self.shape = args

    def forward(self,x):
        return x.view(self.shape)

class Resblock(nn.Module):
    def __init__(self,in_channel, out_channel, stride=1):
        super(Resblock, self).__init__()
        self.in_channel = in_channel
        self.out_channel = out_channel
        self.stride = stride
        self.downsample = nn.Sequential(
            nn.Conv2d(in_channel, out_channel,1,stride)
        ) if stride !=1 else lambda x:x

        self.res = nn.Sequential(
            nn.Conv2d(in_channels=self.in_channel, out_channels=self.out_channel, kernel_size=3, stride=self.stride, padding=1),
            #nn.BatchNorm2d(),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=self.out_channel, out_channels=self.out_channel, kernel_size=3,stride=1, padding=1),
            #nn.BatchNorm2d(),
            nn.ReLU(inplace=True)
        )


    def forward(self, x):

        output = self.res(x)        # [64, 508, 356]

        sample = self.downsample(x) # [64, 510, 358]

        output += sample

        return output

class SKGNet(nn.Module):
    def __init__(self, outputdim):
        # RGB image size [1280,720] as input,
        super(SKGNet, self).__init__()
        self.outputdim = outputdim
        self.stage1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64,kernel_size=3, stride=2),
            nn.ReLU(True),
            nn.MaxPool2d(kernel_size=2, stride=1)
        )
        self.stage2 = self.build_layer(64,64,2)
        self.stage3 = self.build_layer(64,128,2,2)
        self.stage4 = self.build_layer(128,256,2,2)
        self.stage5 = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            SeqView(256),
            nn.Linear(256, outputdim)
        )
        
    def build_layer(self, in_feature, out_feature, block_num=2, stride=1):
        layer = nn.Sequential(
            Resblock(in_channel= in_feature, out_channel= out_feature, stride= stride),
        )
        for _ in range(1,block_num):
            layer.append(
                Resblock(in_channel=out_feature, out_channel= out_feature, stride=stride)
            )
        return layer

    def forward(self,x):

        x = self.stage1(x)  # [3, 1280,358] -> [64,510,358]
        x = self.stage2(x)  # [64,510,358] -> [64,510,358]
        x = self.stage3(x)  # [64,510,358] -> [128,128,90]
        x = self.stage4(x)  # [128,128,90] -> [256, 32, 23]
        x = self.stage5(x)  # [256, 32, 23] - > [1,5]

        return x

if __name__ == '__main__':
    # Test image in/output
    # input image size: [1280,720,3]
    model = SKGNet(outputdim=5)
    input_img = torch.Tensor(3,1024,720)
    out = model(input_img)
    print(out)

