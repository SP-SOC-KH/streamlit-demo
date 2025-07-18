import streamlit as st
import pandas as pd
import json
import os

from auth import check_password


if not check_password():
    st.stop()
    
# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App: File Upload"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("File Uplod")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt", "json"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    # Save the uploaded file to disk
    # save_path = f"saved_{uploaded_file.name}"
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success(f"✅ File saved as: `{save_path}`")

    # Check file type and read accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
        st.write("Preview of CSV file:")
        st.dataframe(df)

    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
        st.write("Preview of Excel file:")
        st.dataframe(df)
        # type(df)

    elif uploaded_file.name.endswith('.json'):
        import json
        data = json.load(uploaded_file)
        st.write("JSON content:")
        st.json(data)

    elif uploaded_file.name.endswith('.txt'):
        content = uploaded_file.read().decode("utf-8")
        st.text("Text file content:")
        st.text(content)