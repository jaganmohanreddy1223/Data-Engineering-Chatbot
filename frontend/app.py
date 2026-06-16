import streamlit as st
import requests

st.title("🤖 Data Engineering Assistant")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)

# Upload Button
if st.button("Upload Dataset"):

    if uploaded_file is not None:

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        }

        upload_response = requests.post(
            "http://127.0.0.1:8000/upload",
            files=files
        )

        if upload_response.status_code == 200:
            st.success(upload_response.json()["message"])
        else:
            st.error(upload_response.text)

    else:
        st.warning("Please select a file first.")

st.divider()

# Chat Section
question = st.text_input("Ask a question")

if st.button("Send"):

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": question}
    )

    if response.status_code == 200:
        st.success(response.json()["response"])
    else:
        st.error(response.text)

st.divider()

# Download Section
if st.button("📥 Download Cleaned Dataset"):

    download_url = "http://127.0.0.1:8000/download"

    st.markdown(
        f"[📥 Click Here To Download Cleaned Dataset]({download_url})"
    )