import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"]='1'
from huggingface_hub import snapshot_download
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline

class InferlessPythonModel:
    def initialize(self):
        model_id = "tenyx/TenyxChat-8x7B-v1"
        snapshot_download(repo_id=model_id,allow_patterns=["*.safetensors"])
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=getattr(torch, "float16"),
            bnb_4bit_use_double_quant=True,
            )
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, quantization_config=bnb_config)
        self.pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
        
    def infer(self, inputs):
        prompt = inputs["prompt"]
        messages = [{"role": "system", "content":prompt}]
        prompt = self.pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        out = self.pipe(prompt, max_new_tokens=256, do_sample=True, top_p=0.9,temperature=0.9)
        generated_text = out[0]["generated_text"][len(prompt):]
        return {'generated_result': generated_text}

    def finalize(self):
        pass
