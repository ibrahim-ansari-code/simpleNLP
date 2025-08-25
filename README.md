# NLP Question-Answer System

A Python-based Natural Language Processing system that can analyze text documents and answer questions about them.

## What This System Does

This NLP system processes text documents and provides intelligent answers to questions by:

1. **Document Processing**: Cleans and segments text into sentences
2. **Keyword Extraction**: Identifies important terms using TF-IDF analysis  
3. **Question Classification**: Categorizes questions as definition, explanation, fact, or unknown
4. **Answer Extraction**: Uses different extraction strategies based on question type
5. **Similarity Matching**: Finds relevant text spans using cosine similarity
6. **Memory System**: Remembers previous questions for follow-up queries

## File Structure

```
nlp_classes/
├── README.md                 # This file
├── run.py                   # Main runner script
├── run.sh                   # Bash script to run the system
├── venv/                    # Virtual environment (auto-generated)
├── base_extractor.py        # Abstract base class for extractors
├── definition_extractor.py  # Extracts definitions from text
├── explanation_extractor.py # Extracts explanations from text  
├── span_extractor.py        # Extracts relevant text spans
├── sentence_extractor.py    # Returns full sentences
├── classifier.py            # Classifies question types
├── preprocessing.py         # Text cleaning and tokenization
├── keywords.py              # TF-IDF keyword extraction
├── similarity.py            # Cosine similarity matching
├── stack_q.py              # Question/answer memory
└── nlp.py                  # Main NLP controller
```

## How to Run

### Option 1: Using the bash script (easiest)
```bash
./run.sh
```

### Option 2: Using Python directly
```bash
./venv/bin/python run.py
```

## How to Use

1. Run the system using one of the methods above
2. The system will load a default text about photosynthesis
3. You can ask questions like:
   - "What is photosynthesis?" (definition questions)
   - "Why do plants need sunlight?" (explanation questions)  
   - "How does photosynthesis work?" (fact questions)
4. Type 'exit' to quit the system

## Question Types

The system classifies questions into four categories:

- **Definition**: "What is...", "Define..." → Uses DefinitionExtractor
- **Explanation**: "Why...", questions with "cause" → Uses ExplanationExtractor
- **Fact**: Questions ending with "?" → Uses SpanExtractor
- **Unknown**: Other questions → Uses SentenceExtractor

## Customizing Input Text

To use your own text file instead of the default, edit the `path` variable in `run.py`:

```python
path = "/path/to/your/text/file.txt"
```

## Dependencies

- Python 3.7+
- scikit-learn (automatically installed in virtual environment)
- numpy (automatically installed with scikit-learn)
- scipy (automatically installed with scikit-learn)

## Example Session

```
NLP System initialized successfully!

Top keywords extracted from the document:
['the', 'and', 'is', 'of', 'energy', 'photosynthesis', 'carbon', 'in', 'dioxide', 'into']

Ask a question (or type 'exit' to quit): what is photosynthesis

[Question Type: definition]
is a biochemical process through which plants, algae, and some bacteria convert light energy into chemical energy (score: 0.62)
is the life-sustaining process by which plants transform solar energy into chemical energy while producing oxygen and removing carbon dioxide from the atmosphere (score: 0.68)
is also a natural method of carbon capture (score: 0.66)
Recent questions: ['what is photosynthesis']
```

## System Architecture

The system uses a modular design with separate classes for different functionalities:

1. **Preprocessing**: Handles text cleaning, sentence segmentation, and tokenization
2. **Classification**: Determines the type of question being asked
3. **Extraction**: Uses different strategies to extract relevant information based on question type
4. **Similarity**: Computes semantic similarity between questions and text passages
5. **Memory**: Tracks conversation history for context-aware responses

This allows for easy extension and modification of individual components without affecting the entire system.
