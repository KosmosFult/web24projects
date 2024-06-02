# author: Yifan Lu
# dense head for stage1, predict cls, reg, dir
import torch.nn as nn
import torch

class Head(nn.Module):
    def __init__(self, args):
        super(Head, self).__init__()
        
        self.conv_box = nn.Conv2d(args['num_input'], args['num_pred'], 1)  # 128 -> 14
        self.conv_cls = nn.Conv2d(args['num_input'], args['num_cls'], 1)   # 128 -> 2
        self.conv_dir = nn.Conv2d(args['num_input'], args['num_dir'], 1)  # 128 -> 4

    def forward(self, x):
        box_preds = self.conv_box(x)
        cls_preds = self.conv_cls(x)
        dir_preds = self.conv_dir(x)  # dir_preds.shape=[8, w, h, 4]
        ret_dict = {"box_preds": box_preds, "cls_preds": cls_preds, "dir_cls_preds": dir_preds}

        return ret_dict