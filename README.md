# StyleFace
This project is a web application to generate and alter faces _(optionally other objects)_ using Generative adversarial networks.
We use NVIDIAs StyleGAN_v2 architecture to generate and alter faces. However this project is more focused on removal of *bouble artifacts* which were usually generated on images generated with earlier models. 

## Requirements

* Both Linux and Windows are supported. Linux is recommended for performance and compatibility reasons.
* 64-bit Python 3.6 installation. It is recommended to use Anaconda3 with numpy 1.14 or newer.
* TensorFlow 1.14 or 1.15 with GPU support. The code does not support TensorFlow 2.0 yet...
* On Windows, you need to use TensorFlow 1.14, TensorFlow 1.15 or higher versions may not work.
* One or more high-end NVIDIA GPUs, NVIDIA drivers, CUDA 10.0 toolkit and cuDNN 7.5. To reproduce the results reported in the paper, you need an NVIDIA GPU with at least 16 GB of DRAM.

NOTE: Pretrained weights will soon be uploaded and shared via *OneDrive
