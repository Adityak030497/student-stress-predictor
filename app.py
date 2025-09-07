import streamlit as st
import numpy as np
import plotly.graph_objects as go
import joblib

bundle = joblib.load("stress_model.pkl")
model      = bundle["model"]
FEATURES   = bundle["features"]
sleep_map  = bundle["sleep_map"]
junk_map   = bundle["junk_map"]

def predict_stress(inputs):
    score = float(model.predict([inputs])[0])
    score = float(np.clip(score, 0, 100))
    level = "Low" if score < 40 else ("Moderate" if score < 70 else "High")
    return score, level

def suggestions(vals):
    tips = []
    (sleep_hours, sleep_quality, study_hours, attendance_percent,
     deadlines, exercise_hours, caffeine, screen_time, social_media,
     family_support, peer_pressure, financial_concerns, junk_freq) = vals

    if sleep_hours < 6: tips.append("💤 Aim for 7–8 hours of sleep.")
    if sleep_quality == sleep_map["Poor"]: tips.append("😴 Improve sleep hygiene (no screens before bed).")
    if attendance_percent < 75: tips.append("🏫 Improve attendance; routine lowers stress.")
    if deadlines >= 5: tips.append("🗓️ Break assignments into smaller chunks; plan earlier.")
    if exercise_hours < 2: tips.append("🏃 Add 20–30 mins activity 3×/week.")
    if caffeine >= 3: tips.append("☕ Cut caffeine after 2pm.")
    if screen_time > 6 or social_media > 3: tips.append("📱 Reduce non-essential screen time.")
    if family_support <= 2: tips.append("👥 Lean on friends/mentors; schedule check-ins.")
    if peer_pressure >= 4: tips.append("🧭 Set boundaries; focus on your pace.")
    if financial_concerns >= 4: tips.append("💰 Use budgeting apps; seek student aid support.")
    if junk_freq >= junk_map.get("Often",3): tips.append("🥗 Swap junk snacks for fruit/nuts.")
    return tips

st.title("📊 Student Stress Predictor")
st.caption("Enter your current habits to estimate stress score and get personalized tips.")

sleep_hours  = st.slider("Sleep Hours (per day)", 0, 12, 6)
sleep_quality_lbl = st.selectbox("Sleep Quality", list(sleep_map.keys()))
sleep_quality = sleep_map[sleep_quality_lbl]

study_hours  = st.slider("Study Hours (per day)", 0, 12, 4)
attendance_percent = st.slider("Attendance (%)", 50, 100, 85)
deadlines    = st.slider("Assignment Deadlines / week", 0, 10, 3)
exercise     = st.slider("Exercise Hours / week", 0, 14, 3)
caffeine     = st.slider("Caffeine Intake (cups/day)", 0, 8, 1)
screen_time  = st.slider("Screen Time (hours/day)", 0, 14, 6)
social_media = st.slider("Social Media (hours/day)", 0, 8, 2)
family_sup   = st.slider("Family Support (1–5)", 1, 5, 3)
peer_press   = st.slider("Peer Pressure (1–5)", 1, 5, 3)
fin_concern  = st.slider("Financial Concerns (1–5)", 1, 5, 2)
junk_lbl     = st.selectbox("Junk Food Frequency", list(junk_map.keys()))
junk_freq    = junk_map[junk_lbl]

vals = [
    sleep_hours, sleep_quality, study_hours, attendance_percent,
    deadlines, exercise, caffeine, screen_time, social_media,
    family_sup, peer_press, fin_concern, junk_freq
]

if hasattr(model, "n_features_in_") and model.n_features_in_ != len(vals):
    st.error(f"Feature count mismatch: model expects {model.n_features_in_} features, app is sending {len(vals)}.")
    st.stop()

if st.button("Check Stress Level"):
    score, level = predict_stress(vals)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={'text': f"Stress Level: {level}"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red" if level == "High" else "orange" if level == "Moderate" else "green"},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "lightyellow"},
                {'range': [70, 100], 'color': "lightcoral"},
            ],
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📌 Personalized Suggestions")
    tips = suggestions(vals) 
    if tips:
        for t in tips:
            st.write("- ", t)
    else:
        st.success("✅ Your habits look well balanced!")
