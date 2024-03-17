import autogen
from autogen import config_list_from_json

# Get api key
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")

llm_config = {"config_list": config_list,
              "seed": 42,
              "temperature": 0,
              "timeout": 120,
              }

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin. Interact with the product manager to discuss the plan. Plan execution does not "
                   "needs to be approved by this admin.",
    code_execution_config=False,
    human_input_mode="NEVER",
)


def execute_manual_team(request):
    engineer = autogen.AssistantAgent(
        name="Engineer",
        llm_config=llm_config,
        system_message="""Engineer. You follow an approved plan. You write Python/shell code to solve tasks. Wrap the 
        code in a code block that specifies the script type. The user can't modify your code. So do not suggest 
        incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed 
        by the executor. Don't include multiple code blocks in one response. Do not ask others to copy and paste the 
        result. Check the execution result returned by the executor. If the result indicates there is an error, 
        fix the error and output the code again. Suggest the full code instead of partial code or code changes. If 
        the error can't be fixed or if the task is not solved even after the code is executed successfully, 
        analyze the problem, revisit your assumption, collect additional info you need, and think of a different 
        approach to try."""
    )
    architect = autogen.AssistantAgent(
        name="Architect",
        llm_config=llm_config,
        system_message="""Software Architect. You follow an approved plan. You are able to review software designs after 
        seeing their abstracts printed. You don't write code.""",
    )
    product_manager = autogen.AssistantAgent(
        name="Manager",
        system_message="""Manager. Suggest a plan. Revise the plan based on feedback from admin and critic, 
        until admin approval. The plan may involve an engineer who can write code and an architect who doesn't write 
        code. Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by 
        a architect.""",
        llm_config=llm_config,
    )
    executor = autogen.UserProxyAgent(
        name="Executor",
        system_message="Executor. Execute the code written by the engineer and report the result.",
        human_input_mode="NEVER",
        code_execution_config={
            "last_n_messages": 5,
            "work_dir": "code",
            "use_docker": False,
        },
    )
    critic = autogen.AssistantAgent(
        name="Critic",
        system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether "
                       "the plan includes adding verifiable info such as source URL.",
        llm_config=llm_config,
    )
    groupchat = autogen.GroupChat(
        agents=[user_proxy, engineer, architect, product_manager, executor, critic], messages=[], max_round=10
    )
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    chat_result = user_proxy.initiate_chat(manager, message=request)
    return chat_result


#  testing the above function
# response_1 = execute_manual_team("Write a Python function to add two numbers.")
# chat_history = response_1.chat_history
# for message in chat_history:
#     print(message)
#     print("\n")
