conda create -n sys2bench python=3.10 -y
conda activate sys2bench
python -m pip install vllm==0.9.2
python -m pip install flash-attn==2.8.1 trl==0.19.1 hydra-core tarski pddl==0.2.0 peft wandb transformers==4.53.1 deepspeed==0.15.4