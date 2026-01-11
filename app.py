import streamlit as st
from gtts import gTTS
import os
st.set_page_config(page_title="Ayurvedic Prakriti & Agni Chatbot")
st.title("🌿 Ayurvedic Prakriti & Agni Chatbot")

st.write("Answer the questions honestly to know your Prakriti and Agni type.")

prakriti_score = {"Vata":0, "Pitta":0, "Kapha":0}
agni_score = {"Samagni":0, "Vishamagni":0, "Mandagni":0}

st.header("🧘 Prakriti Assessment")

prakriti_questions = {
    "Body type": ["Lean", "Medium", "Heavy"],
    "Skin type": ["Dry", "Oily", "Normal"],
    "Appetite": ["Irregular", "Strong", "Slow"],
    "Sleep pattern": ["Light", "Moderate", "Heavy"],
    "Nature": ["Anxious", "Aggressive", "Calm"],
    "Energy level": ["Low", "High", "Stable"],
    "Weight gain": ["Difficult", "Moderate", "Easy"],
    "Digestion": ["Variable", "Fast", "Slow"],
    "Body temperature": ["Cold", "Warm", "Normal"],
    "Hair type": ["Dry", "Fine", "Thick"]
}

for q, options in prakriti_questions.items():
    ans = st.radio(q, options)
    if ans == options[0]:
        prakriti_score["Vata"] += 1
    elif ans == options[1]:
        prakriti_score["Pitta"] += 1
    else:
        prakriti_score["Kapha"] += 1

st.header("🔥 Agni Assessment")

agni_questions = [
    "Regular hunger",
    "Strong digestion",
    "No heaviness after meals",
    "No acidity",
    "Regular bowel movement",
    "No bloating",
    "Good appetite",
    "Quick digestion",
    "Energetic after meals",
    "No sleepiness after eating"
]

for q in agni_questions:
    ans = st.radio(q, ["Yes", "Sometimes", "No"])
    if ans == "Yes":
        agni_score["Samagni"] += 1
    elif ans == "Sometimes":
        agni_score["Vishamagni"] += 1
    else:
        agni_score["Mandagni"] += 1
        st.markdown("---")  
if st.button("Get Result"):
    prakriti = max(prakriti_score, key=prakriti_score.get)
    agni = max(agni_score, key=agni_score.get)

    st.success(f"🌿 Your Prakriti: {prakriti}")
    st.success(f"🔥 Your Agni Type: {agni}")
    st.info("This is a preliminary assessment. Consult an Ayurvedic doctor for treatment.")
    
    st.subheader("🌿 Aahar, Vihar & Daily Routine")
if prakriti == "Vata":
    st.markdown("### 🥗 Aahar")
    st.write("Warm, oily, nourishing food. Milk, ghee, cooked vegetables.")

    st.markdown("### 🧘 Vihar")
    st.write("Avoid stress, follow routine, stay warm.")

    st.markdown("### ⏰ Daily Routine")
    st.write("Wake up early, eat on time, sleep well.")

elif prakriti == "Pitta":
    st.markdown("### 🥗 Aahar")
    st.write("Cooling, sweet foods. Rice, milk, fruits. Avoid spicy food.")

    st.markdown("### 🧘 Vihar")
    st.write("Avoid heat, practice yoga and meditation.")

    st.markdown("### ⏰ Daily Routine")
    st.write("Timely meals, calm activities, sleep before 11 PM.")

elif prakriti == "Kapha":
    st.markdown("### 🥗 Aahar")
    st.write("Light, warm food. Vegetables, barley.")

    st.markdown("### 🧘 Vihar")
    st.write("Regular exercise, avoid excess sleep.")

    st.markdown("### ⏰ Daily Routine")
    st.write("Early wake-up, active day, light dinner.")
    st.subheader("🤖 AI Ayurvedic Explanation")

ai_text = f"""
नमस्कार 🌸  
तुमची प्रकृती **{prakriti}** आहे  
आणि तुमचा अग्नी **{agni}** आहे.

याचा अर्थ असा की,
तुमच्या शरीराची कार्यपद्धत,
पचनशक्ती आणि ऊर्जा
या गोष्टी या प्रकृतीवर अवलंबून असतात.

योग्य आहार, विहार आणि दिनचर्या पाळल्यास
तुमचे आरोग्य नक्कीच सुधारेल.
"""
st.info(ai_text)

    tts = gTTS(text=ai_text, lang="mr")
    tts.save("voice.mp3")

    audio_file = open("voice.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
 st.subheader("🤖 AI Ayurvedic Chatbot")
    user_input = st.text_input("आपला प्रश्न टाका (उदा. माझा पचन कमी आहे, काय करावे?)")
    if user_input:
        response = f"तुमच्या प्रकृती {prakriti} आणि अग्नी {agni} नुसार: {user_input} साठी योग्य आहार व दिनचर्या पाळा."
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**AI:** {response}")

        # Voice output for chat
        tts_chat = gTTS(text=response, lang="mr")
        tts_chat.save("chat_voice.mp3")
        audio_file = open("chat_voice.mp3", "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
