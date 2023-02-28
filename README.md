# Equato - A Chatbot Built using RASA to do Basic Mathematical Operations
This project involves building a chatbot using RASA that can perform basic mathematical operations based on user inputs. The bot will take two operands and an operation as input, and then display the output to the user.

# Supported Mathematical Operations
The Math Operation Chatbot currently supports the following mathematical operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

# Workflow
The following is the proposed workflow for the chatbot:

- The chatbot will prompt the user to input two operands and an operation.
- The chatbot will show the available mathematical operations to the user, using a simple menu-based approach. The available categories will include "addition", "subtraction", "multiplication", and "division".
- Based on the user's input, the chatbot will show the output to the user.
- After the flow ends, if the user requests for "more operations", the chatbot will take the new inputs and proceed.
- The chatbot will also accept the mathematical query as a single sentence.

# Output
# Sample 1: If the user only provides the operator name, the chatbot will request the user to enter two operands separately.
![maths_operation1](https://user-images.githubusercontent.com/113231945/221856812-ae6dbf29-fe95-428e-a095-b0aa6cfe1f64.png)

# Sample 2: This is an updated version of the mathematical operations chatbot, which now allows the user to input their mathematical query as a single sentence (e.g., 'What is the sum of 10 and 20?'). The chatbot will extract the operands and the operator from the user's input and provide the resulting output.
![maths_operation2](https://user-images.githubusercontent.com/113231945/221856492-515a500b-f41b-4dc5-8586-cb5dc15c59a7.png)

# This is a general Conversation between the chatbot and user.
![general_conversation](https://user-images.githubusercontent.com/113231945/221856562-60effd01-74f2-4a8b-85a5-3e5bf1b66f25.png)
