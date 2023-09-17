import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Define predefined rules and responses
rules = {
    "hello": "Hello! Welcome, I'm your programming chatbot. How can I assist you today?",
    "hi": "Hello! Welcome, I'm your programming chatbot. How can I assist you today?",
    "hey": "Hello! Welcome, I'm your programming chatbot. How can I assist you today?",
    "how": "I'm just a computer program, so I don't have feelings, but I'm here to help you with any questions or tasks you have. How can I assist you today?",
    "you": "I am Py-chatbot, I'll help you in providing AI information. You can ask me questions and I'll do my best to provide helpful responses. How can I assist you today?",
    "programming": "Programming is the process of creating computer programs or software by writing a series of instructions that a computer can understand and execute. These instructions are typically written in a programming language, which serves as a medium for humans to communicate with computers",
    "ai": "AI, or Artificial Intelligence, refers to the development of computer systems and software that can perform tasks that typically require human intelligence. These tasks include reasoning, problem-solving, learning, perception, language understanding, and decision-making.",
    "machine": "Machine learning is a subset of artificial intelligence (AI) that focuses on developing algorithms and models that enable computers to learn from and make predictions or decisions based on data. ",
    "nlp": "NLP, or Natural Language Processing, is a subfield of artificial intelligence (AI) that focuses on the interaction between computers and human language. Its primary goal is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. NLP encompasses a wide range of tasks and applications related to languags. ",
    "language":"AI Languages are Python, R, Java, Julia",
    "python":"Python is the most widely used programming language for AI and machine learning. It offers a vast ecosystem of libraries and frameworks, such as TensorFlow, PyTorch, Keras, scikit-learn, and NLTK (Natural Language Toolkit), which make it easy to implement AI algorithms, conduct data analysis, and work with neural networks.",
    "r": "R is another popular language for statistical analysis and data science. It has a strong community of users and packages like caret and xgboost that are valuable for machine learning and data visualization.",
    "java": "Java is widely used in enterprise-level AI applications and Android app development. Libraries like Deeplearning4j and Weka provide AI capabilities for Java developers.",
    "julia": "Julia is a relatively new programming language designed for scientific and numerical computing. It is known for its high-performance capabilities and is gaining popularity in the AI and machine learning community.",
    "world" :"Healthcare: AI aids in medical diagnosis, accelerates drug discovery, and offers personalized treatment recommendations. \n\n Finance: AI powers algorithmic trading, assesses credit risk, and detects fraudulent transactions in the financial industry. \n\n Retail: AI enables personalized recommendations, optimizes inventory management, and enhances customer service through chatbots. \n\n Agriculture: AI supports precision farming, livestock monitoring, and smart agricultural practices.\n\n Energy: AI optimizes energy distribution in smart grids and predicts energy consumption patterns. \n\n Entertainment: AI recommends content, generates art and music, and creates deepfake videos. \n\n Education: AI personalizes learning experiences and automates grading in educational settings.",
    "replace" :"AI has the potential to automate specific tasks and roles, leading to changes in the job market. However, the extent to which it replaces human jobs depends on various factors, including the nature of the work, industry, and the ability of society and individuals to adapt to these changes. Many experts argue that AI will transform the job market rather than eliminate it entirely, with humans working alongside AI systems in new and evolving roles. The impact of AI on jobs is a complex and ongoing area of study and debate.",
    "frameworks": "Popular AI frameworks and tools for developers include TensorFlow and PyTorch for deep learning, scikit-learn for traditional machine learning, OpenCV for computer vision, and NLTK and spaCy for natural language processing. These tools offer a range of capabilities, from building and training neural networks to data preprocessing and analysis. Additionally, libraries like XGBoost and fast.ai excel in specific machine learning tasks, while cloud-based platforms such as Microsoft Azure ML, IBM Watson, and Google Cloud AI Platform provide scalable AI solutions.",
    "neural": "Neural networks, a fundamental concept in artificial intelligence, are computational models inspired by the structure and functioning of the human brain. They are used for various tasks, including pattern recognition, classification, regression, and decision-making.",
    "chatbot": "Chatbots are computer programs designed to engage in natural language conversations with humans, typically through text or voice interactions. They use artificial intelligence (AI) technologies to understand user inputs, generate responses, and provide assistance or information. ",
    "gaming": "AI in gaming brings realistic NPCs, procedural content generation, adaptive difficulty, immersive storytelling, and efficient testing. It enhances enemy AI, graphics, moderation, and personalization, shaping modern gaming for deeper player experiences.",
    "bias": "AI bias refers to unfair or discriminatory outcomes in artificial intelligence systems caused by biased training data or algorithm design. It can result in unjust treatment of certain groups, reinforcing stereotypes, and ethical concerns, necessitating strategies like diverse data collection, fairness-aware algorithms, and transparency to mitigate its impact.",
    "security": "AI introduces security concerns such as vulnerability to adversarial attacks where malicious inputs manipulate AI systems, privacy risks due to data exposure, and the potential for AI-powered cyberattacks that exploit machine learning for malicious purposes, necessitating robust defenses and responsible AI development.",
    "impact": "AI has revolutionized NLP by enabling machines to understand, generate, and process human language more effectively. Techniques like deep learning and transformer models have led to significant advancements in tasks such as machine translation, sentiment analysis, chatbots, and speech recognition, making NLP applications more accurate and versatile.",
    "difference": "AI is the overarching field that aims to create intelligent systems. Machine Learning (ML) is a subset of AI that focuses on teaching computers to learn patterns from data, while Deep Learning (DL) is a specialized form of ML that utilizes deep neural networks to extract complex features from data, especially in tasks like image and speech recognition.",
    "data": "AI and data science are interconnected disciplines; data science provides the data and insights AI needs, while AI automates analysis and enhances data-driven decision-making, fostering innovation across industries.",
    "bye": "Goodbye! Have a great day!",
}
def chatbot_response(input_text):
    doc = nlp(input_text.lower())
    response = "I'm sorry, I don't understand. How can I assist you?"
    for token in doc:
        if token.text in rules:
            response = rules[token.text]
            break

    return response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Py-chatbot:", response)
