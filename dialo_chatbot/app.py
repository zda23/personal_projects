
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

chat_history_ids = None

def chat_with_bot(user_input, history=[]):
    global chat_history_ids

    # Convert user input to tokens with end-of-sentence token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append to previous chat history or start fresh
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate model response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode only the new part of the response
    response = tokenizer.decode(
        chat_history_ids[:, bot_input_ids.shape[-1]:][0],
        skip_special_tokens=True
    )

    # Store the message pair
    history.append((user_input, response))
    return history, history

# Gradio ChatInterface UI
gr.ChatInterface(
    fn=chat_with_bot,
    title="💬 Chat with DialoGPT",
    description="An open-domain conversational AI chatbot powered by Microsoft's DialoGPT-medium. Ask anything!"
).launch()
