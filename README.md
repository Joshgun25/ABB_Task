# Bank Chat Application

This is a Django-based chat application for interacting with Bank. It allows users to ask questions and receive answers from the Bank chatbot.

## Running the Application with Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/Joshgun25/ABB_Task.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ABB_Task
    ```
    
3. Set your OpenAI API key:

    Before running the application, you need to set your OpenAI API key as an environment variable named `OPENAI_API_KEY`.
   
5. Build the Docker containers:

    ```bash
    docker-compose build
    ```
    
6. Run the Docker containers:

    ```bash
    docker-compose up
    ```

7. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Usage
- You will be directed to Menu Page as default.
- You can scrape text content from the url which you should provide.
- You can upload custom data file for OpenAI chatbot.
- Navigate to the chat page to interact with the Bank chatbot.
- Type your question in the input field and press "Send" to receive an answer from the chatbot.
- You can also view visualizations, such as word clouds and histograms, by navigating to the appropriate pages.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
