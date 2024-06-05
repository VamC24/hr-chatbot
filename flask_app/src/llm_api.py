import requests
from typing import Optional

BASE_API_URL = "http://127.0.0.1:7860/api/v1/run"
FLOW_ID = "70ea9263-860e-4bb5-b5d4-0b7ec0fce748"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
    "ChatInput-QeU5F": {
      "input_value": "hi",
      "return_record": False,
      "sender": "User",
      "sender_name": ""
    },
    "Prompt-SoD2H": {
      "template": "Kindly provide a response to the user's inquiry, adhering to the provided context and message history. Please ensure the following rules are followed:\n\nAvoid repetition of information already stated in the context or message history.\nMaintain clarity and conciseness in your response.\nEnsure relevance to the user's question.\n\nContext: {context}\n\nMessage History:\n{history}\n\nUser's Question: what is the capital of india?",
      "context": "",
      "history": "",
      "question": "what is the capital of india?"
    },
    "TextInput-VCNwk": {
      "input_value": "HR",
      "record_template": ""
    },
    "MemoryComponent-fa3ud": {
      "n_messages": 5,
      "order": "Descending",
      "record_template": "{sender_name}: {text}",
      "sender": "Machine and User"
    },
    "ChatOutput-eRs9B": {
      "record_template": "{text}",
      "return_record": False,
      "sender": "Machine",
      "sender_name": "AI"
    },
    "Chroma-5nKsy": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow"
    },
    "SplitText-tLIxq": {
      "chunk_overlap": 200,
      "chunk_size": 1000,
      "recursive": False,
      "separators": [
        " ,"
      ]
    },
    "ChromaSearch-agmaS": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow",
      "number_of_results": 4,
      "search_type": "Similarity"
    },
    "File-znA40": {
      "path": "C:/Users/vabhukya/Documents/vs_workspace/chatbot_app/candidates_data.csv",
      "silent_errors": False
    },
    "OpenAIEmbeddings-8Yp8N": {
      "allowed_special": [],
      "chunk_size": 1000,
      "default_query": "{}",
      "deployment": "text-embedding-ada-002",
      "disallowed_special": [
        "all"
      ],
      "embedding_ctx_length": 8191,
      "max_retries": 6,
      "model": "text-embedding-ada-002",
      "model_kwargs": "{}",
      "openai_api_key": "sk-proj-Ga6Nzh1Oj63nuMdJJbwYT3BlbkFJwoa8JEZmuWgDYjusrepC",
      "show_progress_bar": False,
      "skip_empty": False,
      "tiktoken_enable": True
    },
    "OpenAIModel-GzRAA": {
      "max_tokens": 256,
      "model_kwargs": "{}",
      "model_name": "gpt-4o",
      "openai_api_key": "sk-proj-Ga6Nzh1Oj63nuMdJJbwYT3BlbkFJwoa8JEZmuWgDYjusrepC",
      "stream": False,
      "temperature": 0
    }
  }


def run_flow(message: str,
  flow_id: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Setup any tweaks you want to apply to the flow
message = "what is the capital of india"
response_result = run_flow(message=message, flow_id=FLOW_ID, tweaks=TWEAKS)
print("result :  ", response_result["outputs"][0]["outputs"][0]["results"]["result"])