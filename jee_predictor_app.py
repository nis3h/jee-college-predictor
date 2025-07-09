import streamlit as st
from predict_colleges import predict_colleges

import base64

# Custom Font + Background
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Roboto&display=swap" rel="stylesheet">
    <style>
        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Background Image Function
def set_bg_from_local(image_file):
    with open(image_file, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Call function with your image filename
set_bg_from_local("bg1.jpg")  # <-- change to your actual image file name

st.markdown("""
    <h1 style='color:#91171F; font-size:42px; font-weight:700; margin-bottom:10px;'>
        ₊⊹JEE College List Maker ⊹₊
</h1>
""", unsafe_allow_html=True)


#line
st.markdown(
    "<span style='color:#91171F; font-weight:600; font-size:20px;'>°-----------------------------------------------------------------------------------------------------------°</span>",
    unsafe_allow_html=True
)

st.markdown(
    "<span style='color:#91171F; font-weight:600; font-size:20px;'> ˗ˏˋ ★ ˎˊ˗ Enter your academic details below:</span>",
    unsafe_allow_html=True
)

st.markdown("""
    <style>
    /* Label text color */
    label {
        color: #91171F !important;
        font-weight: 600;
    }

    /* Input fields border */
    input[type="number"], input[type="text"] {
        border: 1.5px solid #91171F;
        padding: 0.4rem;
        border-radius: 5px;
    }

    input[type="number"]:focus, input[type="text"]:focus {
        outline: none;
        border: 2px solid #91171F;
    }

    /* Selectbox (category, gender) */
    div[data-baseweb="select"] {
        border: 1.5px solid #91171F;
        border-radius: 5px;
    }

    /* Dropdown + Slider title colors */
    .stSelectbox label, .stSlider label {
        color: #91171F !important;
        font-weight: 600;
    }

    /* Slider knob color */
    .stSlider > div[data-baseweb="slider"] > div {
        color: #91171F !important;
    }

    </style>
""", unsafe_allow_html=True)

# Input fields
rank = st.number_input("Your JEE Rank", min_value=1, step=1)

category = st.selectbox("Seat Type (Category)", [
    "OPEN", "EWS", "OBC-NCL", "SC", "ST"
])

gender = st.selectbox("Gender", ["Male", "Female"])

preferred_branch = st.text_input("Preferred Branch (Optional)", placeholder="e.g. Computer, Mechanical...")

# Predict button
if st.button("(„• ֊ •„) Show Eligible Colleges"):
    result_df = predict_colleges(rank, category, gender, preferred_branch)

    if not result_df.empty:
        st.markdown(f"""
<div style="background-color: rgba(145, 23, 31, 0.15);
            border-left: 5px solid #91171F;
            padding: 1rem;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            color: #91171F;
            margin-top: 1rem;">
    𖤐 Found {len(result_df)} eligible programs!
</div>
""", unsafe_allow_html=True)

        st.dataframe(result_df.reset_index(drop=True), use_container_width=True)
    else:
        st.warning("( ◡̀_◡́) No colleges found for your criteria.")
