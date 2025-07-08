import spacy
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords

nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")
stop_words = stopwords.words('english')

vectorizer = CountVectorizer(stop_words=stop_words)
lda = LatentDirichletAllocation(n_components=1, random_state=42)

def get_metadata_for_chunk(chunk):
    doc = nlp(chunk)

    # Extract entities as a comma-separated string
    entities = [f"{ent.text} ({ent.label_})" for ent in doc.ents]
    entities_str = ", ".join(entities)

    # Clean text
    clean_text = doc.text.lower()

    # Topic modeling
    stop_words = stopwords.words('english')
    vectorizer = CountVectorizer(stop_words=stop_words)
    doc_term_matrix = vectorizer.fit_transform([clean_text])
    lda = LatentDirichletAllocation(n_components=1, random_state=42)
    lda.fit(doc_term_matrix)

    feature_names = vectorizer.get_feature_names_out()
    top_words = [feature_names[i] for i in lda.components_[0].argsort()[-5:]]
    topics_str = ", ".join(top_words)

    return {
        "entities": entities_str,  # ✅ string
        "topics": topics_str       # ✅ string
    }


    

