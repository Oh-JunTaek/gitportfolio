def search(query, bm25, faiss_index, vectorizer, top_n=5):
    """쿼리를 사용해 FAISS 및 BM25 검색"""
    
    # BM25 검색
    tokenized_query = query.split()
    bm25_scores = bm25.get_scores(tokenized_query)
    
    # TF-IDF 쿼리 벡터화
    query_vector = vectorizer.transform([query]).toarray()
    
    # FAISS 검색
    _, faiss_scores = faiss_index.search(query_vector, top_n)
    
    # BM25와 FAISS 점수를 결합한 앙상블
    final_scores = bm25_scores + faiss_scores.flatten()
    top_n_indices = final_scores.argsort()[-top_n:][::-1]
    
    return top_n_indices
