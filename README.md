
# Chicken Disease Classification Project

## Overview

The **Chicken Disease Classification Project** is a machine learning application designed to identify various chicken diseases based on image data. This project leverages a Convolutional Neural Network (CNN) for classification, with a deployment setup that enables real-time predictions via a Flask API.

### Main Features
- **Image-based Disease Classification**: Automatically identifies chicken diseases from input images.
- **Modular Architecture**: Organized for scalability and ease of maintenance.
- **Data Versioning**: Ensures reproducibility with DVC (Data Version Control).
- **API Deployment**: Serves predictions through a Flask API.

### Intended Use
This project is designed for agricultural researchers and poultry farmers who need automated disease detection in chickens, enabling timely treatment and management.

### Key Components
1. **Data Ingestion**: Manages the retrieval of image data, with DVC ensuring version control and reproducibility.
2. **Data Processing**: Includes pre-processing steps such as resizing, normalization, and augmentation to prepare images for training.
3. **Model Training**: Uses TensorFlow to train a CNN on processed data.
4. **Model Evaluation**: Evaluates the model’s accuracy and recall using metrics like precision, recall, and F1 score.
5. **Deployment**: Provides an endpoint via Flask for external applications to submit images and receive disease predictions.

## Technologies & Libraries

The project uses a combination of libraries and tools to handle various stages of the machine learning pipeline:

- **TensorFlow**: Core library for building and training the CNN model.
- **DVC**: Manages data and model versioning.
- **Flask**: Used for creating a web API to serve model predictions.
- **Pandas & Numpy**: Data handling and processing.
- **Matplotlib & Seaborn**: Visualization tools for evaluating model performance.
- **Python Box & PyYAML**: Configuration management.
- **Docker**: Optional containerization for consistent deployment.

## Project Structure

```
Chicken-Disease-Classification-Project/
│
├── src/
│   └── cnnclassifier/
│       ├── components/          # Data processing components
│       ├── config/              # Configuration management
│       ├── constants/           # Static values and constants
│       ├── entity/              # Data entities and model structures
│       ├── pipeline/            # Training and evaluation pipeline
│       └── utils/               # Utility functions
│
├── config/                      # Configuration files
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
├── params.yaml                  # Hyperparameters and configuration values
└── dvc.yaml                     # DVC configuration
```

## Installation and Setup

### Prerequisites
Ensure that you have the following installed:
- **Python 3.8+**
- **pip** (Python package installer)
- **DVC** (Data Version Control)
- **Docker** (Optional, for containerized deployment)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/Chicken-Disease-Classification-Project.git
   cd Chicken-Disease-Classification-Project
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure DVC for Data Access**
   Pull the latest dataset using DVC. Ensure you have access to the remote storage.
   ```bash
   dvc pull
   ```

4. **Run the Setup**
   Use the setup script to initialize directories and files if needed.
   ```bash
   python setup.py install
   ```

5. **Environment Variables**
   Configure environment variables in a `.env` file (if required), including paths to data, model weights, and other configuration options.

## Usage

### Training the Model
To train the model, use the following command:
```bash
python src/cnnclassifier/pipeline/train.py
```

### Running the API
After training, you can start the Flask API to serve predictions.
```bash
python src/app.py
```
Submit an image to the API endpoint to receive a classification result.

### Example API Request
```python
import requests

# Example: Posting an image for prediction
url = "http://localhost:5000/predict"
files = {'file': open('path_to_image.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

## Configuration

### Parameters
The parameters for training, such as batch size, learning rate, and epochs, are managed in `params.yaml`. Update this file as needed before starting training.

### Docker Configuration
To run the application in a Docker container:

1. **Build the image**:
   ```bash
   docker build -t chicken-disease-classifier .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 chicken-disease-classifier
   ```

## Testing

Testing can be performed by using unit tests and integration tests. The project is set up to support tests for:

- **Data Processing Functions**
- **Model Training and Evaluation**
- **API Endpoints**

Use `pytest` to run tests:
```bash
pytest tests/
```

## Contribution Guidelines

1. **Fork the Repository**
2. **Create a Feature Branch**
3. **Commit Changes**
4. **Push to Branch and Submit a Pull Request**

Ensure that all tests pass before submitting your PR.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
