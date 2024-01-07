import streamlit as st
import pandas as pd
import datetime
import pickle

# Step 1
def extract_week(df):
    try:
        df['Date'] = pd.to_datetime(df['Date'])
        df['Week'] = df['Date'].dt.isocalendar().week
        df['Year'] = pd.DatetimeIndex(df['Date']).year
        df['Month'] = pd.DatetimeIndex(df['Date']).month
    except Exception as e:
        st.error(f"Error during date extraction: {str(e)}")
    return df

# Step 2
def maping_type(df):
    try:
        df['Type'] = df['Type'].map({'A': 1, 'B': 2, 'C': 3})  # Convert to integer directly
    except Exception as e:
        st.error(f"Error during type mapping: {str(e)}")
    return df

# Step 3
def convert_to_int(df):
    try:
        df['Type'] = df['Type'].astype(int)
        df['IsHoliday'] = df['IsHoliday'].astype(int)
    except Exception as e:
        st.error(f"Error during data type conversion: {str(e)}")
    return df

# Step 4
def input_col_sel(df):
    input_col = ['Store', 'Dept', 'IsHoliday', 'Type', 'Size', 'Temperature',
                 'Fuel_Price', 'CPI', 'Unemployment', 'Week', 'Year', 'Month',
                 'Fuel_Price_Cat']
    return df[input_col]

def load_model():
    try:
        # Load the pre-trained model from the pickle file
        model = pickle.load(open('model.pkl', 'rb'))
        return model
    except Exception as e:
        st.error(f"Error loading the model: {str(e)}")
        return None

def predict_sales(model, input_data):
    try:
        # Make predictions using the loaded model
        # Replace this line with the appropriate prediction logic based on your model
        prediction = model.predict(input_data)
        return prediction
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        return None

def main():
    st.title("Walmart Sales Forecasting App")

    # Create input fields for manual input
    st.sidebar.header("Inputs")
    store = st.sidebar.number_input("Store", min_value=1, max_value=45, step=1, value=1)
    dept = st.sidebar.number_input("Dept", min_value=1, max_value=99, step=1, value=1)
    is_holiday = st.sidebar.checkbox("Is Holiday")
    type_input = st.sidebar.selectbox("Type", ['A', 'B', 'C'])
    size = st.sidebar.number_input("Size", min_value=34875, max_value=219622, step=1, value=34875)
    temperature = st.sidebar.number_input("Temperature", min_value=-2, max_value=100)
    fuel_price = st.sidebar.number_input("Fuel Price", min_value=2.5, max_value=4.4)
    cpi = st.sidebar.number_input("CPI", min_value=126, max_value=227)
    unemployment = st.sidebar.number_input("Unemployment", min_value=3.879, max_value=14.00, value=3.879)
    min_date = datetime.date(2010, 3, 1)  # Minimum allowed date
    input_date = st.sidebar.date_input("Date", min_value=min_date, value=datetime.date.today())
    fuel_price_cat = st.sidebar.number_input("Fuel Price Category", min_value=2.00, max_value=4.25)

    # Create a dataframe from manual input
    input_data = pd.DataFrame({
        'Store': [store],
        'Dept': [dept],
        'IsHoliday': [int(is_holiday)],
        'Type': [type_input],
        'Size': [size],
        'Temperature': [temperature],
        'Fuel_Price': [fuel_price],
        'CPI': [cpi],
        'Unemployment': [unemployment],
        'Date': [input_date],  # Use the manually input date
        'Fuel_Price_Cat': [fuel_price_cat]
    })

    # Load the model
    model = load_model()

    if model is not None and st.button("Predict Sales Amount"):
        # Apply the preprocessing steps to the manual input
        input_data = extract_week(input_data)
        input_data = maping_type(input_data)
        input_data = convert_to_int(input_data)
        input_data = input_col_sel(input_data)

        # Make predictions
        prediction = predict_sales(model, input_data)

        if prediction is not None:
            st.success(f"Prediction: {prediction}")

if __name__ == "__main__":
    main()
