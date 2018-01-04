# Saliency Guided Activity Recognition
Activity recognition is a very important and challenging problem that tries to track and understand the behavior of agents through videos taken by various cameras. There exist a number of methods such as optical flow, Kalman filtering, Hidden Markov models, etc., under different modalities such as single camera, stereo, and infrared. Vision-based activity recognition has found many applications such as human-computer interaction, user interface design, robot learning, and surveillance. 

Through this paper, we propose an alternate approach to the problem of activity recognition, namely through information from saliency maps from first person viewpoint. Saliency maps help identify regions or objects in an image which attract the most attention and could essentially represent most of the features relevant for activity recognition. Based on this hypothesis, we present a systematic approach to obtaining saliency maps and predicting activity based on both saliency maps and RGB images.

## Visual Saliency Prediction with Generative Adversarial Networks

We use SalGAN, a deep convolutional neural network for visual saliency prediction trained with adversarial examples.
The first stage of the network consists of a generator model whose weights are learned by back-propagation computed from a binary cross entropy (BCE) loss over downsampled versions of the saliency maps. The resulting prediction is processed by a discriminator network trained to solve a binary classification task between the saliency maps generated by the generative stage and the ground truth ones. 
This code contains the [PyTorch](https://github.com/pytorch/pytorch) implementation of the network with minor changes from the original architecture. The original SalGAN is implemented in [Lasagne](https://github.com/Lasagne/Lasagne), which at its time is developed over [Theano](http://deeplearning.net/software/theano/).

SalGAN Architecture
![architecture-fig]

* [[SalGAN Generator Model (127 MB)]](https://imatge.upc.edu/web/sites/default/files/resources/1720/saliency/2017-salgan/gen_modelWeights0090.npz)
* [[SalGAN Discriminator (3.4 MB)]](https://imatge.upc.edu/web/sites/default/files/resources/1720/saliency/2017-salgan/discrim_modelWeights0090.npz)


## LSTM for Activity Recognition
The activity recognition model consists of a feature extractor and a classifier. A CNN feature extractor is used for extracting spatial information from either the RGBS image (RGB + Saliency) or saliency overlapped RGB image. An LSTM is then used for temporal information gathering for activity classification using a linear classifier on the output feature maps.

## References

*Junting Pan, Cristian Canton, Kevin McGuinness, Noel E. O'Connor, Jordi Torres, Elisa Sayrol and Xavier Giro-i-Nieto. "SalGAN: Visual Saliency Prediction with Generative Adversarial Networks." arXiv. 2017.*

## Acknowledgements

We would like to especially thank Dr. Jianbo Shi and Gedas Bertasius for their technical support and guidance.
