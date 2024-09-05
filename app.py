import streamlit as st
import os
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text, PERSONAS
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
import wave

# Set layout to wide
st.set_page_config(layout="wide")

# Float feature initialization
float_init()

def initialize_session_state():
    if "messages" not in st.session_state:
        persona = st.session_state.get("persona", "Home Decor")  # Default to "Home Decor" if not set
        st.session_state.messages = [
            {"role": "assistant", "content": PERSONAS[persona]["starting_message"]}
        ]
    if "persona" not in st.session_state:
        st.session_state.persona = "Home Decor"  # Default persona

initialize_session_state()

# Center the title
st.markdown("<h1 style='text-align: center;'>FlipKart AI Seller Model 🧑🏻‍💼</h1>", unsafe_allow_html=True)

# Add persona selection
persona = st.selectbox("Choose a Persona:", list(PERSONAS.keys()))
if persona != st.session_state.persona:
    st.session_state.persona = persona
    st.session_state.messages = [
        {"role": "assistant", "content": PERSONAS[persona]["starting_message"]}
    ]

# Create footer container for the microphone
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder(icon_name="microphone")

# Define CSS styles for dark theme with yellow accents and animations
st.markdown("""
    <style>
    body {
        background-color: #0a0a0a; /* Even darker background color */
        color: #f0f0f0; /* Light text color */
    }
    .user-message {
        background-color: #1c1c1c; /* Darker background for user messages */
        color: #f0f0f0; /* Light text color */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 2px solid #f7e50e; /* Yellow border */
        animation: fadeIn 0.5s ease-in-out;
    }
    .assistant-message {
        background-color: #2a2a2a; /* Slightly lighter background for assistant messages */
        color: #f0f0f0; /* Light text color */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 2px solid #f7e50e; /* Yellow border */
        animation: fadeIn 0.5s ease-in-out;
    }
    .chat-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        animation: slideIn 0.5s ease-in-out;
    }
    .chat-container.assistant {
        justify-content: flex-end;
    }
    .chat-container .emoji {
        font-size: 1.5rem;
        margin-right: 10px;
    }
    .stButton button {
        display: none;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateX(-10px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Display messages with consistent styling
for message in st.session_state.messages:
    emoji = ""
    if message["role"] == "assistant":
        if PERSONAS[st.session_state.persona]["gender"] == "male":
            emoji = "👨🏼"
        elif PERSONAS[st.session_state.persona]["gender"] == "female":
            emoji = "👩🏻"
        st.markdown(f"""
            <div class="chat-container assistant">
                <div class="emoji">{emoji}</div>
                <div class="assistant-message">{message['content']}</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-container">
                <div class="emoji">👤</div>
                <div class="user-message">{message['content']}</div>
            </div>
        """, unsafe_allow_html=True)

def is_audio_valid(file_path):
    try:
        with wave.open(file_path, 'r') as wf:
            duration = wf.getnframes() / float(wf.getframerate())
            return duration >= 0.1
    except wave.Error:
        return False

if audio_bytes:
    # Write the audio bytes to a file
    with st.spinner("Transcribing..."):
        webm_file_path = "temp_audio.mp3"
        with open(webm_file_path, "wb") as f:
            f.write(audio_bytes)

        if is_audio_valid(webm_file_path):
            transcript = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.messages.append({"role": "user", "content": transcript})
                st.markdown(f"""
                    <div class="chat-container">
                        <div class="emoji">👤</div>
                        <div class="user-message">{transcript}</div>
                    </div>
                """, unsafe_allow_html=True)
                os.remove(webm_file_path)
        else:
            st.warning("Recorded audio is too short. Please try again.")

if st.session_state.messages[-1]["role"] != "assistant":
    with st.spinner("Thinking🤔..."):
        final_response = get_answer(st.session_state.messages, st.session_state.persona)
    with st.spinner("Generating audio response..."):
        audio_file = text_to_speech(final_response, st.session_state.persona)
        autoplay_audio(audio_file)
    st.markdown(f"""
        <div class="chat-container assistant">
            <div class="emoji">{emoji}</div>
            <div class="assistant-message">{final_response}</div>
        </div>
    """, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": final_response})
    os.remove(audio_file)

# Float the footer container and provide CSS to target it with
footer_container.float("bottom: 0rem;")

h_s_s = """
<style>
.st-emotion-cache-1wbqy5l {visibility:hidden}
</style>
"""
st.markdown(h_s_s, unsafe_allow_html=True)