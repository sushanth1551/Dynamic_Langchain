from langchain_core.prompts import PromptTemplate

def get_prompt():
    template = """
    You are a helpful AI assistant.

    User asked: {topic}

    Respond clearly based on {difficulty} level.
    Keep it simple and structured.
    """

    return PromptTemplate.from_template(template)