import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as trained_models
from collections import OrderedDict
from constants import *
import numpy as np
import pdb
from torch.autograd import Variable

def weight_tensor_from_np(weight):
  return Variable(torch.from_numpy(weight).cuda())

def bias_tensor_from_np(bias):
  return Variable(torch.from_numpy(bias).cuda().view(1,bias.shape[0],1,1))


class Generator(nn.Module):
  def __init__(self):
    super(Generator, self).__init__()

    # self.relu = F.relu()
    # self.maxpool = nn.MaxPool2d(2,2,return_indices=True)
    # self.maxunpool = nn.MaxUnpool2d(1)

    # ---------------------------------------------------------------------------------------------------------
    #                               ENCODER ARCHITECTURE
    # ---------------------------------------------------------------------------------------------------------
  
  def forward(self, x):
                         # Conv 1_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add(bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                         # Conv 1_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add(bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                         # Pool 1
    x = F.max_pool2d(x,2)

                        # Conv 2_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 2_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]),stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Pool 2
    x = F.max_pool2d(x,2)

                        # Conv 3_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 3_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 3_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Pool 3
    x = F.max_pool2d(x,2)

                        # Conv 4_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 4_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 4_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Pool 4
    x = F.max_pool2d(x,2)

                        # Conv 5_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 5_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # Conv 5_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
              
    # pdb.set_trace()
    # -------------------------------------------------------------------------------------------------------------
    #                                        DECODER ARCHITECTURE
    # -------------------------------------------------------------------------------------------------------------

                         # uConv 5_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                         # uConv 5_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 5_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                         # Upool 4
    x = F.upsample(x, scale_factor=2)

                        # uConv 4_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 4_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 4_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uPool 3
    x = F.upsample(x, scale_factor=2)

                        # uConv 3_3
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 3_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 3_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uPool 2
    x = F.upsample(x, scale_factor=2)

                        # uConv 2_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 2_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uPool 1
    x = F.upsample(x, scale_factor=2)

                        # uConv 1_2
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)
                        # uConv 1_1
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.relu(x)

                        # Output to 1 Channel
    x = F.conv2d(x, weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()]), stride = 1, padding = 0)
    x = x.add( bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()]))
    x = F.sigmoid(x)
    
    return x


class Discriminator(nn.Module):
  def __init__(self):
    super(Discriminator, self).__init__()
    
    
  def forward(self, x):
    pdb.set_trace()

    # Conv 1_1
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 0)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)    
    # Conv 1_2
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)
    # Pool1
    x = F.max_pool2d(x,4)

    # Conv 2_1
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)
    # Conv 2_2
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)
    # Pool2
    x = F.max_pool2d(x,2)

    # Conv 3_1
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)
    # Weight norm 3_1
    # ('weight_norm3_1', nn.utils.weight_norm()), # Look into this later
    # Conv 3_2
    x = F.conv2d(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]), stride = 1, padding = 1)
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.relu(x)
    # Weight norm 3_2
    # ('weight_norm3_2', nn.utils.weight_norm()), # Look into this later
    # Pool 3
    x = F.max_pool2d(x,2)

    # Fc 4
    x = F.linear(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.tanh(x)
    # Fc 5
    x = F.linear(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.tanh(x)
    # Fc 6
    x = F.linear(x, weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = x.add( bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()]))
    x = F.sigmoid(x)
    return x

    # self.fc_layers = nn.Sequential(OrderedDict([
    #                                         ('fc4', nn.Linear(12288, 60)),
    #                                         ('tanh4', nn.Tanh()),
    #                                         ('fc5', nn.Linear(100,2)),
    #                                         ('tanh5', nn.Tanh()),
    #                                         ('fc6', nn.Linear(2,1)),
    #                                         ('sigmoid', nn.Sigmoid())

    #                                             ]))

    # self.maxpool = F.max_pool2d(x,2)

    # self.weight_norm1 = nn.utils.weight_norm(self.conv_layers1)
    # self.weight_norm2 = nn.utils.weight_norm(self.conv_layers2)
    # TODO : Look into adding weight norm layer in discriminator network

  """
  def forward(self,x):
    x = self.conv_layers1(x)
    # x = nn.utils.weight_norm(x)
    x = self.conv_layers2(x)
    # x = nn.utils.weight_norm(x)
    # x = self.weight_norm1(x)
    # x = self.weight_norm2(x)
    # x = self.maxpool(x)
    x = x.view(x.size(0),-1)
    x = self.fc_layers(x)
    pdb.set_trace()

    return x
  """

#pre-define weights and biases
gen_weights = np.load(genWeightsPath)
gen_weight_list_split = [int(i.split('_')[1]) for i in gen_weights.keys()]
gen_weight_list_split.sort(reverse=True)
gen_weight_list_order = ["arr_" + str(i) for i in gen_weight_list_split]


disc_weights = np.load(discWeightsPath)
disc_weight_list_split = [int(i.split('_')[1]) for i in disc_weights.keys()]
disc_weight_list_split.sort(reverse=True)
disc_weight_list_order = ["arr_" + str(i) for i in disc_weight_list_split]

pdb.set_trace()