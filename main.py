import streamlit as st

# Başlık
st.title("Python Web GUI Paneli")

# Kullanıcıdan input al
text = st.text_input("Bir şey yaz:")

# Gönder düğmesi
if st.button("Gönder"):
    if text:  # Boş değilse göster
        st.success(f"Yazdığın şey: {text}")
    else:
        st.warning("Lütfen bir şey yaz!")

# Ekstra bilgi kutusu
st.info("Bu uygulama Streamlit ile çalışıyor. Public link üzerinden erişilebilir.")
