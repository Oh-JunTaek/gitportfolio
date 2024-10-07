from retriever.bm25_retriever import BM25Retriever
from retriever.faiss_retriever import FAISSRetriever

class EnsembleRetriever:
    def __init__(self):
        self.bm25_retriever = BM25Retriever()
        self.faiss_retriever = FAISSRetriever()

    def retrieve(self, query, top_k=5):
        bm25_results = self.bm25_retriever.retrieve(query, top_k)
        faiss_results = self.faiss_retriever.retrieve(query, top_k)
        
        # 앙상블: BM25와 FAISS 결과를 합치거나 가중치를 줄 수 있음
        combined_results = self._combine_results(bm25_results, faiss_results)
        return combined_results

    def _combine_results(self, bm25_results, faiss_results):
        # 간단한 방법으로는 점수를 평균내거나, 순위에 따라 가중치를 부여
        # 또는 더 복잡한 앙상블 방법 적용 가능
        return (bm25_results + faiss_results)[:5]  # 단순 예시