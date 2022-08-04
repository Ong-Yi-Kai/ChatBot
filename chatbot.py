"""
Uses OpenAI dialoGPT which is a GPT2 model with a LM head
to predict a response from user's speech

Choice of a Large, Medium or Small model.
Model's weights stored in dir 'model'
"""

from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import torch

class chatBot():
    """
    chatbot object that utilises dialoGPT from hugging face transformers

    attributes:
        tokenizer [GPT2TokenizerFast]: tokenizer object, cvt str -> vector
        model [GPT2LMHeadModel]: gpt2 causal language model
    """
    def __init__(self,model_dir):
        """
        Creates attrib tokenizer and model

        param model_dir [str]: path to model weights and cfg dir
        """
        assert type(model_dir) == str
        assert os.path.isdir(model_dir)

        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForCausalLM.from_pretrained(model_dir)

    def generate_response(self,user_ip:str)->str:
        """
        returns the model's generated response

        param user_ip: [str] user's speech/response
        """
        assert type(user_ip) == str

        # tokenize user input
        user_ip_tokenized = self.tokenizer.encode(user_ip + self.tokenizer.eos_token,
                                                  return_tensors='pt')

        if not hasattr(self, 'chat_history_ids'):
            bot_input_ids = user_ip_tokenized
        else:
            bot_input_ids = torch.cat([self.chat_history_ids, user_ip_tokenized], dim=-1)


        self.chat_history_ids = self.model.generate(bot_input_ids, max_new_tokens = 1000,
                                                    pad_token_id=self.tokenizer.eos_token_id)

        # decode to readable
        return self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0],
                                     skip_special_tokens=True)



