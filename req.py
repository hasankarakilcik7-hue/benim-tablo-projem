import requests
import streamlit as st
import pandas as pd
import json

st.title("🌐 Web Tablosu")
url_1='https://jsonplaceholder.typicode.com/users'

    

result=requests.get(url_1)
result=result.json()

with open("yazı.json", "r", encoding="utf-8") as f:
  okunan_veri = json.load(f)

List=[]

for i in okunan_veri:
    List.append({
        "id":i["id"],
        "name":i["name"],
        "email":i["email"],
        "phone":i["phone"],
        "address":i["address"]["city"],
        "username":i["username"]
                 })

df=pd.DataFrame(List)
st.dataframe(df,use_container_width=True)
    

