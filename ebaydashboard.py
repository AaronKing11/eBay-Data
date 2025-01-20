import streamlit as st
import pandas as pd
import plotly.express as px

# Set the page layout to wide
st.set_page_config(layout="wide")

# Import the CSV file into a DataFrame
ebay_data_imported = pd.read_csv('ebay_data_clean.csv')

# Display the first few rows to verify
print(ebay_data_imported.head())

# create Streamlit app and display some text
st.header('eBay Data Exploration Dashboard')

# Create tabs using radio buttons
tabs = st.radio("Select a graph to view", ('Sales Records Filtered by Brand, Color, and Resolution Size', 
                                           'eBay Computers by Brand', 
                                           "Processing Speed's Impact on Price", 
                                           'eBay Computer Prices and their SSD Capacities'))

if tabs == 'Sales Records Filtered by Brand, Color, and Resolution Size':
    st.subheader('Sales Records Filtered by Brand, Color, and Resolution Size')
    st.write("The table below shows characteristics of computers listed on eBay that may help us inform its price. Included are technical measures (Hard Drive Capacity, Processor Speed, SSD Capacity, etc.) as well as feature measures (Brand, Model, Color, Screen Size).")

    # Get unique options for brand, color, and resolution size
    brand_options = ebay_data_imported['Brand'].unique()
    color_options = ebay_data_imported['Color'].unique()
    resolution_options = ebay_data_imported['Resolution Size'].unique()

    # Multiselect widgets for choosing multiple brands, colors, and resolution sizes
    brand_selection = st.multiselect('Select Brands', options=brand_options)
    color_selection = st.multiselect('Select Colors', options=color_options)
    resolution_selection = st.multiselect('Select Resolution Sizes', options=resolution_options)

    # Apply filters based on user selections
    filtered_df = ebay_data_imported

    if brand_selection:  # Filter by selected brands if any
        filtered_df = filtered_df[filtered_df['Brand'].isin(brand_selection)]

    if color_selection:  # Filter by selected colors if any
        filtered_df = filtered_df[filtered_df['Color'].isin(color_selection)]

    if resolution_selection:  # Filter by selected resolution sizes if any
        filtered_df = filtered_df[filtered_df['Resolution Size'].isin(resolution_selection)]

    # Display the filtered dataframe
    st.dataframe(filtered_df)

elif tabs == 'eBay Computers by Brand':
    st.subheader('eBay Computers by Brand')
    st.write("The graph below shows us the distribution of listed computers on eBay by the brand of the computer producer.")

    # Count the occurrences of each brand
    brand_counts = ebay_data_imported['Brand'].value_counts()

    # Create a horizontal bar chart (switch x and y axes)
    st.bar_chart(brand_counts)

    st.write("We can see in this chart that the market for computers on Ebay is dominated by a handful of brands: Dell, HP, and Lenovo. These are the brands that most often have computers listed on the site.")
    st.write("Either these brands are the most desired by consumers, most produced by producers, or both.")

elif tabs == "Processing Speed's Impact on Price":
    st.subheader("Processing Speed's Impact on Price")
    st.write("The graph below shows the relationship between a computer's processing speed, which describes how 'fast' it will run, and the price of the computer.")

    # Create the scatter plot for Processor Speed vs Price
    fig = px.scatter(
        ebay_data_imported, 
        x='Processor Speed (GHz)', 
        y='Price ($)', 
        title="Processor Speed vs Price", 
        labels={'Processor Speed (GHz)': 'Processor Speed (GHz)', 'Price ($)': 'Price ($)'}
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig)

    st.write("At first glance, there may not seem to be much of a relationship between a computer's processor speed and its listed price, which is certainly true for computers with processor speeds less than 4 GHz. However, we can see that the majority of computers with higher than 4 GHz tend to sell for more than the majority of computers with less than 3 GHz. This tells us that broadly speaking, a very high-end processor (4+ GHz) will have a positive impact on the value of the computer. Outside of that highest end, though, the computer's processor will not have much of an impact on its price.")

elif tabs == 'eBay Computer Prices and their SSD Capacities':
    st.subheader('eBay Computer Prices and their SSD Capacities')
    st.write("The graph below shows the relationship between a computer's SSD capacity, which corresponds to the amount of data it can store, and the computer's price.")

    # Filter the data based on 'Condition'
    new_computers = ebay_data_imported[ebay_data_imported['Condition'] == 'New']
    used_computers = ebay_data_imported[ebay_data_imported['Condition'] == 'Used']

    # Create a scatter plot
    fig = px.scatter()

    # Add scatter plots for "New" and "Used" computers
    fig.add_scatter(x=new_computers['SSD Capacity (GB)'], y=new_computers['Price ($)'], mode='markers', name='New', marker=dict(color='blue'))
    fig.add_scatter(x=used_computers['SSD Capacity (GB)'], y=used_computers['Price ($)'], mode='markers', name='Used', marker=dict(color='red'))

    # Customize the layout
    fig.update_layout(
        title="SSD Capacity vs Price by Condition",
        xaxis_title="SSD Capacity (GB)",
        yaxis_title="Price (USD)",
        legend_title="Condition"
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig)

    st.write("While the SSD capacities and prices of the listed computers vary widely, we can observe that computers with a SSD capacity of 64 GB or less will be listed at very low prices. Only once their SSD capacities exceed 256 GB do we begin to see computer prices above $1000.")
    st.write("This is not to say that higher SSD capacities will always lead to more expensive computers, as there are ones listed at low prices with higher SSD capacities. But in essence, a low-priced computer will not always have a low SSD capacity, but computers with a low SSD capacity (128 or less) will generally always have a low price.")
    st.write("It seems that higher SSD capacities have some sort of relationship with higher prices for computers, and the relationship appears to be stronger for new computers rather than used computers. This makes sense, considering that used computers vary in their condition, which we can't account for in this graph other than the umbrella filter.")

