from langchain_huggingface import HuggingFacePipeline
from src.core.config import settings
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


class LLMService:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            settings.MODEL_NAME, token=settings.HUGGINGFACE_TOKEN
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            settings.MODEL_NAME, token=settings.HUGGINGFACE_TOKEN
        )

        self.pipe = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_length=settings.MAX_LENGTH,
        )

        self.llm = HuggingFacePipeline(pipeline=self.pipe)

    def get_llm(self):
        return self.llm
