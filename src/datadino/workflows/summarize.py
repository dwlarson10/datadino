from core.loader import load_csv
from core.profiler import profile_df
from core.llm import groq_chat

def summarize(path: str):
    df = load_csv(path)
    profile = profile_df(df)

    prompt = f"""
    You are a data analyst. Summarize the dataset below in plain English:

    Profile:
    {profile}
    """

    summary = groq_chat(prompt)
    return {"summary": summary, "profile": profile}
