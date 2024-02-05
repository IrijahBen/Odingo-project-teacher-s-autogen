import autogen

# Updated configuration for teaching ideas
teaching_config = [
    {
        'base_url': "http://0.0.0.0:8000",
        'api_key': "NULL",
    }
]

llm_config_teaching = {
    "config_list": teaching_config,
}

# Updated agents for teaching scenario
teacher = autogen.AssistantAgent(
    name="Teacher",
    llm_config=llm_config_teaching,
    system_message="""Teacher. Your role is to develop ideas, explain topics, and create questions for evaluation. Encourage interactive learning.
    """
)

learner = autogen.UserProxyAgent(
    name="Learner",
    system_message="Learner. Ask questions, seek clarification, and engage in discussions to understand the topics presented by the teacher."
)

evaluator = autogen.UserProxyAgent(
    name="Evaluator",
    system_message="Evaluator. Evaluate the learning materials provided by the teacher. Ask questions to assess comprehension and provide feedback."
)

# GroupChat setup for teaching scenario
teaching_groupchat = autogen.GroupChat(agents=[teacher, learner, evaluator], messages=[], max_round=50)
teaching_manager = autogen.GroupChatManager(groupchat=teaching_groupchat, llm_config=llm_config_teaching)

# Teacher initiates the chat with an introduction and a teaching task
teacher.initiate_chat(
    teaching_manager,
    message="""
    Welcome to the learning session! Today, we'll explore the fascinating world of [subject]. 
    I'll provide explanations, share ideas, and create questions for evaluation. Feel free to ask questions and engage in discussions.
    """
)

# Additional tasks for the teacher to demonstrate teaching ideas
teacher.initiate_chat(
    teaching_manager,
    message="""
    Let's delve into the first topic: [Topic]. I'll explain the key concepts and then create a few questions for evaluation.
    """
)

# Create two or three questions for evaluation
question1 = "What is the main concept discussed in [Topic]?"
question2 = "How does [Topic] relate to real-world applications?"
question3 = "Can you provide an example illustrating [specific aspect of Topic]?"

# Print the questions for reference
print("Evaluation Questions:")
print(f"1. {question1}")
print(f"2. {question2}")
print(f"3. {question3}")
