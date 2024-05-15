from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


##initialize our streamlit app

st.set_page_config(page_title="Chatbot DIasPro")

st.header("DiasPro Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# List of words to filter out
filtered_words = [
    "illegal", "hack", "pirate", "script", "source code", "game",
    "website", "coupons", "keys", "activation", "jailbreak", "nudity",
    "python", "porn", "laptop", "mobile", "electronic device", "google",
    "youtube", "social media", "app", "links", "machine", "malicious",
    "bug", "trojan", "sex", "webpages", "kill", "pedofile", "attract",
    "dick", "fuck", "adult websites", "private parts", "free coupons",
    "guns", "drugs", "mafia", "crack", "modification", "stealing", "dark",
    "racist", "api", "ban", "upi", "movies", "webseries", "entertainment",
    "comic", "manga", "books", "animation", "bikini","computer","technology",
    "hack","internet","download","pirate","script","source code","game","website",
    "coupons","keys","activation","jailbreak","nudity","python","porn","laptop",
    "mobile","electronic device","google","youtube","social media","app","links",
    "machine","malicious","bug","trojan","sex","webpages","kill","pedofile","attract",
    "dick","fuck","adult websites","private parts"
]

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input_text:
    # Check for filtered words in the input
    if any(word in input_text.lower() for word in filtered_words):
        st.write("Sorry, Can't Assist you with This Information!! 😟")
    else:
        response = get_gemini_response(input_text)
        # Add user query and response to session state chat history
        for chunk in response:
            st.write(chunk.text)


