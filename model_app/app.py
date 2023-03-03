import streamlit as st
from predict import predict_nertags

st.title('InKaNER - India 🇮🇳 Ka Named Entity Recognizer')
st.markdown("An XLM-Roberta Model trained to recognize entities in **6 Indian 🇮🇳 Languages**")
st.markdown("Try out the model in **_Hindi, Kannada, Bengali, Marathi, Tamil, and Telugu!_**")

name = st.text_input("Enter Your Statement", "यशराज आज गोरखपुर जाएगा")

if(st.button('Submit')):
    result = name.title()
    ner_res =  predict_nertags(result)
    prompt_list = result.split(' ')
    display = ""
    for i,values in enumerate(zip(prompt_list,ner_res)):
        if values[1]=="":
            display+=values[0]+" "
        else:
            display+= "<span style='background-color: crimson; color: white;'> {0} ({1}) </span>".format(values[0],values[1])
    
    st.markdown(display,unsafe_allow_html=True)

# removing hamburger and streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# adding a footer
footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
opacity:0.75
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://github.com/yashrajOjha" target="_blank">Yash Raj Ojha</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

