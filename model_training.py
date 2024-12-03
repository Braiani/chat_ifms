# from transformers import GPT2Tokenizer, GPT2LMHeadModel
from ollama import Client

# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

# def generate_text(prompt):
#     inputs = tokenizer.encode(prompt, return_tensors="pt")
#     outputs = model.generate(
#         inputs, 
#         max_length=50,
#         num_return_sequences=1, 
#         pad_token_id=tokenizer.eos_token_id,
#         no_repeat_ngram_size=2,  # Evita repetições
#         temperature=0.1,  # Controla a aleatoriedade (mais baixo é mais previsível)
#         top_p=0.9,  # Foco nos tokens mais prováveis
#         do_sample=True, # Ativa o modo de amostragem
#     )
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)

def generate_text(prompt):
    try:
        ollama = Client(host='http://10.1.1.82:11434')
        response = ollama.chat(model='tinyllama', messages=[{
            'role': 'user',
            'content': prompt
        }])

        llm_response = response.get('message', {}).get('content', '')

        return llm_response
    except Exception as err:
        print(f'Erro: {err}')

if __name__ == "__main__":
    prompt = "Quanto é 2+2?"
    result = generate_text(prompt)
    print("Texto gerado pelo modelo:", result)

