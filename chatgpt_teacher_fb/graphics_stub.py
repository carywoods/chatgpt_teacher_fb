# Reattempting to generate all the graphics based on the provided and assumed data in the analysis summary.

# Setup for generating the graphics

## Sentiment Distribution
sentiments = ['Positive', 'Neutral', 'Negative']
sentiment_values = [138, 18, 16]  # Provided sentiment analysis output

## Themes and Post Counts
themes = ['Technology Integration', 'Curriculum Development', 'Classroom Management', 'Other']
theme_counts = [34, 16, 7, 103]  # Actual counts from classification

## Average Likes by Theme (Assumed for demonstration)
average_likes = [120, 100, 80, 90]  # Assumed average likes for visualization

# Generate Sentiment Distribution Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(sentiment_values, labels=sentiments, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99'])
plt.title('Sentiment Distribution Among Posts')
plt.show()

# Generate Top Themes in Discussions Bar Chart
plt.figure(figsize=(8, 6))
positions = np.arange(len(themes))
plt.bar(positions, theme_counts, color=['#66b3ff','#99ff99','#ffcc99','#ff9999'])
plt.xticks(positions, themes)
plt.xlabel('Themes')
plt.ylabel('Number of Posts')
plt.title('Post Frequencies by Theme')
plt.xticks(rotation=45)
plt.show()

# Generate Engagement Levels by Theme Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(positions, average_likes, color=['#66b3ff','#99ff99','#ffcc99','#ff9999'])
plt.xticks(positions, themes)
plt.xlabel('Themes')
plt.ylabel('Average Number of Likes')
plt.title('Average Likes by Theme')
plt.xticks(rotation=45)
plt.show()
