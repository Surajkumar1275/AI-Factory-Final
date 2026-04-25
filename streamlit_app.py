import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts
import os

# Mobile Friendly Setup
st.set_page_config(page_title="AI Factory", layout="centered")
st.title("🎬 My AI Video Factory")

# Nayi API Key jo aapne abhi nikali hai
API_KEY = "AIzaSyA0Zfyf0shedxkKloB4peT-hljjpqVVgFI"
genai.configure(api_key=API_KEY)

topic = st.text_input("Enter Video Topic:", "Future 2050")

if st.button("🚀 Start Generating"):
    if topic:
        with st.spinner("AI is thinking..."):
            try:
                # Latest and simplest model call
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Write a 20s viral Hindi script for {topic}")
                
                st.subheader("📜 Script:")
                st.write(response.text)
                
                async def make_voice():
                    await edge_tts.Communicate(response.text, "hi-IN-MadhuramNeural").save("v.mp3")
                asyncio.run(make_voice())
                
                st.success("✅ Voice Ready!")
                st.audio("v.mp3")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a topic.")
