from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss

def vectorize_texts(texts):
    """텍스트를 벡터화하고 FAISS 인덱스를 생성"""
    
    # BM25 벡터화
    tokenized_corpus = [doc.split() for doc in texts]
    bm25 = BM25Okapi(tokenized_corpus)
    
    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_vectors = vectorizer.fit_transform(texts).toarray()
    
    # FAISS 인덱스 생성
    d = tfidf_vectors.shape[1]
    index = faiss.IndexFlatL2(d)
    index.add(tfidf_vectors)
    
    return bm25, index, vectorizer
