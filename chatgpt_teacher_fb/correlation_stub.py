# Function to convert 'K' notation to numeric value
def k_to_numeric(value):
    if 'K' in str(value):
        return float(value.replace('K', '')) * 1000
    else:
        return float(value)

# Apply the conversion function to the 'NUMBER OF LIKES' column
cleaned_data['NUMBER OF LIKES'] = cleaned_data['NUMBER OF LIKES'].apply(k_to_numeric)

# Recalculate the correlation matrix with the corrected 'NUMBER OF LIKES' values
correlation_matrix = cleaned_data[['NUMBER OF LIKES', 'Sentiment Score', 'Category Numeric']].corr()

correlation_matrix
