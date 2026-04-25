import streamlit as st
import google.generativeai as genai
import asyncio
import edge_tts
import os

# Dashboard Setup
st.set_page_config(page_title="Final AI Factory", layout="centered")
st.title("🎬 2026 AI Video Factory")

# API Configuration (Nayi wali Key)
API_KEY = "AIzaSyA0Zfyf0shedxkKloB4peT-hljjpqVVgFI"

try:
    genai.configure(api_key=API_KEY)
    # Sabse latest stable model
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Setup Error: {e}")

topic = st.text_input("Enter Topic:", "Future in 2050")

if st.button("🚀 Generate AI Magic"):
    if topic:
        with st.spinner("AI Script likh raha hai..."):
            try:
                # Is baar hum simple content generation use kar rahe hain
                response = model.generate_content(f"Write 2 lines in Hindi about {topic}")
                
                if response.text:
                    st.subheader("📜 Script:")
                    st.write(response.text)
                    
                    # Voice Generation
                    async def make_voice():
                        await edge_tts.Communicate(response.text, "hi-IN-MadhuramNeural").save("v.mp3")
                    asyncio.run(make_voice())
                    
                    st.audio("v.mp3")
                    st.success("✅ Script aur Voice taiyar!")
                else:
                    st.error("AI ne jawab nahi diya. Key check karein.")
                    
            except Exception as e:
                st.error(f"Dhyan dein: {e}")
                st.info("Ye error server side hai, 1 minute baad dobara try karein.")
