import requests
import streamlit as st
import pandas as pd

st.title("🌐 Canlı Döviz Kuru")

bozdulurucak_para=st.selectbox("Bozdurulucak Para Birimi",["USD", "EUR", "TRY", "GBP"])
alınacak_para=st.selectbox("alınacak Para Birimi",["TRY", "EUR","USD" ,"GBP"])

miktar=st.number_input("Miktar:",min_value=1.0,value=100.0)

if st.button("Kuru Hesapla"):
    try:
        api_url=f" https://v6.exchangerate-api.com/v6/e3593749b274faf227a895e3/latest/{bozdulurucak_para}"
        response=requests.get(api_url)
        result=response.json()

        if response.status_code==200:
            conversion_rates=result[conversion_rates][alınacak_para]
            yeni_miktar=miktar*conversion_rates

            st.success(f"{miktar} {bozdulurucak_para} = {yeni_miktar:.2f} {alınacak_para}")

            rates = result["conversion_rates"]
            df = pd.DataFrame(list(rates.items()), columns=["Para Birimi", "Kur"])
            st.subheader("Tüm Kurlar Tablosu")
            st.dataframe(df, use_container_width=True)

        else:
            st.error("API'den veri çekilirken bir hata oluştu.")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")

         