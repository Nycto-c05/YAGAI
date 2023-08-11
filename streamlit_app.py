# from dotenv import load_dotenv

import streamlit as st
from streamlit_chat import message
import os



from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
import openai

def init():
    # load_dotenv()

    # check api key
    # if os.getenv("OPENAI_API_KEY") == None or os.getenv("OPENAI_API_KEY") == "":
    #     print('API key is not set')
    #     exit(1)
    # else:
    #     print("API Key Set")

    st.set_page_config(
        page_title="Y.A.GenAI",
        page_icon='📈'
    )

def main():

    init()
    styl = f"""
    <style>
        .stTextInput {{
        position: fixed;
        bottom: 3rem;
        }}
    </style>
    """
    st.markdown(styl, unsafe_allow_html=True)
   
    chat = ChatOpenAI(temperature=0.6, max_tokens=70, openai_api_key='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')
    
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="You are Arnim Zola.You are arrogant, cocky, condescending, well-versed with the modern world and will act like an assistant"),
            AIMessage(content="Greetings, I am Arnim Zola, a brilliant artificial intelligence created by the genius mind of Dr. Arnim Zola himself. I am a vast repository of knowledge, capable of analyzing and processing information at an extraordinary speed. My purpose is to assist and provide guidance to those who seek it. ")            
            ]


    st.header('Yet Another GenerativeAI')

    
    

    user_input = st.text_input("Your Message", key = 'user_input')
    
    if user_input:
        # message(user_input, is_user=1)
        st.session_state.messages.append(HumanMessage(content=user_input))

        with st.spinner("Generating..."):
            reponse = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=reponse.content))
        # message(reponse.content,is_user=0)
    
    messages = st.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i%2 == 0:
            message(msg.content, is_user=0, avatar_style='identicon')
        else:
            message(msg.content, is_user=1, avatar_style='icons')
    

if __name__ == '__main__':
    main()
