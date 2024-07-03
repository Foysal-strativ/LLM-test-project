from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


def get_ai_data(text):
    lm = ChatGoogleGenerativeAI(model="gemini-pro")

    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": text,
            }, 
        ]
    )
    response = lm.invoke([message])
    return response.content

