import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder

config_file_or_env = "OAI_CONFIG_LIST.json"
llm_config = {"temperature": 0}
config_list = autogen.config_list_from_json(config_file_or_env, filter_dict={"model": ["gpt-4-0125-preview"]})


def start_task(execution_task: str, agent_list: list):
    group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)
    manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={"config_list": config_list, **llm_config})
    agent_list[0].initiate_chat(manager, message=execution_task)


# Step 2: create a AgentBuilder
builder = AgentBuilder(
    config_file_or_env=config_file_or_env,
    builder_model="gpt-4-0125-preview",
    agent_model="gpt-4-0125-preview"
)


def execute_auto_team(request, task_desc):
    agent_list, agent_configs = builder.build(request, llm_config)
    start_task(
        execution_task=task_desc,
        agent_list=agent_list,
    )
    builder.clear_all_agents(recycle_endpoint=True)
