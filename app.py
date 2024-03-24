import streamlit as st
from manual_team import execute_manual_team
from auto_team import execute_auto_team
from lang_graph_generator import execute
from mixtral_code_gen import execute_mixtral
from autobuild_agent_lib import execute_agent_system
from kb_reader import reader
from openai_agents import execute_openai_assistant

st.title("DevDuo : Your Code Assistant Team!")

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
        ("overview",
         "generic-code-generator: manual",
         "openai-assistants",
         "autogen: manual",
         "autogen: agent-library",
         "autogen: agent-builder",
         "alpha_codium : langgraph",
         "mixtral-8x7b: local",
         "about devduo")
    )
if add_radio == "overview":
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
            st.header("Microsoft AutoDev")
            st.image("images/auto_dev.png")
            st.write("https://arxiv.org/html/2403.08299v1")
        with col2:
            st.header("Devin")
            st.image("images/devin.png")
            st.write("https://twitter.com/cognition_labs/status/1767548763134964000")
    with tab3:
        st.write("Large Language Models and The End of Programming - CS50 Tech Talk with Dr. Matt Welsh")
        st.write("https://www.youtube.com/watch?v=JhCl-GeT4jw&t=7s")
        st.write("From the persisted Youtube transcript & RAG !")
        st.write("query : Whats the cost benefit analysis of auto code generation?")
        query = "Whats the cost benefit analysis of auto code generation?"
        st.write(reader(query))

elif add_radio == "generic-code-generator: manual":
    st.subheader("Code Generator : Manual")
    st.image("images/coding_assistant.webp", width=400)
    st.write("Please visit the following link to access the generic code generator")
    st.write("http://localhost:8501/")

elif add_radio == "openai-assistants":
    st.subheader("OpenAI Assistants")
    st.image("images/openai_assistants_image.png", use_column_width=True)
    request = st.text_input("Enter the coding request!")
    submit = st.button("submit", type="primary")
    if request and submit:
        messages = execute_openai_assistant(request)
        for message in messages:
            st.write(f"{message.role}: {message.content[0].text.value}")

elif add_radio == "autogen: manual":
    st.subheader("AutoGen : Manual Builder")
    st.image("images/ms_autogen_1.webp", use_column_width=True)
    scenario_list = [
        "Generate a deep neural network using TF/Keras to analyse the Heart Disease Cleveland dataset and predict if "
        "a person has heart disease or not", "Generate a microservice to manage Trades in a stock trading system", ]
    manual_mode = st.checkbox("Manual Mode")
    if manual_mode:
        coding_task_manual = st.text_input("Enter the task you want the code generator to perform!")
        submit = st.button("submit", type="primary")
        if coding_task_manual and submit:
            chat_result = execute_manual_team(coding_task_manual)
            chat_history = chat_result.chat_history
            for message in chat_history:
                st.write(message)
    else:
        coding_task = st.selectbox("Select the code generation task !", scenario_list)
        submit = st.button("submit", type="primary")
        if coding_task and submit:
            chat_result = execute_manual_team(coding_task)
            chat_history = chat_result.chat_history
            for message in chat_history:
                st.write(message)

elif add_radio == "autogen: agent-builder":
    st.subheader("AutoGen : Agent Builder")
    st.image("images/autogen_autobuild.png", use_column_width=True)
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

elif add_radio == "autogen: agent-library":
    st.subheader("AutoGen : Agent Library")
    st.image("images/autogen_agent_lib.webp", width=400)
    scenario_list = [
        "Generate some agents to analyse latest stock price performance  from Yahoo finance and recommend if "
        "a given stock is a buy, sell or a hold",
        "Generate some agents that can find papers on arxiv by programming and analyzing them in specific "
        "domains related to generative ai and deep learning"]
    building_task = st.selectbox("Enter the building task", scenario_list)
    building_task_desc = st.text_input("Enter the task you want the agents to perform")
    submit = st.button("submit", type="primary")
    if building_task and building_task_desc and submit:
        st.write(execute_agent_system(building_task, building_task_desc))

elif add_radio == "alpha_codium : langgraph":
    st.subheader("LangGraph : Alpha Codium")
    st.image("images/alpha_codium.png", use_column_width=True)
    coding_task = st.text_input("Enter the coding task!")
    st.write("e.g. Generate LangGraph code to download stock price data from Yahoo finance for the past 5 years and "
             "plot the stock price performance for the largest tech companies!")
    submit = st.button("submit", type="primary")
    if coding_task and submit:
        coding_task_dict = {"question": coding_task}
        result = execute(coding_task_dict)
        st.write(result)

elif add_radio == "mixtral-8x7b: local":
    st.subheader("Mixtrail - 8x7B : Local Code Generator")
    st.image("images/mixtral.png", width=400)
    scenario_list = [
        "Create a fully functional DNN using Tensorflow and Keras to analyse the MNIST dataset.",
        "Create a microservice to manage trades in a stock trading system."]
    manual_mode = st.checkbox("Manual Mode")
    if manual_mode:
        building_task_desc = st.text_input("Enter the task you want the code generator to perform!")
        submit = st.button("submit", type="primary")
        if building_task_desc and submit:
            st.write(execute_mixtral(building_task_desc))
    else:
        building_task = st.selectbox("Enter the building task", scenario_list)
        submit = st.button("submit", type="primary")
        if building_task and submit:
            st.write(execute_mixtral(building_task))

elif add_radio == "about devduo":
    st.markdown(''' :green[The hottest new programming language is English !]''', unsafe_allow_html=True)
    st.write("@karpathy")
    st.write("https://twitter.com/karpathy/status/1617979122625712128")
    st.write("Generative AI-based code generators like AutoGen are revolutionizing software engineering by enabling "
             "rapid development of AI-driven applications through multi-agent conversations and enhanced LLM "
             "inference. These platforms democratize access to AI, allowing for sophisticated solutions without deep "
             "data science expertise. The future of software engineering with these technologies promises greater "
             "efficiency, innovation, and a blend of human creativity with computational power, fundamentally "
             "transforming how software is developed and deployed.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("generic-code-generator: manual")
        st.write("openai-assistants")
        st.write("autogen: manual")
    with col2:
        st.write("autopen: agent-library")
        st.write("autogen: agent-builder")
    with col3:
        st.write("alpha_codium : langgraph")
        st.write("mixtral-8x7b: local")