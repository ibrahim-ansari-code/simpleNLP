import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nlp import NLP


def loadFile(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return ""


if __name__ == "__main__":
    # You can change this path to point to your own text file
    path = "/Users/shehryar.ansari/PycharmProjects/CS/notes.txt"

    # Try to load file, if it doesn't exist use default text
    text = loadFile(path)
    if text == "":
        text = """
        Photosynthesis is a biochemical process through which plants, algae, and some bacteria convert light energy into chemical energy. It primarily occurs in the chloroplasts of plant cells, where a green pigment called chlorophyll captures light energy from the sun. This energy is then used to convert carbon dioxide from the air and water from the soil into glucose, a type of sugar that plants use as food.

        The general equation for photosynthesis is: 6CO₂ + 6H₂O + sunlight → C₆H₁₂O₆ + 6O₂. This means that six molecules of carbon dioxide and six molecules of water, using sunlight, produce one molecule of glucose and six molecules of oxygen.

        Photosynthesis consists of two main stages: the light-dependent reactions and the light-independent reactions, also known as the Calvin cycle. In the light-dependent reactions, which occur in the thylakoid membranes, sunlight is used to split water molecules, releasing oxygen as a byproduct and generating energy-rich compounds like ATP and NADPH. These compounds are then used in the Calvin cycle to fix carbon dioxide into glucose.

        Not only is photosynthesis crucial for producing the food plants need to grow, but it also releases oxygen into the atmosphere, which is essential for the survival of most living organisms. In fact, photosynthesis is the foundation of most ecosystems, as it provides both the oxygen we breathe and the organic materials that fuel food chains.

        Interestingly, photosynthesis is also a natural method of carbon capture. By absorbing carbon dioxide, plants help reduce the greenhouse effect and combat climate change. This is one reason why protecting forests and encouraging reforestation is vital for a healthy planet.

        In summary, photosynthesis is the life-sustaining process by which plants transform solar energy into chemical energy while producing oxygen and removing carbon dioxide from the atmosphere.
        """

    try:
        nlp_instance = NLP(text)

        print("\nNLP System initialized successfully!")
        print("\nTop keywords extracted from the document:")
        print(nlp_instance.keywords)

        while True:
            userInput = input("\nAsk a question (or type 'exit' to quit): ")
            if userInput.lower() == "exit":
                break

            qType, answers, history = nlp_instance.handleQuestion(userInput)

            print(f"\n[Question Type: {qType}]")
            for sent, score in answers:
                print(f"{sent.strip()} (score: {round(score, 2)})")

            recentQuestions = [q for q, _ in history]
            print("Recent questions:", recentQuestions)
            
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have scikit-learn installed: pip install scikit-learn")
