from core.loader import load_csv
from core.profiler import profile_df
from core.llm import groq_chat


def qna(path: str, question: str):
    df = load_csv(path)

    prompt = f"""
    The user has asked a question about this dataframe:
    Schema: {df.dtypes.to_dict()}
    Question: {question}
    Respond ONLY with Python pandas code to compute the answer.
    """

    code = groq_chat(prompt)
    try:
        result = eval(code)  # sandbox later for safety!
    except Exception as e:
        result = str(e)

    return {"code": code, "result": result}
