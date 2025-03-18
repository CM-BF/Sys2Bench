
CUDA_VISIBLE_DEVICES=0,4,2,5,7 accelerate launch --num_processes 1 --config_file methods/RL/deep_speed.yaml  methods/RL/train.py 