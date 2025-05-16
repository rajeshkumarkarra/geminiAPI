import gradio as gr
import requests
import os

# Securely get the API key from Hugging Face secrets
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def query_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return f"Error: {e}\nFull Response: {response.text}"

iface = gr.Interface(
    fn=query_gemini,
    inputs=gr.Textbox(lines=4, placeholder="Ask something..."),
    outputs="text",
    title="Gemini 2.0 Flash with Gradio",
    description="Powered by Google's Gemini 2.0 Flash API"
)

if __name__ == "__main__":
    iface.launch()