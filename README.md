# TAP - Transcript Analysis Project

A Python-based natural language processing tool for analyzing transcripts produced by real-time captionists. Uses NLTK, word clouds, and statistical analysis to extract insights from transcription data.

## Overview

TAP (Transcript Analysis Project) was created to analyze typed transcripts from real-time captionists at RIT's RTC/NT department. The tool processes .docx transcript files to generate frequency distributions, collocations, word clouds, and other linguistic analyses.

**Authors**: Mike Donovan, Thomas Kinsman

## Features

- **Document Processing**: Batch processing of .docx transcript files
- **NLP Analysis**:
  - Word tokenization and frequency analysis
  - Stopword filtering
  - Collocation detection
  - Contraction expansion
  - Sentence tokenization
- **Visualization**: Automatic word cloud generation
- **Export**: CSV output of analysis results

## Installation

### Prerequisites

- Python 3.7+
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/mpdnes/transcript-analysis-pipeline.git
cd transcript-analysis-pipeline
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download required NLTK data:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

## Usage

### Basic Usage

Place your .docx transcript files in the `TEST_SUITE` directory (or specify a custom directory), then run:

```bash
cd TAPv0_1_1
python TAP.py
```

### Project Structure

```
transcript-analysis-pipeline/
├── TAPv0_1_1/              # Main application code
│   ├── TAP.py              # Main analysis script
│   ├── preprocessing.py    # Document preprocessing utilities
│   ├── postprocessing.py   # Analysis output formatting
│   └── setup.py            # Configuration
├── TEST_SUITE/             # Directory for transcript files
├── BUILD_CLASSIFIER_for_UNIGRAMS/  # MATLAB classifier scripts
└── requirements.txt        # Python dependencies
```

## Components

### Preprocessing (`preprocessing.py`)
- Directory inspection and file discovery
- .docx file parsing
- Text cleaning and normalization

### Main Analysis (`TAP.py`)
- Term frequency calculation
- Collocation detection
- Word cloud generation
- Statistical analysis

### Postprocessing (`postprocessing.py`)
- Results formatting
- CSV export
- Visualization output

## Analysis Pipeline

1. **Document Discovery**: Scans directory for .docx files
2. **Text Extraction**: Reads and parses transcript content
3. **Preprocessing**: Tokenization, stopword removal, contraction expansion
4. **Frequency Analysis**: Calculates term frequencies and distributions
5. **Collocation Detection**: Identifies word pairs and phrases
6. **Visualization**: Generates word clouds
7. **Export**: Saves results to CSV

## Dependencies

- `docxpy`: Reading .docx files
- `nltk`: Natural language processing
- `wordcloud`: Word cloud generation
- `matplotlib`: Plotting and visualization
- `Pillow`: Image processing
- `contractions`: Contraction expansion
- `numpy`: Numerical operations
- `scikit-learn`: Statistical analysis

## Output

TAP generates:
- **Word clouds**: Visual representations of term frequencies
- **CSV files**: Detailed frequency distributions
- **Statistics**: Collocation analysis and linguistic metrics

## Research Context

This project was developed as part of research into real-time captioning quality and linguistic patterns in educational transcription. The analysis helps identify common terms, captioning patterns, and areas for improvement in real-time captioning services.

## License

MIT License - see LICENSE file for details

## Version History

**Version 0.1** (03/01/23)
- Initial GitHub upload
- Basic transcript analysis functionality

**Version 0.1.1** (03/16/23)
- Repository restructuring
- Enhanced preprocessing pipeline
- Added visualization capabilities

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

## Acknowledgments

Developed at Rochester Institute of Technology for the RTC/NT department.

