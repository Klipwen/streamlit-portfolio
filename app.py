import os
import pandas as pd
import streamlit as st

# ==============================================================================
# 1. PAGE CONFIGURATION (Extra Component: Theme / Page Config)
# ==============================================================================
st.set_page_config(
    page_title="Gee Caliph Juen | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling for polished, modern look
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        color: #94a3b8;
        font-size: 1.15rem;
        margin-bottom: 1.5rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        background-color: #2563eb;
        color: white;
        margin-right: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State (Extra Component: Session State)
if "feedback_history" not in st.session_state:
    st.session_state.feedback_history = []

# ==============================================================================
# 2. SIDEBAR (Sidebar, Images, Visibility Toggle, Resume Download)
# ==============================================================================
st.sidebar.title("📌 Student Info")

# Avatar / Profile Photo (Extra Component: Image display with stand-in label)
avatar_path = os.path.join(os.path.dirname(__file__), "assets", "avatar.png")
if os.path.exists(avatar_path):
    st.sidebar.image(avatar_path, caption="📸 Profile Photo Stand-in", width=170)
else:
    st.sidebar.markdown("### 📸 [Profile Photo Placeholder]")

st.sidebar.markdown("### **Gee Caliph A. Juen**")
st.sidebar.markdown("**Class Section:** `CSIT349 - G01`")
st.sidebar.markdown("📍 **Location:** Medellin, Cebu, Philippines")
st.sidebar.markdown("🎓 **Degree:** BSIT Student @ **CIT-U**")
st.sidebar.markdown("🏫 **School:** Cebu Institute of Technology – University")
st.sidebar.divider()

# Checkbox Component
show_advanced = st.sidebar.checkbox("Show Advanced Tech Stack", value=True)

# Extra Component: Download Button for Resume / Summary
resume_text = """GEE CALIPH A. JUEN
BSIT Student | Cebu Institute of Technology - University
Class: CSIT349 - G01 | Medellin, Cebu

PROFILE SUMMARY:
Pragmatic, hands-on software engineering student with expertise in prototype development,
full-stack development, and UI/UX engineering.

CORE COMPETENCIES:
- Frontend: React Native, React.js, Tailwind CSS
- Backend: Python (Django), Java (Spring Boot)
- Cloud & Infrastructure: AWS (EC2, VPC, Load Balancers), SysAdmin, VirtualBox
- Databases: Supabase, MySQL, PostgreSQL
- AI Integration: Google Gemini 2.5 Flash API

FEATURED PROJECTS:
1. Presyohan-V2: Real-time multi-store price monitoring with AI pricelist scanner.
2. CipherQuest: Gamified cybersecurity education platform.
3. Code-IT: Browser-based multi-language code execution environment.
"""

st.sidebar.download_button(
    label="📄 Download Profile Summary",
    data=resume_text,
    file_name="Gee_Caliph_Juen_Summary.txt",
    mime="text/plain",
    help="Download a plain-text copy of Gee Caliph's credentials and portfolio summary.",
)

st.sidebar.divider()
st.sidebar.caption("CSIT 349: Applied AI · Activity Submission")

# ==============================================================================
# 3. HEADER & METRICS SUMMARY (Text, Headers, Metrics)
# ==============================================================================
st.markdown('<div class="main-title">Gee Caliph A. Juen</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">BSIT Student · Software Engineer · Problem Solver | Section: <b>CSIT349 - G01</b></div>',
    unsafe_allow_html=True,
)

# Metrics summary row (Extra Component: Metrics)
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric(label="Featured Projects", value="3", delta="Full-Stack & AI")
with metric_col2:
    st.metric(label="Primary Skills", value="6+", delta="Cloud & Dev")
with metric_col3:
    st.metric(label="Academic Institution", value="CIT-U", delta="Cebu, PH")
with metric_col4:
    st.metric(label="Target Degree", value="BSIT", delta="Senior Coursework")

st.write("---")

# ==============================================================================
# 4. AUTOBIOGRAPHY (Text components & Columns)
# ==============================================================================
st.header("📖 Autobiography")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    **Background:**  
    I am a pragmatic, hands-on software engineering student with a strong focus on end-to-end prototyping and UI/UX design. I prefer resource-conscious solutions and real-world utility over purely theoretical concepts.

    **Education:**  
    Currently pursuing my Bachelor of Science in Information Technology (BSIT) at **Cebu Institute of Technology – University (CIT-U)**. My coursework heavily involves AWS cloud infrastructure, ServiceNow, systems administration, and software engineering.
    """)

    # Extra Component: Expander for deeper educational details
    with st.expander("🔍 View Core Coursework & Certifications"):
        st.write("""
        - **Cloud Infrastructure:** AWS Academy Cloud Architecting (EC2, IAM, VPC, S3, RDS, ALBs).
        - **Enterprise Platforms:** ServiceNow Application Development & IT Service Management.
        - **Systems Administration:** Linux server configuration, bash scripting, VirtualBox networking.
        - **Applied AI (CSIT 349):** Model integrations, Prompt Engineering, Streamlit deployment.
        """)

with col2:
    if show_advanced:
        st.info("💡 **Tech Stack Highlights:**\nReact Native, Python, Django, Spring Boot, Tailwind CSS, Supabase, MySQL.")

    # Radio Component
    milestone_view = st.radio(
        "Filter Milestones by Category:",
        ["All", "Cloud/SysAdmin", "Development", "Design"],
    )

st.subheader("🏆 Career & Academic Milestones")
if milestone_view in ["All", "Cloud/SysAdmin"]:
    st.write("- ☁️ **Oct 2026:** Configured AWS cloud infrastructure including EC2, security groups, and load balancers.")
    st.write("- 🖥️ **Jul 2026:** Completed practical systems administration credentials in VirtualBox.")
if milestone_view in ["All", "Development"]:
    st.write("- 💻 **May 2026:** Developed **'Code-IT'**, a multi-language browser-based code execution environment.")
if milestone_view in ["All", "Design"]:
    st.write("- 📐 **Mar 2026:** Designed a complete 100 sqm single-storey residential architectural layout in SketchUp.")

st.write("---")

# ==============================================================================
# 5. TECHNICAL SKILLS (Table, Chart, and Slider)
# ==============================================================================
st.header("🛠️ Technical Skills")

# Slider Component
min_skill = st.slider(
    "Filter skills by minimum proficiency (%)",
    min_value=0,
    max_value=100,
    value=50,
    step=5,
    help="Adjust slider to filter technical skills displayed in the table and chart.",
)

skills_data = {
    "Skill": [
        "React / React Native",
        "Python / Django",
        "Java Spring Boot",
        "AWS / SysAdmin",
        "UI/UX Design",
        "MySQL / Supabase",
    ],
    "Proficiency (%)": [90, 85, 80, 75, 85, 80],
}

df_skills = pd.DataFrame(skills_data)
filtered_skills = df_skills[df_skills["Proficiency (%)"] >= min_skill]

skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    st.write("**Skills Data Table**")
    st.dataframe(filtered_skills, use_container_width=True)  # Table Component

with skill_col2:
    st.write("**Proficiency Chart**")
    if not filtered_skills.empty:
        chart_data = filtered_skills.set_index("Skill")
        st.bar_chart(chart_data)  # Chart Component
    else:
        st.warning("No skills match the selected minimum proficiency threshold.")

st.write("---")

# ==============================================================================
# 6. FEATURED PROJECTS (Tabs & Metrics - Extra Components)
# ==============================================================================
st.header("🚀 Featured Projects")
tab1, tab2, tab3 = st.tabs(["Presyohan-V2", "CipherQuest", "Code-IT"])

with tab1:
    st.subheader("Presyohan-V2")
    p1_col1, p1_col2 = st.columns([3, 1])
    with p1_col1:
        st.write("**Role:** Lead Developer")
        st.write("**Tools Used:** Gemini 2.5 Flash, React Native, AI integrations, Supabase.")
        st.write("**Outcome:** A real-time multi-store price monitoring and inventory synchronization platform featuring AI-powered pricelist scanning.")
    with p1_col2:
        st.metric(label="Status", value="Active Dev", delta="AI Powered")
        st.button("Explore Presyohan-V2 Specs", key="btn_p1", help="Simulate exploring project specifications.")

with tab2:
    st.subheader("CipherQuest")
    p2_col1, p2_col2 = st.columns([3, 1])
    with p2_col1:
        st.write("**Role:** Full-Stack Developer")
        st.write("**Tools Used:** React, Spring Boot, Gamification Logic, MySQL.")
        st.write("**Outcome:** Built a gamified cybersecurity e-learning platform for classical ciphers with interactive modes and leaderboards.")
    with p2_col2:
        st.metric(label="Platform Type", value="Cybersecurity", delta="Educational")
        st.button("View CipherQuest Levels", key="btn_p2", help="Simulate previewing interactive cybersecurity challenges.")

with tab3:
    st.subheader("Code-IT")
    p3_col1, p3_col2 = st.columns([3, 1])
    with p3_col1:
        st.write("**Role:** Backend/Frontend Developer")
        st.write("**Tools Used:** Python, Java, Web execution environments, Docker.")
        st.write("**Outcome:** Completed a browser-based multi-language code execution environment for educational coding sandboxes.")
    with p3_col2:
        st.metric(label="Execution Sandbox", value="Multi-Lang", delta="Browser Ready")
        st.button("Run Code-IT Sandbox", key="btn_p3", help="Simulate launching web-based code executor.")

st.write("---")

# ==============================================================================
# 7. INTERESTS & HOBBIES (Multiselect & Status Boxes)
# ==============================================================================
st.header("⛰️ Interests & Hobbies")
hobbies = st.multiselect(
    "Select an interest to learn more:",
    ["Mountain Hiking", "3D Modeling & Design", "Gaming", "Anime"],
    default=["Mountain Hiking", "3D Modeling & Design"],
)

if "Mountain Hiking" in hobbies:
    st.success("🥾 **Mountain Hiking:** I frequently hike mountain trails across Cebu Province, tracking elevation profiles and route statistics.")
if "3D Modeling & Design" in hobbies:
    st.info("📐 **3D Modeling & Design:** I enjoy exploring tools like SketchUp and Blender, and designing 2D/3D floor plan visualizations.")
if "Gaming" in hobbies:
    st.warning("🎮 **Gaming:** I play mobile MOBAs, specifically mastering characters like Zhask in Mobile Legends.")
if "Anime" in hobbies:
    st.error("🎌 **Anime:** I follow series like Jujutsu Kaisen, analyzing story arcs and character abilities.")

st.write("---")

# ==============================================================================
# 8. CONTACT & FEEDBACK FORM (Form, Text Input, Text Area, Selectbox, Button)
# ==============================================================================
st.header("📬 Contact & Feedback Form")

with st.form("contact_form", clear_on_submit=True):
    st.write("Leave some feedback or reach out for collaboration!")
    # Text Input & Selectbox
    name = st.text_input("Your Name", placeholder="e.g., Juan Dela Cruz")
    email = st.text_input("Your Email (Optional)", placeholder="e.g., juan@example.com")
    inquiry_type = st.selectbox(
        "Reason for Contact",
        ["General Inquiry", "Project Collaboration", "Feedback", "Academic Inquiry"],
    )
    # Text Area
    message = st.text_area("Your Message", placeholder="Type your message here...")
    
    # Submit Button Component
    submitted = st.form_submit_button("Send Message")

if submitted:
    if name.strip() and message.strip():
        # Extra Component: Balloons celebration on success
        st.balloons()
        # Extra Component: Toast notification
        st.toast(f"Message received from {name}!", icon="✅")
        st.success(f"Thank you for reaching out, **{name}**! Your **{inquiry_type.lower()}** has been successfully recorded.")
        
        # Save to Session State
        st.session_state.feedback_history.append({
            "Name": name,
            "Type": inquiry_type,
            "Message": message,
        })
    else:
        st.error("⚠️ Please fill out both your name and a message before submitting.")

# Show recent feedback messages if any exist (Extra Component: Dynamic List / Session State)
if st.session_state.feedback_history:
    with st.expander(f"📝 Recent Messages Submitted ({len(st.session_state.feedback_history)})"):
        for i, item in enumerate(reversed(st.session_state.feedback_history), 1):
            st.markdown(f"**{i}. {item['Name']}** (*{item['Type']}*): {item['Message']}")

# Footer
st.write("---")
st.caption("Developed by **Gee Caliph A. Juen** · CIT-U BSIT · Section CSIT349 - G01 · Powered by Streamlit")
