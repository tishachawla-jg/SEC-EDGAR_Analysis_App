import streamlit as st
import json
import plotly.express as px
import pandas as pd
import main as backend 

# Visualization Functions

def visualize_bar_graph(df, x_label, y_label):
    """Generate a bar graph from the DataFrame with specified x and y labels."""
    try:
        fig = px.bar(
            df,
            x=x_label,
            y=y_label,
            title=f"Bar Graph of {y_label} by {x_label}",
            labels={x_label: x_label.replace('_', ' ').title(), y_label: y_label.replace('_', ' ').title()}
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error generating bar graph: {e}")

def visualize_line_chart(df, x_label, y_label):
    """Generating a line chart from the DataFrame with specified x and y labels."""
    try:
        fig = px.line(
            df,
            x=x_label,
            y=y_label,
            title=f"Line Chart of {y_label} by {x_label}",
            labels={x_label: x_label.replace('_', ' ').title(), y_label: y_label.replace('_', ' ').title()}
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error generating line chart: {e}")

def visualize_scatter_plot(df, x_label, y_label):
    """Generating a scatter plot from the DataFrame with specified x and y labels."""
    try:
        fig = px.scatter(
            df,
            x=x_label,
            y=y_label,
            title=f"Scatter Plot of {y_label} by {x_label}",
            labels={x_label: x_label.replace('_', ' ').title(), y_label: y_label.replace('_', ' ').title()}
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error generating scatter plot: {e}")

def visualize_histogram(df, x_label):
    """Generating a histogram from the DataFrame with the specified x label."""
    try:
        fig = px.histogram(
            df,
            x=x_label,
            title=f"Histogram of {x_label}",
            labels={x_label: x_label.replace('_', ' ').title()}
        )
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Error generating histogram: {e}")

# Processing and Visualization

def process_and_visualize_response(response):
    """Process the JSON response and visualize data with all available chart types."""
    try:
        # Parse the response as JSON
        json_data = json.loads(response)

        # Convert JSON to DataFrame with the first two keys
        df, x_key, y_key = process_json_to_dataframe(json_data)

        if df is None or df.empty:
            st.error("The data resulted in an empty DataFrame.")
            return

        # Display all chart types together
        st.subheader('Bar Graph')
        visualize_bar_graph(df, x_label=x_key, y_label=y_key)

        st.subheader('Line Chart')
        visualize_line_chart(df, x_label=x_key, y_label=y_key)

        st.subheader('Scatter Plot')
        visualize_scatter_plot(df, x_label=x_key, y_label=y_key)

        st.subheader('Histogram')
        visualize_histogram(df, x_label=x_key)

    except json.JSONDecodeError as e:
        st.error(f"Invalid JSON format: {e}")

# Helper Function to Process JSON Data

def process_json_to_dataframe(json_data):
    """Convert varying JSON data to a Pandas DataFrame, ensuring valid x and y keys."""
    try:
        keys = list(json_data.keys())
        if len(keys) < 2:
            st.error("The JSON data should contain at least two fields.")
            return None, None, None

        x_key = keys[0]
        y_key = keys[1]

        x_values = json_data.get(x_key, [])
        y_values = json_data.get(y_key, [])

        if len(x_values) != len(y_values):
            st.error(f"The lengths of '{x_key}' and '{y_key}' do not match.")
            return None, None, None

        data = [{x_key: x, y_key: y} for x, y in zip(x_values, y_values)]
        df = pd.DataFrame(data)

        df[y_key] = pd.to_numeric(df[y_key], errors='coerce')

        return df, x_key, y_key

    except Exception as e:
        st.error(f"Error processing data: {e}")
        return None, None, None

# Main App

def app_main():
    st.title('Gemini Response Explorer')
    query = st.text_input('Enter your query')
    if st.button('Get Response'):
        context = []  # Populate this with relevant context data
        response = backend.get_gemini_response(query, context)  # Reference the function correctly
        st.subheader('Gemini Response (Raw):')
        st.write(response)

        # Process and visualize the response if it's in JSON format
        process_and_visualize_response(response)

if __name__ == '__main__':
    app_main()
