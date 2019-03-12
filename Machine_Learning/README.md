# MSI Tensorflow tutorial
* Caffe is one of the core technology frameworks for modern AI


## ROugh overview of deep learning model
* Untrained model with input and output layers with hidden layers inbetween
* neuron weights are randomized when first introducing training set
    * Will modify neuron weights depending on what predictions are correct or incorrect
    * First layer of networks is learning very basic items such as edges or colors
* After training networks, you perform inference/production (less computationally intensive)
* Nividia has deep learning institue to help give workships www.nvidia.com/dli
* Nvidia does not write the frameworks, but inserts optimization aka working on thier hardware
* NVIDIA digits is a web based interface interactively train and manage deep learning models without having to code
* Caffe is a deep learning framwork
* TensorRT is and NVDIVIA SDK that will help optimize inference stage
* NVIDIA qwiklab  nvidia/qwiklab.com/catalog for tutorials
    * The tutorial today will always be free
* Digts has a nice hand written tutorial

# Using tensorflow on MSI
* All of the slides are attached as a PDF for the MSI tuturial

## How to submit a batch job using tensorflow
```bash
ssh mesabi
 wget z.umn.edu/tensorflow1
 tar xvfz tensorflow1
 cd tutorial_3_2_2018_mnist
 qsub run_tensorflow_examples.pbs
```

 ### Some of the key features
 * requesting the tire k40 node 
 * modules for caffee GPU vs CPU version and tensorflow gpu

```bash
ssh mesabi
 wget z.umn.edu/tensorflow2
 tar xvfz tensorflow2
 cd tutorial_3_2_2018_text
 qsub run_tensorflow_example.pbs
```

* Tensorboard is a good way to visualize your neural networks and the training process
    * Works well if you are running this locally on one machine
    * Runs as a web application
```bahs
# mount the DIR
tensorboard --logdir /Volumes/msi
```
