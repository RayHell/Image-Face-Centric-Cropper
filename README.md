# Image Face-Centric Cropper

This application processes images by identifying faces and ensuring they remain central in the final output. It first crops the image to maximize the surrounding region while keeping the face at the center. The cropped image is then resized to a standard 
1024×1024 resolution, ensuring the face remains undistorted and prominent. Ideal for creating consistent profile pictures or avatars from a collection of photographs.

## Prerequisites

- **Python 3.8** or higher
- **Conda** (Recommended for easy installation)

## Installation

### Windows:

#### 1. Install Conda:

- Download the [Miniconda installer](https://docs.conda.io/en/latest/miniconda.html) for Windows.
- Run the installer and follow the on-screen instructions.

#### 2. Set Up Environment:

```
conda create --name face_crop_env python=3.8
conda activate face_crop_env
conda install -c conda-forge dlib
pip install face_recognition Pillow
```

### Linux:

#### 1. Install Conda:

- Download the [Miniconda installer](https://docs.conda.io/en/latest/miniconda.html) for Linux.
- In the terminal, navigate to the directory where you downloaded the installer.
- Make the installer executable: `chmod +x Miniconda3-latest-Linux-x86_64.sh`
- Run the installer: `./Miniconda3-latest-Linux-x86_64.sh`
- Follow the on-screen instructions.

#### 2. Set Up Environment:

```
conda create --name face_crop_env python=3.8
conda activate face_crop_env
conda install -c conda-forge dlib
pip install face_recognition Pillow
```

## Usage

Place all the `.jpg` images you want to process inside the `images` folder. Then run the script:

```
conda activate face_crop_env
python image_processor.py
```
Windows user can also execute run.bat

Processed images will be saved in the `cropped` folder.


