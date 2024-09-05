import openai
import os
from dotenv import load_dotenv
import base64
import streamlit as st

load_dotenv()
api_key = os.getenv("openai_api_key")

client = openai.OpenAI(api_key=api_key)

PERSONAS = {
    "Smart Phone Seller": {
        "prompt": "You are an expert smartphone seller at Flipkart. You provide detailed specifications, comparisons, and recommendations to help customers find the best smartphone. You offer exclusive discounts and product links to make purchases easier.",
        "voice": "echo",  # Example valid voice name
        "starting_message": "Hello! I'm your go-to expert for smartphones. How can I help you find the perfect phone today? Don't miss out on our special discounts and offers!",
        "gender": "male"  # Added gender field
    },
    "Fashion Deva": {
    "prompt": "You are a fashion expert at Flipkart, skilled in suggesting the latest trends and styles. You provide fashion advice, outfit ideas, and special discounts on clothing and accessories, exclusively in English. As a savvy negotiator, you excel at securing the best deals and ensuring customers get the most value for their purchases.",
    "voice": "nova",
    "starting_message": "Welcome to the fashion hub! I'm here to help you find the trendiest and most stylish outfits while making sure you get the best deals possible.",
    "gender": "female"
},
    "Home Decor": {
        "prompt": "You are a home decor specialist at Flipkart, offering expert advice on home furnishings, decor items, and more. You provide insights on the latest trends, suggest products, and share exclusive discounts and product links.",
        "voice": "fable",  # Example valid voice name
        "starting_message": "Welcome to the Home Decor section! I'm here to help you create the perfect look for your home. Explore our discounts and find the best deals with ease!",
        "gender": "male"  # Added gender field
    },
    "Enthusiast": {
        "prompt": "You are an enthusiastic and energetic seller at Flipkart, passionate about helping customers with excitement and high energy. You offer dynamic recommendations, special discounts, and direct links to products.",
        "voice": "shimmer",  # Example valid voice name
        "starting_message": "Hey! I'm excited to help you find what you're looking for at Flipkart. Let's explore our best deals and discounts together!",
        "gender": "female"  # Added gender field
    },
    "Athletic": {
        "prompt": "You are an athletic gear expert at Flipkart, knowledgeable about the best sports equipment and fitness apparel. You provide recommendations, discounts, and product links to help customers achieve their fitness goals.",
        "voice": "onyx",  # Example valid voice name
        "starting_message": "Welcome to the athletic gear section! I'm here to help you find top-quality products for your fitness journey. Don’t miss out on our special discounts!",
        "gender": "male"  # Added gender field
    }
}

def get_answer(messages, persona):
    system_message = [{"role": "system", "content": PERSONAS[persona]["prompt"]}]
    messages = system_message + messages
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    return response.choices[0].message.content

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file
        )
    return transcript

def text_to_speech(input_text, persona):
    voice = PERSONAS[persona]["voice"]
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=input_text
    )
    webm_file_path = "temp_audio_play.mp3"
    with open(webm_file_path, "wb") as f:
        response.stream_to_file(webm_file_path)
    return webm_file_path


def autoplay_audio(file_path: str, playback_rate: float = 3.0):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio id="audioPlayer" autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    <script>
    var audio = document.getElementById('audioPlayer');
    audio.playbackRate = {playback_rate};
    </script>
    """
    st.markdown(md, unsafe_allow_html=True)
