# Walmart Sales Forecasting App


HuggingFace Space: https://huggingface.co/spaces/animay620/SMS_Spam_Classifier

![image](https://github.com/animay7860/Walmart-Sales-Forecasting/assets/99870091/60e6887f-60a2-441e-b4e5-8c4fd0f62467)

This Streamlit app is designed for predicting Walmart sales based on user-provided input. It utilizes a pre-trained model to make predictions, considering various input features such as store information, department, weather conditions, and economic indicators.

## Getting Started

1. **Installation:**
   - Make sure you have Python installed on your machine.
   - Install the required dependencies using the following command:

     ```bash
     pip install -r requirements.txt
     ```

2. **Run the App:**
   - Execute the following command to run the Streamlit app:

     ```bash
     streamlit run app.py
     ```

3. **Usage:**
   - Access the app through your web browser (usually at http://localhost:8501).
   - Input relevant details such as store, department, date, and various other factors to predict Walmart sales.

## Input Fields

The app provides user-friendly input fields for manual input, allowing you to customize the prediction based on your specific scenario. These input fields include information such as store number, department, holiday status, type, size, temperature, and economic indicators.

## Additional Information

- The model used for prediction is loaded from a pre-trained pickle file (`model.pkl`).
- Ensure that the required Python packages are installed by checking the `requirements.txt` file.

## Author

[Your Name]

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to customize this README to include additional information about your app, usage instructions, or any other relevant details. Provide clear instructions for users to understand how to interact with and benefit from your Walmart Sales Forecasting App.
