import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.models as trained_models
from collections import OrderedDict
import numpy as np
from constants import *
from torch.autograd import Variable
import pdb


def weight_tensor_from_np(weight,gradflag = True):
  return torch.nn.Parameter(torch.from_numpy(weight).cuda(),requires_grad=gradflag)

def bias_tensor_from_np(bias,gradflag = True):
  return torch.nn.Parameter(torch.from_numpy(bias).cuda().view(1,bias.shape[0],1,1),requires_grad=gradflag)

  
class CNNFeatureExtractor(nn.Module):
  def __init__(self):
    super(CNNFeatureExtractor, self).__init__()    

                            # Conv 0
    self.W0_1 = weight_tensor_from_np(disc_weights[disc_weight_list_order.pop()])
    self.b0_1 = bias_tensor_from_np(disc_weights[disc_weight_list_order.pop()])

                            # Conv 1_1
    self.W1_1 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b1_1 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 1_2
    self.W1_2 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b1_2 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])

                            # Conv 2_1
    self.W2_1 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b2_1 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 2_2
    self.W2_2 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b2_2 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])

                            # Conv 3_1
    self.W3_1 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b3_1 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 3_2
    self.W3_2 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b3_2 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 3_3
    self.W3_3 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b3_3 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])

                            # Conv 4_1
    self.W4_1 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b4_1 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 4_2
    self.W4_2 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b4_2 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 4_3
    self.W4_3 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b4_3 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])

                            # Conv 5_1
    self.W5_1 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b5_1 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 5_2
    self.W5_2 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b5_2 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
                            # Conv 5_3
    self.W5_3 = weight_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    self.b5_3 = bias_tensor_from_np(gen_weights[gen_weight_list_order.pop()])
    
    # ---------------------------------------------------------------------------------------------------------
    #                               ENCODER ARCHITECTURE
    # ---------------------------------------------------------------------------------------------------------

  def forward(self, x):   

                        # Conv 0_1
    x = F.conv2d(x,self.W0_1, stride = 1, padding = 0)
    x = x.add(self.b0_1)
    x = F.relu(x)
                         # Conv 1_1
    x = F.conv2d(x, self.W1_1, stride = 1, padding = 1)
    x = x.add(self.b1_1)
    x = F.relu(x)    
                         # Conv 1_2
    x = F.conv2d(x, self.W1_2, stride = 1, padding = 1)
    x = x.add(self.b1_2)
    x = F.relu(x)
                         # Pool 1
    x = F.max_pool2d(x,2)

                        # Conv 2_1
    x = F.conv2d(x, self.W2_1, stride = 1, padding = 1)
    x = x.add(self.b2_1)
    x = F.relu(x)
                        # Conv 2_2
    x = F.conv2d(x,self.W2_2,stride = 1, padding = 1)
    x = x.add(self.b2_2)
    x = F.relu(x)
                        # Pool 2
    x = F.max_pool2d(x,2)

                          # Conv 3_1
    x = F.conv2d(x, self.W3_1, stride = 1, padding = 1)
    x = x.add(self.b3_1)
    x = F.relu(x)
                        # Conv 3_2
    x = F.conv2d(x, self.W3_2, stride = 1, padding = 1)
    x = x.add(self.b3_2)
    x = F.relu(x)
                        # Conv 3_3
    x = F.conv2d(x, self.W3_3, stride = 1, padding = 1)
    x = x.add(self.b3_3)
    x = F.relu(x)
                        # Pool 3
    x = F.max_pool2d(x,2)

                        # Conv 4_1
    x = F.conv2d(x,self.W4_1, stride = 1, padding = 1)
    x = x.add(self.b4_1)
    x = F.relu(x)
                        # Conv 4_2
    x = F.conv2d(x, self.W4_2, stride = 1, padding = 1)
    x = x.add(self.b4_2)
    x = F.relu(x)
                        # Conv 4_3
    x = F.conv2d(x, self.W4_3, stride = 1, padding = 1)
    x = x.add(self.b4_3)
    x = F.relu(x)
                        # Pool 4
    x = F.max_pool2d(x,2)

                        # Conv 5_1
    x = F.conv2d(x, self.W5_1, stride = 1, padding = 1)
    x = x.add(self.b5_1)
    x = F.relu(x)
                        # Conv 5_2
    x = F.conv2d(x, self.W5_2, stride = 1, padding = 1)
    x = x.add(self.b5_2)
    x = F.relu(x)
                        # Conv 5_3
    x = F.conv2d(x, self.W5_3, stride = 1, padding = 1)
    x = x.add(self.b5_3)
    x = F.relu(x)

    return x
        
gen_weights = np.load(genWeightsPath)
gen_weight_list_split = [int(i.split('_')[1]) for i in gen_weights.keys()]
gen_weight_list_split.sort(reverse=True)
gen_weight_list_order = ["arr_" + str(i) for i in gen_weight_list_split]

disc_weights = np.load(discWeightsPath)
disc_weight_list_split = [int(i.split('_')[1]) for i in disc_weights.keys()]
disc_weight_list_split.sort(reverse=True)
disc_weight_list_order = ["arr_" + str(i) for i in disc_weight_list_split]


class LSTM(nn.Module):
    def __init__(self):
        super(LSTM, self).__init__()
        self.lstm = nn.LSTM(input_size=512, 
                            hidden_size=512,
                            num_layers=1,
                            batch_first=False,
                            bidirectional=False)
        self.fc = nn.Linear(512*1,128)
        self.fc1 = nn.Linear(128*1,16)
        self.fc2 = nn.Linear(128*1,37)
        self.hidden = self.init_hidden()
        
    def init_hidden(self):
        return (Variable(torch.zeros(1, 1, 512)).cuda(), # shape is (num_layers,sequence_length,hidden_dim)
                Variable(torch.zeros(1, 1, 512)).cuda())
    
    def forward(self, x):
        hidden = self.init_hidden()        
        output, hidden = self.lstm(x, hidden)

        intermediate = self.fc(output.view(output.size()[0],-1))
        action_output = self.fc1(intermediate)
        object_output = self.fc2(intermediate)

        return torch.clamp(action_output,0,49688), torch.clamp(object_output,0,49688)