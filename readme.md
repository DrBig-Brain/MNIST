# MNIST Digit Recognition Web App

This project is a web application for handwritten digit recognition using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The app allows users to draw a digit on a canvas and predicts the digit using a trained Keras model.

## Folder Structure

```
.
├── app.py              # Streamlit web app for digit prediction
├── model.ipynb         # Jupyter notebook for model training
├── model.keras         # Saved Keras model
├── requirements.txt    # Python dependencies
├── test.ipynb          # Notebook for testing the model
└── readme.md           # Project documentation
```

## Getting Started

### 1. Install Dependencies

Install the required Python packages:

```sh
pip install -r requirements.txt
```

### 2. Train the Model (Optional)

You can retrain the model using [model.ipynb](model.ipynb). The trained model will be saved as `model.keras`.

### 3. Run the Web App

Start the Streamlit app:

```sh
streamlit run app.py
```

### 4. Usage

- Draw a digit (0-9) on the canvas.
- Click the **Predict** button.
- The predicted digit will be displayed.

## Files

- [`app.py`](app.py): Main Streamlit application.
- [`model.ipynb`](model.ipynb): Notebook for training the CNN model.
- [`model.keras`](model.keras): Saved trained model.
- [`test.ipynb`](test.ipynb): Notebook for testing the model on images.
- [`requirements.txt`](requirements.txt): List of dependencies.

## Requirements

- Python 3.7+
- streamlit
- keras
- tensorflow
- numpy
- matplotlib
- pillow
- streamlit-drawable-canvas

## License

This project is for educational purposes.