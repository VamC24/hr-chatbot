document.addEventListener("DOMContentLoaded", function () {
    const chatbotToggler = document.querySelector(".chatbot-toggler");
    const closeBtn = document.querySelector(".close-btn");
    const chatbox = document.querySelector(".chatbox");
    const chatInput = document.querySelector("#chatInput");
    const sendChatBtn = document.querySelector("#send-btn");
    const emojiSelector = document.getElementById("emojiSelector");
    const emojiSearch = document.getElementById("emojiSearch");
    const emojiList = document.getElementById("emojiList");

    document.getElementById("smile-icon").addEventListener("click", function (event) {
        // Toggle emoji selector visibility
        emojiSelector.classList.toggle("active");
        event.stopPropagation(); // Prevent the click event from bubbling up to the document
    });

    // Add a click event listener to the document to close the emoji selector when clicking outside of it
    document.addEventListener("click", function (event) {
        // Check if the clicked element is not inside the emoji selector or the smile icon
        if (!emojiSelector.contains(event.target) && event.target.id !== "smile-icon") {
            // Hide the emoji selector
            emojiSelector.classList.remove("active");
        }
    });

    // Fetch emojis and load them
    fetch("https://emoji-api.com/emojis?access_key=42f043dc9a37878a131a1c9609ed7499b70604f7")
        .then((res) => res.json())
        .then((data) => loadEmoji(data))
        .catch((error) => console.error("Error fetching emojis:", error));

    // Function to load emojis
    function loadEmoji(data) {
        emojiList.innerHTML = ""; // Clear emoji list before loading new emojis
        data.forEach((emoji) => {
            let li = document.createElement("li");
            li.textContent = emoji.character; // Display only the emoji character
            li.dataset.name = emoji.unicodeName.toLowerCase(); // Store the emoji name in a data attribute
            li.addEventListener("click", () => {
                // Insert selected emoji into the chat input
                chatInput.value += emoji.character;
            });
            emojiList.appendChild(li);
        });
    }

    // Function to filter emojis based on search input
    function filterEmojis() {
        const searchValue = emojiSearch.value.trim().toLowerCase();
        const emojis = emojiList.querySelectorAll("li");
        emojis.forEach((emoji) => {
            const emojiName = emoji.dataset.name; // Get the emoji name from the data attribute
            // Check if the emoji character or its name includes the search value
            if (emojiName.includes(searchValue)) {
                emoji.style.display = "block";
            } else {
                emoji.style.display = "none";
            }
        });
    }

    emojiSearch.addEventListener("input", filterEmojis);
    emojiSearch.addEventListener("keyup", filterEmojis);

    let userMessage = null; // Variable to store user's message
    const API_KEY = "sk-proj-G6XIDwTZRUwmyOCtdcS9T3BlbkFJHKKgEePvx3Uxw2AHXCcl"; 
    const inputInitHeight = chatInput.scrollHeight;

    const createChatLi = (message, className) => {
        // Create a chat <li> element with passed message and className
        const chatLi = document.createElement("li");
        chatLi.classList.add("chat", `${className}`);
        let chatContent = className === "outgoing" ? `<p></p>` : `<img src="{{ url_for('static', filename='images/robo.jpg') }}" alt="Image"><p></p>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = message;
        return chatLi; // return chat <li> element
    };

    const generateResponse = (chatElement) => {

        //
            
                const { exec } = require("child_process");

                // Execute the Python script
                exec(`python3 C:/Users/vabhukya/Documents/vs_workspace/chatbot_app/llm_api.py "${userMessage}"`,  (error, stdout, stderr) => {
                    if (error) {
                        console.error(`Error executing Python script: ${error.message}`);
                        return;
                    }
                    const result = stdout.trim(); // Remove any trailing newline
                    messageElement.textContent = result
                    console.log(`Python script result: ${result}`);
                    // Use the result in your JavaScript code
                });

        //

       
    };

    const handleChat = () => {
        userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
        if (!userMessage) return;
        // Clear the input textarea and set its height to default
        chatInput.value = "";
        chatInput.style.height = `${inputInitHeight}px`;
        // Append the user's message to the chatbox
        chatbox.appendChild(createChatLi(userMessage, "outgoing"));
        chatbox.scrollTo(0, chatbox.scrollHeight);

        setTimeout(() => {
            // Display "Thinking..." message while waiting for the response
            const incomingChatLi = createChatLi("Typing...", "incoming");
            chatbox.appendChild(incomingChatLi);
            chatbox.scrollTo(0, chatbox.scrollHeight);
            generateResponse(incomingChatLi);
        }, 600);
    };

    chatInput.addEventListener("input", () => {
        // Adjust the height of the input textarea based on its content
        chatInput.style.height = `${inputInitHeight}px`;
        chatInput.style.height = `${chatInput.scrollHeight}px`;
    });

    chatInput.addEventListener("keydown", (e) => {
        // If Enter key is pressed without Shift key and the window
        // width is greater than 800px, handle the chat
        if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
            e.preventDefault();
            handleChat();
        }
    });

    sendChatBtn.addEventListener("click", handleChat);
    closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
    chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));
});