import os
import base64
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import altair as alt

# ----------------------
# PAGE CONFIG
# ----------------------
st.set_page_config(
    page_title="Hello, I’m Eunice 🌷",
    page_icon="🌷",
    layout="wide"
)

# ----------------------
# GLOBAL STYLING
# ----------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

.stApp {
    font-family: 'Inter', sans-serif;
    padding: 2rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #3f3d56;
}

.card {
    background: linear-gradient(135deg,#A3C1DA,#C9E4CA);
    padding: 1rem;
    border-radius: 14px;
    text-align: center;
    margin-bottom: 1rem;
    font-weight: 500;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.08);
}

.hero-container {
    display: flex;
    gap: 2rem;
    align-items: flex-start;
}

.hero-left {
    flex: 1;
    text-align: center;
}

.hero-left img {
    width: 100%;
    max-width: 280px;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    border-radius: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}

.hero-meta {
    font-weight: 600;
    font-size: 16px;
    margin-top: 0.75rem;
}

.hero-right {
    flex: 2;
}

.hero-text {
    background: linear-gradient(120deg,#FDE2FF 0%,#C9E4CA 100%);
    padding: 1.25rem;
    border-radius: 14px;
}

.hero-text p, .hero-text div {
    font-size: 18px;
    line-height: 1.7;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# ----------------------
# HERO SECTION (Fully Self-Contained)
# ----------------------

photo_file = "my_photo.jpg.jpeg"  # match your exact file name

# Encode the image if found
encoded = None
if os.path.exists(photo_file):
    with open(photo_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

hero_html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

.hero-container {{
    display: flex;
    gap: 2rem;  /* slightly larger gap for bigger image */
    align-items: flex-start;
    font-family: 'Inter', sans-serif;
    max-width: 1000px;  /* limit width */
    margin: 0 auto;      /* center horizontally */
}}

.hero-left {{
    flex: 0 0 350px;  /* bigger fixed width for image */
    text-align: center;
}}

.hero-left img {{
    width: 100%;
    aspect-ratio: 3 / 4;
    object-fit: cover;
    border-radius: 14px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
}}

.hero-meta {{
    font-weight: 600;
    font-size: 16px;
    margin-top: 0.75rem;
}}

.hero-right {{
    flex: 1;  /* text takes remaining space */
}}

.hero-text {{
    background: linear-gradient(120deg,#FDE2FF 0%,#C9E4CA 100%);
    padding: 1rem;
    border-radius: 14px;
}}

.hero-text div {{
    font-size: 20px;
    line-height: 1.6;
    font-weight: 700;
}}
</style>

<div class="hero-container">

  <div class="hero-left">
    {"<img src='data:image/jpg;base64," + encoded + "'>" if encoded else "<div style='padding:1rem; background:#C9E4CA; border-radius:12px;'>No profile image 🌷</div>"}

    <div class="hero-meta">
      <b>Name:</b> Adegbola Aanuoluwa Eunice<br>
      <b>Field:</b> Electrochemistry & Nanosensing<br>
      <b>Institution:</b> North-West University, Mahikeng<br>
      <b>Degrees:</b> B.Tech, M.Tech, Ph.D in view
    </div>
  </div>

  <div class="hero-right">
    <div class="hero-text">
      <div>
        Hello, I’m Eunice 🌷<br><br>
        A small girl, greatly motivated by others’ successes, while observing the world with curiosity and wonder.
        Over time, this curiosity grew into careful exploration of <b>chemistry, materials, and nanosensing</b>,
        learning how tiny bits and small designs can make meaningful change.
      </div>
      <br>
      <div>
        I am particularly drawn to <b>sustainable nanomaterials</b> and <b>electrochemical sensing</b>,
        integrating green synthesis and thoughtful design to build stable, sensitive and selective detection systems.
      </div>
      <br>
      <div>
        I enjoy a quiet, visual, and meaningful work : where progress unfolds steadily,
        thoughtfully, and deliberately.
      </div>
    </div>
  </div>

</div>
"""

# Give a slightly taller height since image is bigger
components.html(hero_html, height=600)
st.divider()


# CURIOSITY CARDS
st.subheader("What I’m becoming curious about lately")
curiosities = [
    "🌱 Sustainable nanomaterials",
    "🔬 Electrochemical sensors",
    "🌍 Environmentally responsible chemistry",
    "✨ Turning data into understanding"
]
cols = st.columns(len(curiosities))
for i, c in enumerate(curiosities):
    with cols[i]:
        st.markdown(f"<div class='card'>{c}</div>", unsafe_allow_html=True)
st.divider()

# ----------------------
# RESEARCH JOURNEY
# ----------------------
st.subheader("My Research Journey So Far")
journey_stages = [
    "📘 Foundations — Learning chemistry’s language",
    "📗 Application — Connecting chemistry to real world",
    "📙 Focus — Nanosensing, sustainability, and meaningful impact"
]
for i, stage in enumerate(journey_stages, start=1):
    if i < 3:
        st.markdown(f"✅ Step {i}: {stage}")
    else:
        st.markdown(f"🔹 **Step {i}: {stage} (Current Stage)**")
st.divider()

# ----------------------
# RESEARCH EVOLUTION
# ----------------------
st.subheader("Research evolution (a moment in motion)")
research_trend = pd.DataFrame({
    "Stage": ["Computational Chemistry", "Applied / Food Chemistry", "Nanoscience & Nanosensing"],
    "Focus (%)": [30, 30, 40]
})

chart = (
    alt.Chart(research_trend)
    .mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6)
    .encode(
        x=alt.X("Stage:N", title=None),
        y=alt.Y("Focus (%):Q"),
        color=alt.Color("Stage:N", legend=None),
        tooltip=["Stage", "Focus (%)"]
    )
    .properties(height=280)
)

st.altair_chart(chart, use_container_width=True)
st.markdown("**Not an endpoint, but a milestone in a path of continuous growth.**")
st.divider()

# ----------------------
# PUBLICATIONS
# ----------------------
st.subheader("Things I’ve put into the world 🌱")

publications_file = "PUBLICATIONS.csv"

if os.path.exists(publications_file):
    publications = pd.read_csv(publications_file, encoding="latin1")
    publications = publications.replace("\xa0", " ", regex=True)
    publications.columns = publications.columns.str.strip().str.upper()

    keyword = st.text_input("Search gently by keyword")
    filtered = publications

    if keyword:
        filtered = publications[
            publications.astype(str)
            .apply(lambda col: col.str.lower().str.contains(keyword.lower()))
            .any(axis=1)
        ]

    with st.expander("Open my publications"):
        st.dataframe(filtered, width="stretch")

    if "YEAR" in filtered.columns:
        filtered["YEAR"] = pd.to_numeric(filtered["YEAR"], errors="coerce")
        year_counts = filtered["YEAR"].value_counts().sort_index()

        if not year_counts.empty:
            st.write("How this space has grown over time")
            st.bar_chart(year_counts, width="stretch")

else:
    st.info("Publications will appear here soon 🌱")

st.divider()
# ----------------------
# HOBBIES & INTERESTS
# ----------------------
st.subheader("Beyond results: What keeps me inspired")
hobbies = [
    "🎨 Visual patterns & designs",
    "📚 Reading & writing",
    "📝 Quiet reflection",
    "💻 Surfing the internet & exploring ideas",
    "🍰 Baking & cooking",
    "📊 Exploring data & patterns"
]
cols = st.columns(len(hobbies))
for i, h in enumerate(hobbies):
    with cols[i]:
        st.markdown(f"<div class='card'>{h}</div>", unsafe_allow_html=True)
st.divider()

# ----------------------
# CONTACT
# ----------------------
st.subheader("Contact Me ✉️")
st.markdown(
    "<p style='text-align:center; font-style:italic;'>This page will keep changing , just like my work.</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; font-weight:600;'>📧 adegokeaanuoluwapo5@gmail.com</p>",
    unsafe_allow_html=True
)



