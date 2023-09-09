# Image Face-Centric Cropper

An app that auto-crops images around detected faces and resizes them to a consistent 1024x1024 resolution.

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


