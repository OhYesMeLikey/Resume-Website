from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# Load Assets
lottie_coding = (
    "https://lottie.host/d7eb0f53-d425-4a74-b54b-e2b026043e37/Oou7Mgj3M7.json"
)
img_bot = Image.open("images/Bot.jpg")

# Header
with st.container():
    st.subheader("Hi. I'm Leo. :wave:")
    st.title(
        "A recent graduated Electrical Engineering and Computing Tech student from uOttawa."
    )
    st.write(
        "I am a passionate explorer that is willing to learn any and every skills that will allow me to create my future software and hardware projects."
    )
    st.write("[Learn More >](https://github.com/OhYesMeLikey?tab=repositories)")

# Projects
# First project
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")
    img_col, text_col = st.columns((1, 2))
    with img_col:
        st.image(img_bot)
    with text_col:
        st.header("OpenCV Object Detection")
        st.write("I'll write this later")
        st.markdown(
            "[Learn More >](https://github.com/OhYesMeLikey/OpenCV-Object-Detection)"
        )

# Contact Info
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/leotan213@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="Your name" required>
     <input type="email" name="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
     </form>
     """
    left_col, right_col = st.columns(2)
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st.empty()
