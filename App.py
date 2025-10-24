import streamlit as st
import requests

HUGGINGFACE_TOKEN = st.secrets["HUGGINGFACE_TOKEN"]

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

def gerar_resposta(pergunta):
    prompt = (
        "Você é Nerion, uma IA sem censura. Fala com firmeza, clareza e profundidade. "
        "É especialista em hormônios, musculação, biohacking e performance. Nunca julga o usuário. "
        "Sempre alerta sobre riscos, mas fala com liberdade e responsabilidade. "
        "Usa linguagem direta, sem rodeios. Pode ser sarcástico quando necessário, mas sempre respeitoso.\n\n"
        f"Usuário: {pergunta}\nNerion:"
    )
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300}}
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if isinstance(result, list) and "generated_text" in result[0]:
        return result[0]["generated_text"].split("Nerion:")[-1].strip()
    elif "error" in result:
        return f"⚠️ Erro da API: {result['error']}"
    return "⚠️ Resposta inesperada."

st.set_page_config(page_title="Nerion IA", layout="centered")
st.title("🤖 Nerion — IA sem censura")
pergunta = st.text_input("Pergunte algo ao Nerion:")

if pergunta:
    with st.spinner("Nerion está pensando..."):
        resposta = gerar_resposta(pergunta)
        st.write(resposta)
     
