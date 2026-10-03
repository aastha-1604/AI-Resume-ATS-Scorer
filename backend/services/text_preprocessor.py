import spacy


# ---------------------------------------------------------
# LOAD SPACY ENGLISH MODEL
# ---------------------------------------------------------

nlp = spacy.load("en_core_web_sm")


# ---------------------------------------------------------
# CLEAN AND PREPROCESS TEXT
# ---------------------------------------------------------

def preprocess_text(text: str) -> str:
    """
    Clean text using spaCy.

    Steps:
    1. Convert text to lowercase
    2. Tokenize text
    3. Remove stopwords
    4. Remove punctuation
    5. Remove spaces
    6. Lemmatize words
    """

    doc = nlp(text.lower())

    cleaned_tokens = []

    for token in doc:

        # Ignore stopwords like:
        # the, is, a, an, and, etc.

        if token.is_stop:
            continue

        # Ignore punctuation

        if token.is_punct:
            continue

        # Ignore spaces

        if token.is_space:
            continue

        # Store lemmatized word

        cleaned_tokens.append(
            token.lemma_
        )

    cleaned_text = " ".join(
        cleaned_tokens
    )

    return cleaned_text


# ---------------------------------------------------------
# TEST CODE
# ---------------------------------------------------------

if __name__ == "__main__":

    job_description = """
    We are looking for a Data Analyst who has strong
    experience in Python, SQL, Excel and Power BI.

    The candidate should be able to build dashboards,
    analyze large datasets and perform statistical analysis.
    """

    processed_text = preprocess_text(
        job_description
    )

    print("\n==============================")
    print("ORIGINAL JOB DESCRIPTION")
    print("==============================\n")

    print(job_description)

    print("\n==============================")
    print("PROCESSED JOB DESCRIPTION")
    print("==============================\n")

    print(processed_text)