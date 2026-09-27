import requests
import streamlit as st
import pandas as pd

st.title("🌐 Web Tablosu")
url_1='https://jsonplaceholder.typicode.com/users'

result=requests.get(url_1)
result=result.json()
List=[]

for i in result:
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
    

