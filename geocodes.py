import pandas as pd
from geocodio import Geocodio

df = pd.read_csv('pathway_to_your_csv.csv')

# Creating new dataframe to pass into Geocodio
addr_df = df[['street', 'city', 'state', 'postal_code']]
addr_df = addr_df.fillna('')    #Fill NaN values with empty strings to avoid JSON issues

# Convert to JSON to meet Geocodio requirements 
addr_json = addr_df.to_dict(orient='records')

# Make the API call
geo = Geocodio()
geocodes = geo.get_geocodes()

data = []

for result in geocodes.get('results', []):
  query_info = result.get('query', {})

  for response_item in result.get('response', {}).get('results', []):
    # Extract geocode information
    addr = response_item.get('formatted_address', {})
    lat = response_item.get('lat')
    long = response_item.get('lng')
    school_districts = response_item.get("fields", {}).get("school_districts", {})

    # Append values to the data list 
    data.append({
      'lat': lat, 
      'lng': long,
      'school_district': school_district

df_final = pd.DataFrame(data)
