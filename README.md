# StyleFace
This project is a web application to generate and alter faces _(optionally other objects)_ using Generative adversarial networks.
We use NVIDIAs StyleGAN_v2 architecture to generate and alter faces. However this project is more focused on removal of *bouble artifacts* which were usually generated on images generated with earlier models. 

#### NOTE: This project is in the final stages of development. All files will be finalized and uploaded soon.

## Requirements

* Both Linux and Windows are supported. Linux is recommended for performance and compatibility reasons.
* 64-bit Python 3.6 installation. It is recommended to use Anaconda3 with numpy 1.14 or newer.
* TensorFlow 1.14 or 1.15 with GPU support. The code does not support TensorFlow 2.0 yet...
* On Windows, you need to use TensorFlow 1.14, TensorFlow 1.15 or higher versions may not work.
* One or more high-end NVIDIA GPUs, NVIDIA drivers, CUDA 10.0 toolkit and cuDNN 7.5. To reproduce the results reported in the paper, you need an NVIDIA GPU with at least 16 GB of DRAM.

## Library dependency
You can get a virtual environment file [this](https://drive.google.com/uc?export=download&id=1lbB4mSu8gkYKKBZmTepDOz2J1c-Yz_3o) Google Drive link. You will need to ask the author for the password.<br>[mohit.gupta2jly@gmail.com](mailto:mohit.gupta2jly@gmail.com) <br> 
Extract the RAR file in the root directory and, type in your console:
```
  styleEnv\Scripts\activate
```
and press enter. Now you can run the project from this activated environment. <br>
Alternatively, you can run _install_dependencies.py_ file, it will automatically install all dependencies.

## Pretrained weights
You can download pre-trained weights [this](https://1drv.ms/u/s!AuH-tUAwy-xChrA5ZgHPbjk1nJUH_Q?e=2Wa6HZ) OneDrive link. You will need to ask the author for the password. <br>This will download a ~10.1GB file. Extract it in the 'models' directory.

## Sample results
StyleFace can transform a source image into an output image reflecting the style (e.g., hairstyle and makeup) of a given reference image.

<p align="left"><img width="99%" src="assets/img2img_translation.gif" /></p>

NOTE: Pretrained weights will soon be uploaded and shared via OneDrive
