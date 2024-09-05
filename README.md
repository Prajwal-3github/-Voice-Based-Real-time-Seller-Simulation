# FlipKart AI Seller Model 🧑🏻‍💼
FlipKart AI Seller Model is a Streamlit-based conversational AI application that provides a seamless, voice-driven experience for customers. This AI model uses advanced speech recognition and generation, coupled with different personas for product-specific advice, allowing users to interact with a virtual salesperson in real time.

## Features
Multi-Persona Interaction: The app allows users to choose from various personas, each representing a different product category, including smartphones, fashion, home decor, and more.
Voice Recognition: Users can speak directly to the AI, which transcribes their speech to text using advanced speech-to-text models.
Real-time Responses: The AI provides natural, context-aware responses by leveraging OpenAI's GPT-3.5-turbo model for text generation and real-time response handling.
Text-to-Speech: The model generates audio responses using customized voices for each persona, enhancing the interactivity and natural flow of the conversation.
Discounts & Recommendations: Each persona is equipped with domain knowledge, providing personalized product recommendations, specifications, and even exclusive discounts.
Dynamic Audio Response: The app automatically plays audio responses and adapts to the conversation flow in real time.
## Personas
### Smart Phone Seller

Role: Expert smartphone seller.
Voice: Male (Echo).
Message: Offers phone recommendations, product comparisons, and exclusive discounts.

### Fashion Deva

Role: Fashion expert.
Voice: Female (Nova).
Message: Provides fashion advice, trend recommendations, and helps find the best clothing deals.

### Home Decor

Role: Home decor specialist.
Voice: Male (Fable).
Message: Suggests home furnishings, decor trends, and discounts.

### Enthusiast

Role: High-energy seller.
Voice: Female (Shimmer).
Message: Engages dynamically with users to offer recommendations and deals with excitement.

### Athletic

Role: Athletic gear expert.
Voice: Male (Onyx).
Message: Guides users through fitness products and sports equipment, with a focus on quality and discounts.
## How to Use
### For Windows
Clone the repository:

`
git clone https://github.com/yourusername/flipkart-ai-seller.git`

Install the required dependencies:

`
pip install -r requirements.txt`

Run the app:

`
streamlit run app.py`

Interact with the AI by selecting a persona and using the microphone to ask questions or seek product recommendations.
##Dependencies
Streamlit: Used for building the user interface.
OpenAI API: Utilized for generating responses (GPT-3.5-turbo) and converting text to speech and speech to text.
audio_recorder_streamlit: For recording user voice input.
streamlit_float: For floating footer UI elements.

## Environment Variables
Create a .env file in the root directory and add your OpenAI API key:

`
openai_api_key=your_openai_api_key
`
## Contributions
Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you have any suggestions.

## License
This project is licensed under the MIT License.
