# Speech Recognition and Text-to-Speech Interaction

This project demonstrates basic speech recognition and text-to-speech interaction using the `speech_recognition` and `pyttsx3` libraries in Python.

## Description

The code allows for voice input through a microphone, recognizes speech using Google's speech recognition service, and provides corresponding text-to-speech responses.

The main functionalities of the code include:

- Listening for voice input and capturing audio using the `Recognizer` class from `speech_recognition`.
- Recognizing speech using Google's speech recognition service.
- Converting text to speech using the `pyttsx3` library.
- Responding with appropriate text-to-speech messages based on the recognized query.

## Requirements

- Python 3.x
- `speech_recognition` library (`pip install SpeechRecognition`)
- `pyttsx3` library (`pip install pyttsx3`)

## Usage

1. Make sure you have the required libraries installed by running the respective installation commands mentioned above.

2. Run the Python script `main.py`.

3. The program will start listening for voice input. Say "hello" to receive a greeting and "goodbye" to end the program. For any other queries, the program will respond with a message indicating that it didn't understand and ask for repetition.

## Additional Notes

- Adjust the microphone volume and ambient noise using the `adjust_for_ambient_noise()` method in the `listen()` function to improve speech recognition accuracy.
- Customize the responses by modifying the conditions and corresponding messages in the main loop.
- Feel free to expand the code and add more functionality based on your requirements.

## License

This project is licensed under the [MIT License](LICENSE).
