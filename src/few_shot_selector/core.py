"""核心向量检索逻辑"""

import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any

from .utils import DatabaseNotInitializedError, EmbeddingError, validate_qa_pair


class FewShotSelector:
    """Few-shot 示例选择器"""

    def __init__(self, db_path: str = "./.chroma_db", model_name: str = "all-MiniLM-L6-v2"):
        """初始化选择器

        Args:
            db_path: ChromaDB 数据库路径
            model_name: Sentence Transformer 模型名称
        """
        self.db_path = db_path
        self.model_name = model_name
        self.client = chromadb.PersistentClient(path=db_path)

        try:
            self.model = SentenceTransformer(model_name)
        except Exception as e:
            raise EmbeddingError(f"加载 Embedding 模型失败: {e}")

        self.collection = self.client.get_or_create_collection(
            name="qa_examples",
            metadata={"hnsw:space": "cosine"}
        )

    def initialize_database(self, qa_pairs: List[Dict[str, Any]]) -> None:
        """批量插入 QA 数据"""
        if not qa_pairs:
            raise ValueError("QA 数据不能为空")

        ids = []
        documents = []
        metadatas = []

        for qa in qa_pairs:
            ids.append(str(qa["id"]))
            documents.append(qa["question"])
            metadatas.append({
                "answer": qa["answer"],
                "category": qa.get("category", ""),
                "tags": ",".join(qa.get("tags", []))
            })

        self.collection.add(ids=ids, documents=documents, metadatas=metadatas)

    def search_similar(self, query: str, n_results: int = 3) -> List[Dict[str, Any]]:
        """搜索相似示例"""
        if not query.strip():
            raise ValueError("查询不能为空")

        if self.collection.count() == 0:
            raise DatabaseNotInitializedError("数据库为空,请先初始化")

        results = self.collection.query(
            query_texts=[query],
            n_results=min(n_results, self.collection.count())
        )

        examples = []
        for i in range(len(results["ids"][0])):
            examples.append({
                "id": results["ids"][0][i],
                "question": results["documents"][0][i],
                "answer": results["metadatas"][0][i]["answer"],
                "category": results["metadatas"][0][i]["category"],
                "distance": results["distances"][0][i] if "distances" in results else None
            })

        return examples

    def format_prompt(self, query: str, examples: List[Dict[str, Any]]) -> str:
        """格式化 Prompt"""
        prompt = "以下是一些相关示例:\n\n"

        for i, ex in enumerate(examples, 1):
            prompt += f"示例 {i}:\n"
            prompt += f"问题: {ex['question']}\n"
            prompt += f"答案: {ex['answer']}\n\n"

        prompt += f"现在请回答:{query}"
        return prompt

    def get_stats(self) -> Dict[str, Any]:
        """获取数据库统计信息"""
        count = self.collection.count()

        if count > 0:
            results = self.collection.get()
            categories = {}
            for meta in results["metadatas"]:
                cat = meta.get("category", "未分类")
                categories[cat] = categories.get(cat, 0) + 1
        else:
            categories = {}

        return {"total": count, "categories": categories}

    def add_qa_pair(self, question: str, answer: str, category: str = "", tags: List[str] = None) -> str:
        """添加单个 QA 对"""
        if not validate_qa_pair(question, answer):
            raise ValueError("问题和答案不能为空")

        new_id = str(self.collection.count() + 1)

        self.collection.add(
            ids=[new_id],
            documents=[question],
            metadatas=[{
                "answer": answer,
                "category": category,
                "tags": ",".join(tags or [])
            }]
        )

        return new_id
