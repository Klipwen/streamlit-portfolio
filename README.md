# Gee Caliph A. Juen - Streamlit Portfolio & Autobiography

**Course:** CSIT 349 (Applied AI)  
**Section:** CSIT349 - G01  
**Student:** Gee Caliph A. Juen  
**Institution:** Cebu Institute of Technology – University (CIT-U)  

---

## 🌟 Overview
This interactive Streamlit web application fulfills all criteria for the **Autobiography and Portfolio App** assignment under CSIT 349. It integrates core Streamlit lecture components alongside interactive extra components for a responsive and intuitive personal site experience.

## 🛠️ Streamlit Components Utilized
- **Page Configuration & Theming:** `st.set_page_config`, `.streamlit/config.toml`
- **Text & Structure:** `st.title`, `st.header`, `st.subheader`, `st.write`, `st.markdown`, `st.divider`
- **Layout:** `st.sidebar`, `st.columns`, `st.tabs`, `st.expander`
- **Visuals & Charts:** `st.image` (Profile photo stand-in), `st.dataframe` (Interactive table), `st.bar_chart` (Dynamic skill rating)
- **Input Widgets:** `st.slider`, `st.selectbox`, `st.checkbox`, `st.radio`, `st.multiselect`, `st.text_input`, `st.text_area`
- **Interactive Triggers:** `st.button`, `st.form_submit_button`, `st.download_button` (Resume / Bio summary)
- **Feedback & State:** `st.form`, `st.metric`, `st.session_state` (Message history), `st.balloons`, `st.toast`, `st.success`, `st.info`, `st.warning`, `st.error`

---

## 🚀 Running Locally

1. Clone or download this repository.
2. Ensure Python 3.10+ is installed.
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the application:
   ```bash
   streamlit run app.py
   ```
5. Open your browser at `http://localhost:8501`.

---

## ☁️ Deploying to Streamlit Community Cloud (Option B)

1. Push this folder to a new public repository on GitHub (e.g. `streamlit-autobiography-portfolio`).
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
3. Click **New app**.
4. Select your repository, branch (`main`), and set the main file path to `app.py`.
5. Click **Deploy!**
6. Copy the resulting public `.streamlit.app` URL and submit it on MS Teams!
