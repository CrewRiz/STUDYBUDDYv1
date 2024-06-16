# Study Buddy

Study Buddy is an interactive learning assistant application that helps students with note-taking and provides personalized tutoring. It leverages OpenAI's powerful language models to offer an engaging and adaptive learning experience.

## Features

- **Dual-Mode Interface**: Choose between Note-Taking and Tutoring modes.
- **Intelligent Note Summarization**: Get concise summaries of your notes to reinforce learning.
- **Interactive Tutoring**: Engage with an AI tutor that adapts to your knowledge level.
- **Document Upload**: Share study materials with the tutor for more contextualized learning.
- **Save and Load**: Easily save your notes or tutoring sessions and load them later.
- **User-Friendly GUI**: A clean and intuitive graphical user interface built with Tkinter.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- OpenAI API key
- PyCharm IDE (recommended for easy setup)

## Installation

1. Clone the repository:
git clone https://github.com/CrewRiz/STUDYBUDDYv1.git
cd STUDYBUDDYv1
Copy
2. Install the required dependencies:
pip install openai
Copy
3. Set up your OpenAI API key as an environment variable. In PyCharm:
- Go to Run -> Edit Configurations
- Click the "+" button and select "Python"
- Name your configuration (e.g., "StudyBuddy")
- In the "Environment variables" section, click on "..."
- Add a new variable with name "OPENAI_API_KEY" and your API key as the value

4. Update the `config.py` file with your OpenAI Assistant IDs:
- Replace `'your_tutor_assistant_id'` with your tutoring assistant's ID
- Replace `'your_notes_assistant_id'` with your note-taking assistant's ID

## Usage

1. Run the `main.py` file in PyCharm or from the command line:
python main.py
Copy
2. In the start menu, choose either "Take Notes" or "Start Tutoring".

3. For note-taking:
- Enter your notes in the input area.
- Click "Submit" to get a summary.
- Use "Save" to store your notes and summary, and "Load" to retrieve previous sessions.

4. For tutoring:
- Enter your questions or topics in the input area.
- Click "Submit" to get responses from the tutor.
- Use "Upload Document" to share study materials with the tutor.
- The tutor will assess your knowledge and provide personalized guidance.

5. In both modes, you can clear the interface, save the output, or return to the main menu at any time.

## Project Structure

- `main.py`: The entry point of the application.
- `gui.py`: Contains the `StudyBuddyApp` class responsible for the graphical user interface.
- `api_client.py`: Handles interactions with the OpenAI API.
- `config.py`: Stores configuration variables and constants.
- `utils.py`: Provides utility functions for file operations.

## Contributing

Contributions to the Study Buddy project are welcome. Please ensure you follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Travi - tcrew5@wgu.edu

Project Link: pending

## Acknowledgements

- [OpenAI](https://openai.com)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Python](https://www.python.org)
