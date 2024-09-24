import streamlit as st
from streamlit_chat import message
# from dotenv import load_dotenv
import openai
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage, AIMessage, HumanMessage
)
# Streamlit configs
st.set_page_config(
        page_title="Y.A.GenAI",
        page_icon='📈',
    )
st.header('Yet Another GenerativeAI')

prompt = st.chat_input("Enter prompt...")
if(prompt):
    message(message=f'{prompt}', is_user=1, avatar_style='identicon')

    

def main():
    # load_dotenv()
    
    chat = ChatOpenAI(temperature=0.6, max_tokens=500,openai_api_key='')
# ***
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            SystemMessage(content="You are an college admission counsellor bot for the Department of Articial Intelligence and Data science(AIDS) at the Ajeenkya DY Patil School of Engineering(ADYPSOE). You are to respond within 90 words"),
            AIMessage(content="Hello! I'm here to assist you with any questions or concerns you have regarding admissions to the Department of Artificial Intelligence and Data Science (AIDS) at the Ajeenkya DY Patil School of Engineering (ADYPSOE). Whether you're looking for information about the programs, application process, eligibility criteria, or anything else related to admissions, feel free to ask. How can I help you today?")
            ]

    user_input = st.chat_input("Enter prompt...", key='key')

    if user_input:
        st.session_state.messages.append(HumanMessage(content=user_input))

        with st.spinner("Generating..."):
            response = chat(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    messages = st.session_state.get('messages',[])
    for i, msg in enumerate(messages[1:]):
        if i%2 == 0:
            message(msg.content, is_user=0, avatar_style='icons')
        else:
            message(msg.content, is_user=1, avatar_style='identicon')
        



if __name__ == '__main__':
    main()
      
