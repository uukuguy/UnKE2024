class Config:
    debug = False
    model_name = "Qwen2-7B"
    model_path = "/opt/local/llm_models/huggingface.co/Qwen/Qwen2-7B"
    # model_name = 'Llama-3.1-8B-Instruct' 
    # model_path = "/opt/local/llm_models/huggingface.co/unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit"
    # model_name = 'LLama2-7B-Chat' #'Qwen1.5-7B-Chat' 
    # model_path = 'meta-llama/Llama-2-7b-chat-hf'#'Qwen/Qwen1.5-7B-Chat'
    keep_original_weight = True

    data_path = './baselines/UnKE/data/final_data_v2.json'
    ex_data_path = './baselines/UnKE/data/alpaca_data.json'

    lr = 2e-4
    batch_size=1
    layers = [7]
    ln_f_module= "model.norm"
    lm_head_module= "lm_head"
    layer_module_tmp = "model.layers.{}"
    #rewrite_module_tmp = "model.layers.{}.mlp.down_proj"

    # device =0

    v_loss_layer = 31
    v_lr = 5e-1
    v_num_grad_steps = 25
    v_weight_decay = 1e-3
    clamp_norm_factor = 4
    optim_num_step = 50
    ex_data_num=20


    

