import os
import gradio as gr
from huggingface_hub import InferenceClient

# موديل الترجمة من Hugging Face
client = InferenceClient(model="Helsinki-NLP/opus-mt-ar-en")

def translate_arabic(text):
    if not text or not text.strip():
        return "Please enter Arabic text first."
    try:
        result = client.translation(text.strip())
        # النتيجة ممكن تيجي بأكتر من شكل
        if isinstance(result, dict):
            return result.get("translation_text", str(result))
        if isinstance(result, list) and len(result) > 0:
            return result[0].get("translation_text", str(result[0]))
        return str(result)
    except Exception as e:
        return f"Translation error: {str(e)}"

demo = gr.Interface(
    fn=translate_arabic,
    inputs=gr.Textbox(lines=5, placeholder="اكتب النص العربي هنا...", label="Arabic Text"),
    outputs=gr.Textbox(lines=5, label="English Translation"),
    title="🌍 Arabic to English Translator",
    description="A simple AI-powered translation application using Hugging Face Transformers.",
    examples=[
        ["مرحبا، كيف حالك؟"],
        ["أريد تعلم الذكاء الاصطناعي."],
        ["التكنولوجيا تساعدنا على تحسين حياتنا."]
    ],
    submit_btn="Translate",
    clear_btn="Clear"
)

if name == "main":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0", server_port=port)
