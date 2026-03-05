import streamlit as st

# Başlık
st.title("Mini Chat Uygulaması")

# Mesaj geçmişini session_state ile sakla
if "messages" not in st.session_state:
    st.session_state.messages = []

# Kullanıcı mesajı input
user_input = st.text_input("Mesajını yaz:", "")

# Gönder tuşu
if st.button("Gönder"):
    if user_input:
        st.session_state.messages.append(f"Kullanıcı: {user_input}")
        user_input = ""  # inputu temizle

# Mesajları göster
st.write("### Sohbet geçmişi:")
for msg in st.session_state.messages:
    st.write(msg)
