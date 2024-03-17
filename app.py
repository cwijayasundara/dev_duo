import streamlit as st
from manual_team import execute_manual_team
from auto_team import execute_auto_team
from lang_graph_generator import execute
from star_coder_code_gen import execute_star_coder_2

st.title("DevDuo : Your Coding Assistant Team!")

st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 400px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image("images/dev-duo.webp")
    add_radio = st.radio(
        "evaluation of the code generator:",
        ("introduction",
         "generic-code-generator-manual",
         "autogen-manual",
         "autogen-auto",
         "autogen-agent-builder",
         "langgraph",
         "star-coder-2: local")
    )
if add_radio == "introduction":
    tab1, tab2, tab3 = st.tabs(["comparison", "frameworks", "cost-benefits"])
    with tab1:
        st.write("@karpathy")
        st.write("https://twitter.com/karpathy/status/1767598414945292695")
        col1, col2 = st.columns(2)
        with col1:
            st.header("self driving")
            st.image("images/self_driving.png")
        with col2:
            st.header("code generation")
            st.image("images/code_gen.png")
    with tab2:
        st.header("AlphaCodium")
        st.image("images/alpha_codium.png")
        st.write("https://arxiv.org/pdf/2401.08500.pdf?ref=blog.langchain.dev")
        col1, col2 = st.columns(2)
        with col1:
            st.header("Autogen")
            st.image("images/autogen.png")
            st.write("https://microsoft.github.io/autogen/")
        with col2:
            st.header("Devin")
            st.image("images/devin.png")
            st.write("https://twitter.com/cognition_labs/status/1767548763134964000")

    with tab3:
        st.write("Large Language Models and The End of Programming - CS50 Tech Talk with Dr. Matt Welsh")
        st.write("https://www.youtube.com/watch?v=JhCl-GeT4jw&t=7s")
        # extract the cost benefits from the talk
        st.write("under development")

elif add_radio == "generic-code-generator-manual":
    st.write("Please visit the following link to access the generic code generator")
    st.write("http://localhost:8001/")

elif add_radio == "autogen-manual":
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
    coding_task = st.text_input("Enter the coding task!")
    submit = st.button("submit", type="primary")
    if coding_task and submit:
        coding_task_dict = {"question": coding_task}
        result = execute(coding_task_dict)
        st.write(result)

elif add_radio == "star-coder-2: local":
    coding_task = st.text_input("Enter the coding task!")
    submit = st.button("submit", type="primary")
    if coding_task and submit:
        result = execute_star_coder_2(coding_task)
        st.write(result)
