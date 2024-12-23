import json

# Open and load the JSON file
with open('posts.json', 'r') as f:
    posts_json = json.load(f)  # Load the data from the JSON file

print(posts_json)  # Print the loaded data
