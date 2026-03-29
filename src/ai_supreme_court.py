from __future__ import annotations

from operator import itemgetter

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama


VERDICT_SCHEMA = {
    "title": "court_verdict",
    "type": "object",
    "properties": {
        "verdict": {
            "type": "string",
            "description": "The final decision made by the judge.",
        },
        "reasoning": {
            "type": "string",
            "description": "Why the judge reached that decision.",
        },
    },
    "required": ["verdict", "reasoning"],
}


def normalize_topic(topic: str) -> str:
    return " ".join(topic.split())


def build_court(model_name: str = "llama3.1"):
    llm = ChatOllama(model=model_name)
    judge_llm = llm.with_structured_output(VERDICT_SCHEMA)
    parser = StrOutputParser()

    history = ChatMessageHistory()
    history.add_user_message("My name is Sreehari.")
    history.add_ai_message("Welcome to AI Supreme Court. State your case.")

    pro_prompt = ChatPromptTemplate.from_template(
        "Topic: {topic}. Provide one strong argument FOR this. Keep it brief."
    )
    con_prompt = ChatPromptTemplate.from_template(
        "Topic: {topic}. Provide one strong argument AGAINST this. Keep it brief."
    )

    pro_chain = pro_prompt | llm | parser
    con_chain = con_prompt | llm | parser

    return (
        RunnablePassthrough.assign(history=lambda _: history.messages)
        | RunnablePassthrough.assign(topic=lambda x: normalize_topic(x["topic"]))
        | RunnablePassthrough.assign(pro_argument=pro_chain, con_argument=con_chain)
        | {
            "verdict_data": ChatPromptTemplate.from_messages(
                [
                    ("system", "You are a judge. Consider the conversation history: {history}"),
                    (
                        "human",
                        "Topic: {topic}\n"
                        "Argument for: {pro_argument}\n"
                        "Argument against: {con_argument}\n"
                        "Give a final verdict with reasoning.",
                    ),
                ]
            )
            | judge_llm,
            "topic": itemgetter("topic"),
            "pro_argument": itemgetter("pro_argument"),
            "con_argument": itemgetter("con_argument"),
        }
    )


def run_case(topic: str, model_name: str = "llama3.1") -> dict:
    court = build_court(model_name=model_name)
    return court.invoke({"topic": topic})
