import streamlit as st 
from cryptmoji import encrypt, decrypt

st.set_page_config(
    page_title="EmojiCrypto",
    layout="centered",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": open("./README.md").read(),
    },
)

st.markdown(open("./README.md").read())

with st.expander("Encrypt ", expanded=True):
    text = st.text_area(label="Text to encrypt")
    key = st.text_input(label="Keyword", value="random_string", key=11)
    if st.button("Encrypt"):
        if key.strip() != "" and text.strip() != "":
            encrypted_result = encrypt(text, key)
            st.write(encrypted_result)
        else:
            st.error("Please do fill all the required spaces.")    

with st.expander("Decrypt", expanded=False):
    text = st.text_area("Text to decrypt", key=20, max_chars=32)
    key = st.text_input("Keyword", value="random_string", key=21)
    if st.button("Decrypt"):
        if key.strip() != "" and text.strip() != "":
            decrypted_result = decrypt(text, key)
            st.write(decrypted_result)
        else:
            st.error("Please do fill all the required fields")

with st.expander("Read Docs ..."):
    st.write(open("Docs/installation.md").read())

    



