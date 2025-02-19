from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load Hugging Face Model
llm = HuggingFacePipeline.from_model_id("google/gemma-7b", task="text-generation")

# Define AI Prompt
prompt = PromptTemplate(
    input_variables=["stock", "price", "sentiment"],
    template="The stock {stock} is predicted to be priced at ${price:.2f}. "
             "News sentiment indicates {sentiment}. Should I buy, hold, or sell?"
)

# AI-driven investment advice
def get_ai_advice(stock, predicted_price, sentiment):
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(stock=stock, price=predicted_price, sentiment=sentiment)
