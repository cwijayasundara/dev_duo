import streamlit as st
from manual_team import execute_manual_team
from auto_team import execute_auto_team

st.title("DevDuo : Your Coding Assistant Team!")

with st.sidebar:
    add_radio = st.radio(
        "choose the virtual team mode !",
        ("autogen-manual",
         "autogen-auto",
         "autogen-agent-builder",
         "langgraph")
    )

st.write("You have chosen", add_radio)

if add_radio == "autogen-manual":
    request = st.text_area("How can we help you today?:", height=100)
    submit = st.button("submit", type="primary")
    if request and submit:
        chat_result = execute_manual_team(request)
        chat_history = chat_result.chat_history
        for message in chat_history:
            st.write(message)
elif add_radio == "autogen-auto":
    scenario_list = [
        "Generate some agents to analyse latest stock price performance  from Yahoo finance and recommend if "
        "a given stock is a buy, sell or a hold",
        "Generate some agents that can find papers on arxiv by programming and analyzing them in specific "
        "domains related to generative ai and deep learning"]
    building_task = st.selectbox("Enter the building task", scenario_list)
    building_task_desc = st.text_input("Enter the task you want the agents to perform")
    submit = st.button("submit", type="primary")
    if building_task and building_task_desc and submit:
        st.write(execute_auto_team(building_task, building_task_desc))
elif add_radio == "autogen-agent-builder":
    st.write("This feature is under development")
elif add_radio == "langgraph":
    st.write("This feature is under development")
