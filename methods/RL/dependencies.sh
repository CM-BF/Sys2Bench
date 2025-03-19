#!/bin/bash

pip install "torch==2.5.1" "setuptools<71.0.0"  --index-url https://download.pytorch.org/whl/cu121
pip install tensorboard

conda install -y nvidia/label/cuda-12.1.1::cuda-compiler
pip install  --upgrade \
  "transformers==4.48.1" \
  "datasets==3.1.0" \
  "accelerate==1.3.0" \
  "hf-transfer==0.1.9" \
  "deepspeed==0.15.4" \
  "trl==0.14.0"

pip install "vllm==0.7.0"
pip install hydra-core --upgrade