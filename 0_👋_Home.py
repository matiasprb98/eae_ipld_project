import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Matias Proaño Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** Matias Proaño")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Matias Proaño""", unsafe_allow_html=True)  


# ----- Profile image file -----
profile_image_file_path = "profile.jpg"        

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Economist & Big Data Analytics Enthusiast"

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 Economist with a specialisation in finance, graduate and on my way to a master's degree in Big Data & Analytics.My strong economic background and commitment to growth positions me to seize opportunities and bringanalytical freshness to new challenges..
- 🛩️ prev: <I Led a B2B project selling customized vegetables to multiple hotels and restaurants in the city, my teamwork and I were able to reduce up to 13 percent of the costs, that includes the purchase of supplies and logistics services.
I was able to develop an analysis of the competition by taking out theaverage prices that were on sale to the public in order to decide ourprices to go to market.
I had the opportunity to solve inventory control problems with programmers from Israel for the correct function of the e
commerce web site.>
- ❤️ <football, music, trips, fitness>

- 🤖 <Big data & analytics master's degree>

- 🏂 <Drums>

- 📫 How to reach me: <proanomatias@gmail.com >

- 🏠 Barcelona
""")


