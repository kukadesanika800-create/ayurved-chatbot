import streamlit as st

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
    st.info("This is a preliminary assessment. Consult an Ayurvedic doctor for treatment.")
