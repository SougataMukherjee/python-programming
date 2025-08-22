st.button()
   pass
st.success()
checked=st.checkbox()
if checked:
  st.write("")
radio=st.radio("pick one:",["milk","water"])
range=st.slider("level",0,5,2)
pick=st.number_input("how many cups"min_value=1,max_value=10,step=1)
name=st.text_input("enter your name")
if name:
  st.write(f"your {dob}")

date=st.date_input("select your date of birth")
st.write(f"your date of birth {dob}")
st.image("http..",width=200)
with st.expander("text"):
  st.write("""
  1.point 1
  2.point 2
""")
st.markdown('>Blockquote')

