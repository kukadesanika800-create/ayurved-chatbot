import streamlit as st
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    if "female" in voice.name.lower() or "zira" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

if st.button("Get Result"):
    st.success(f"🌿 Your Prakriti: {max(prakriti_score, key=prakriti_score.get)}")
    st.success(f"🔥 Your Agni Type: {max(agni_score, key=agni_score.get)}")
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
Your Prakriti is {prakriti} and your Agni is {agni}.
Based on this, your body needs proper diet, lifestyle and routine.
Please follow the suggested Aahar, Vihar and Dinacharya.
"""

st.write(ai_text)

if st.button("🔊 Listen AI Explanation (Female Voice)"):
    speak(ai_text)
    
    st.info("This is a preliminary assessment. Consult an Ayurvedic doctor for treatment.")
