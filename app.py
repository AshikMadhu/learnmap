import streamlit as st
import time

st.set_page_config(page_title="LearnMap", layout="centered")

# ----------- PREMIUM UI CSS -----------
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: #e2e8f0;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: 700;
    background: linear-gradient(90deg, #6366f1, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}

/* Glass Card */
.card {
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 18px;
    transition: all 0.3s ease;
}

/* Hover glow */
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 30px rgba(34,211,238,0.15);
}

/* Inputs */
input, textarea {
    background-color: #020617 !important;
    color: white !important;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 48px;
    border-radius: 12px;
    border: none;
    font-weight: 600;
    background: linear-gradient(90deg, #6366f1, #22d3ee);
    color: white;
    transition: 0.3s;
}

/* Button hover */
.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(99,102,241,0.5);
}

/* Fade animation */
.fade {
    animation: fadeInUp 0.6s ease;
}

@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Highlight */
.highlight {
    color: #22d3ee;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ----------- HEADER -----------
st.markdown('<div class="title">🧭 LearnMap</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Craft your learning journey with clarity</div>', unsafe_allow_html=True)

# ----------- INPUT SECTION -----------
st.markdown('<div class="card">', unsafe_allow_html=True)

topic = st.text_input("🎯 What do you want to master?")
level = st.selectbox("📊 Experience Level", ["Beginner", "Intermediate", "Advanced"])
duration = st.selectbox("⏳ Time Commitment", ["2 Weeks", "4 Weeks", "8 Weeks"])
goal = st.text_input("💡 Your End Goal", placeholder="Get job-ready / build real projects")

generate = st.button("✨ Generate Smart Roadmap")

st.markdown('</div>', unsafe_allow_html=True)

# ----------- OUTPUT -----------
if generate:

    if topic == "":
        st.warning("Enter a topic to generate roadmap")
    else:
        st.success("Designing your roadmap...")

        # Smooth loading
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.008)
            progress.progress(i + 1)

        # Output
        st.markdown('<div class="fade">', unsafe_allow_html=True)

        st.markdown(f"""
<div class="card">
<h2>📚 {topic} Roadmap</h2>
<p><span class="highlight">{level}</span> • {duration}</p>
</div>

<div class="card">
<h3>🧠 Phase 1 — Foundation</h3>
<ul>
<li>Core concepts of {topic}</li>
<li>Understand fundamentals deeply</li>
<li>Beginner-friendly resources</li>
</ul>
</div>

<div class="card">
<h3>⚙️ Phase 2 — Build Skills</h3>
<ul>
<li>Hands-on practice</li>
<li>Mini projects</li>
<li>Problem-solving approach</li>
</ul>
</div>

<div class="card">
<h3>🚀 Phase 3 — Real Application</h3>
<ul>
<li>Advanced projects</li>
<li>Real-world use cases</li>
<li>Portfolio creation</li>
</ul>
</div>

<div class="card">
<h3>🎯 Outcome</h3>
<p>{goal if goal else "Confident and industry-ready"}</p>
</div>
""", unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # Download
        roadmap = f"{topic} roadmap - {duration}"
        st.download_button("📥 Download Roadmap", roadmap)