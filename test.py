import streamlit as st
from streamlit_image_comparison import image_comparison

# importing other files
import sys 
sys.path.append('../')
import dumpp as dd
import warnings
warnings.ignore_warnings()

def masking_image(masking_list):
    options = st.multiselect(
    'Choose the Masking U want',
    masking_list,
    default = dd.masking_list[:2])
    st.write(dd.hamza_func(options))

# page title
st.set_page_config("Webb Space Telescope vs Hubble Telescope", "🔭")
# image
st.image(
    "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/325/telescope_1f52d.png",
    width=120,
)

st.header("HEADER")
st.write("")

radio = st.sidebar.radio("Choose the Dataset", ["Flavo", "Sfbay", "Uplode your own"])

if radio == "Flavo":
    st.markdown("### Flavo")
    image_comparison(
        img1="assets/deep_field_700.jpg",
        img2="assets/deep_field_700_after.jpg",
        label1="Hubble",
        label2="Webb",
    )
    masking_image(dd.masking_list)
    

elif radio == "Sfbay":
    st.markdown("### Sfbay")
    image_comparison(
        img1="assets/southern_nebula_700.jpg",
        img2="assets/southern_nebula_700_after.jpg",
        label1="Hubble",
        label2="Webb",
    )
    masking_image(dd.masking_list)

elif radio == "Uplode your own":
    uploded_file = st.file_uploader("Upload your own image", type=["bin"])
    if uploded_file is not None:
        st.image(uploded_file)
        st.write("")
        st.markdown("### Your Image")
        image_comparison(
            img1=uploded_file,
            img2=uploded_file,
            label1="Hubble",
            label2="Webb",
        )

