from pathlib import Path

import streamlit as st
from PIL import Image

# ---PATH SETTINGS----
current_dir=Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file=current_dir/"styles"/ "main.css"
resume_file=current_dir/"assets"/ "Resume MN.docx"
profile_pic=current_dir/"assets"/ "profile-pic.png"


#------GENERAL SETTINGS ----
PAGE_TITLE= "Digital CV |Sherwin Varghese"
PAGE_ICON= ":wave:"
NAME= "Sherwin Varghese"
DESCRIPTION= """

As a budding data analyst, I leverage data transformation skills to facilitate informed decisions and stimulate business growth.

"""
EMAIL= "varghesesheriwn@gmail.com"
SOCIAL_MEDIA={
    "LinkedIn": "https://linkedin.com/in/sherwin14",
    "Github": "https://github.com/Sherwin-14",
    "Youtube": "",
    "Twitter": ""
}

PERSONAL_PROJECTS={

    "🏆 English Premier League Analysis - Dashboard on EPL Season 20/21 " : "https://github.com/Sherwin-14/English_Premier_Analysis",
    "🏆 Polish Property Market Overview - Dashboard on Poland's Property Market " : "https://github.com/Sherwin-14/Polish-Property-Market-Overview",
    "🏆 PixieDust Plots - Dashboard on Walt Disney Company":"https://github.com/Sherwin-14/PixieDust/tree/master",
    "🏆 BeatBoard - Dashboard on Spotify" :"https://github.com/Sherwin-14/BeatBoard ",
    "🏆 Revenue Insights Hospitality Domain - Dashboard on Hospitality Domain" :"https://github.com/Sherwin-14/Hospitality_Domain ",
    
}


st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


# ----LOAD ,CSS,PDF AND PROFILE PIC-----

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)

#---HERO SECTION---

col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet_stream"
    ) 
    st.write("📫 ",EMAIL)   


#----SOCIAL LINKS_----
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")        

#----Experience and Qualifications---
st.write("#")
st.subheader("Experience and Qualifications")
st.markdown(
    """
- ✔️ Earned a Bachelor’s degree in Industrial Engineering from SGSITS, Indore.
- ✔️ Studied subjects like Operations Research, Supply Chain Management, and OOPS.
- ✔️ Worked as a Project Engineer at IIT Indore.
- ✔️ Good Understanding of statistical principles and their respective applications.
- ✔️ Excellent team player with good problem-solving skills.
"""
)


#-----SKILLS ----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
   - 👨‍💻 Programming - Python, C/C++, SQL
   - 📊 Data Visualization - Matplotlib, Seaborn, Plotly, MS-Excel, Power BI
   - 💽 Databases  -  PostgresSQL, MongoDB
   - 📚 Libraries  -  Pandas, Numpy, OpenCV, Visual Python, CryptoGraphy, Simpy
   - 🍶 Frameworks -  Plotly-Dash, Flask, Streamlit 
   - 🔧 Dev Tools  -  Git, Jupyter Notebook, VS Code, Pycharm, Postman, Jira 
"""
)

#---WORK HISTORY---
st.write("#")
st.subheader("Work History")
st.write("---")

#---JOB 1
st.write(" 🚧 ","**Project Engineer | IIT Indore**")
st.write("06/2023- 10/2023")
st.write(
    """
     - ► Addressed challenges by conducting comprehensive research on the Simulation and MedTech industry.
     - ► Led the development of a web application using Streamlit and Visual Python for real-time simulation visualization, which increased team productivity by 40%.
     - ► Developed an effective scheduling algorithm for job processing in the simulation, which cut down the runtime by 25%.
     - ► Rectified significant bugs, thereby improving the performance and dependability of the simulation software.
     - ► Oversaw a team to exhibit the product’s features at SETU, an event hosted by IIT Indore.

"""
)


#---JOB 2
st.write(" 🚧 ","**Supply Chain Analyst | Premeir Interio**")
st.write("01/2023- 05/2023")
st.write(
    """
     - ► Implemented a Just-In-Time inventory system, reducing carrying costs by 30% and boosting inventory turnover by 25%
     - ► Leveraged Excel dashboards for real-time inventory analysis, optimizing stock levels based on demand forecasts.

"""
)

#------Projects & Accomplishments---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("----")

for project,link in PERSONAL_PROJECTS.items():
    st.write(f"[{project}]({link})")
