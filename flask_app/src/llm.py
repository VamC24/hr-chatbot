from langflow.load import run_flow_from_json
TWEAKS = [
  {
    "ChatInput-KBK8u": {
      "input_value": "Hi",
      "return_record": False,
      "sender": "User",
      "sender_name": ""
    },
    "Prompt-TZ1Eu": {
      "template": "Kindly provide a response to the user's inquiry, adhering to the provided context and message history. Please ensure the following rules are followed:\n\nAvoid repetition of information already stated in the context or message history.\nMaintain clarity and conciseness in your response.\nEnsure relevance to the user's question.\n\nContext: {context}\n\nMessage History:\n{history}\n\nUser's Question: {question}",
      "context": "",
      "history": "",
      "question": ""
    },
    "TextInput-696KC": {
      "input_value": "HR",
      "record_template": ""
    },
    "MemoryComponent-U9AHr": {
      "n_messages": 5,
      "order": "Descending",
      "record_template": "{sender_name}: {text}",
      "sender": "Machine and User"
    },
    "ChatOutput-8Uag1": {
      "record_template": "{text}",
      "return_record": False,
      "sender": "Machine",
      "sender_name": "AI"
    },
    "Chroma-lDP0m": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow"
    },
    "SplitText-bDw0U": {
      "chunk_overlap": 200,
      "chunk_size": 1000,
      "recursive": False,
      "separators": [
        " ,"
      ]
    },
    "ChromaSearch-TR858": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow",
      "number_of_results": 4,
      "search_type": "Similarity"
    },
    "File-IZg7k": {
      "path": "candidates_data.csv",
      "silent_errors": False
    },
    "OpenAIEmbeddings-xVUzi": {
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
      "tiktoken_enable": False
    },
    "OpenAIModel-UilGx": {
      "max_tokens": 256,
      "model_kwargs": "{}",
      "model_name": "gpt-4o",
      "openai_api_key": "sk-proj-Ga6Nzh1Oj63nuMdJJbwYT3BlbkFJwoa8JEZmuWgDYjusrepC",
      "stream": False,
      "temperature": 0
    }
  }
]

result = run_flow_from_json(flow=r"C:/Users/vabhukya/Documents/vs_workspace/chatbot_app/HR_chatbot.json",
                            input_value="message",
                            tweaks=TWEAKS)

print("this is result: ", result)