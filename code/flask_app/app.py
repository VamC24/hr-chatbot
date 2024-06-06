from flask import Flask, render_template, request, jsonify
import requests
from typing import Optional
import sys


BASE_API_URL = "http://127.0.0.1:7860/api/v1/run"
FLOW_ID = "b07f4cdd-3fa7-4020-8974-e6884065f68e"


# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
    "ChatInput-AVrOA": {
      "input_value": "hi",
      "return_record": False,
      "sender": "User",
      "sender_name": ""
    },
    "Prompt-A0E27": {
      "template": "Kindly provide a response to the user's inquiry, adhering to the provided context and message history. Please ensure the following rules are followed:\n\nAvoid repetition of information already stated in the context or message history.\nMaintain clarity and conciseness in your response.\nEnsure relevance to the user's question.\n\nContext: {context}\n\nMessage History:\n{history}\n\nUser's Question: {question}",
      "context": "",
      "history": "",
      "question": ""
    },
    "TextInput-NaBKt": {
      "input_value": "HR",
      "record_template": ""
    },
    "MemoryComponent-2RYZd": {
      "n_messages": 5,
      "order": "Descending",
      "record_template": "{sender_name}: {text}",
      "sender": "Machine and User"
    },
    "ChatOutput-MfaXc": {
      "record_template": "{text}",
      "return_record": False,
      "sender": "Machine",
      "sender_name": "AI"
    },
    "Chroma-sdzww": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow"
    },
    "SplitText-VxmnQ": {
      "chunk_overlap": 200,
      "chunk_size": 1000,
      "recursive": False,
      "separators": [
        " ,"
      ]
    },
    "ChromaSearch-w70R4": {
      "chroma_server_ssl_enabled": False,
      "collection_name": "langflow",
      "number_of_results": 4,
      "search_type": "Similarity"
    },
    "File-ipfax": {
      "path": "C:/Users/vabhukya/Documents/vs_workspace/chatbot_app/candidates_data.csv",
      "silent_errors": False
    },
    "OpenAIEmbeddings-iLas5": {
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
      "openai_api_key": "sk-proj-gJR19mQ6bXqdGuFyrRU1T3BlbkFJHxajHSxzzgqZQMNBiHZX",
      "show_progress_bar": False,
      "skip_empty": False,
      "tiktoken_enable": True
    },
    "OpenAIModel-jTIa5": {
      "max_tokens": 256,
      "model_kwargs": "{}",
      "model_name": "gpt-4o",
      "openai_api_key": "sk-proj-gJR19mQ6bXqdGuFyrRU1T3BlbkFJHxajHSxzzgqZQMNBiHZX",
      "stream": False,
      "temperature": 0
    }
  }



app = Flask(__name__)

@app.route('/process_user_message', methods=['POST'])
def process_user_message(
    output_type: str = "chat",
    input_type: str = "chat",
    api_key: Optional[str] = None) -> dict:
      """
      Run a flow with a given message and optional tweaks.

      :param message: The message to send to the flow
      :param flow_id: The ID of the flow to run
      :param tweaks: Optional tweaks to customize the flow
      :return: The JSON response from the flow
      """
      print("inside process message")
      flow_id=FLOW_ID
      tweaks=TWEAKS
      #message = "what is the capital of telangana?"
      # Get the JSON data from the request
      data = request.get_json()

        # Extract the user message (assuming the key is "message")
      message = data.get("message")
      print("user message: ", message)
      
      api_url = f"{BASE_API_URL}/{flow_id}"
      
      payload = {
          "input_value": message,
          "output_type": output_type,
          "input_type": input_type,
      }
      print("payload: ", payload)
      headers = None
      if tweaks:
          payload["tweaks"] = tweaks
      if api_key:
          headers = {"x-api-key": api_key}
      try:
        print("------------question sent to llm and waiting.... ")
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        json_data = response.json()
        #print("json response from model: ", json_data)
        result = json_data["outputs"][0]["outputs"][0]["results"]["result"]
        #print("result: ", result)
      except requests.RequestException as e:
        # Handle exceptions (e.g., network errors, invalid API responses)
        print(f"Exception occured while getting response from openai Exception: {e}")
        return jsonify({"error": "No Response from llm. Please Check"}), 500  # Return an appropriate value or raise a custom exception
      json_result = jsonify({"result": result})
      #print("data type pf retunr value: ", type(json_result))
      return json_result



@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
