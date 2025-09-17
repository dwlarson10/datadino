def profile_df(df):
    return {
        "n_rows": len(df),
        "n_cols": len(df.columns),
        "columns": {col: str(df[col].dtype) for col in df.columns},
        "missing": df.isnull().sum().to_dict(),
        "summary": df.describe(include="all").to_dict()
    }
