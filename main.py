import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

# print("Setup complete.")

# reviews.head()
desc = reviews.description


# first_description = desc.iloc[0]

# print("Description: ", desc)
# first_row = reviews.iloc[0]
# print("First row: ", first_row)

# Select the first 10 values from the description column in reviews,
# assigning the result to variable first_descriptions.

# first_descriptions = reviews.loc[:9, "description"]
# first_descriptions = reviews.description.iloc[:10]
# desc.head(10)
# Note: loc usually is used with text
# print("First descriptions: ", first_descriptions)


# Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
# sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]
# print("Sample views 1,2, 3, 5, 8: ", sample_reviews)

# Create a variable df containing the country, province, region_1,
# and region_2 columns of the records with the index labels 0, 1, 10, and 100.
# In other words, generate the following DataFrame:

# df = reviews.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
# print("DATA: ", df)

# Create a variable df containing the country and variety columns of the first 100 records.

# cols = ['country', 'variety']
# df = reviews.loc[:99, cols]
# # or
# cols_idx = [0, 11]
# df = reviews.iloc[:100, cols_idx]
# print("DATA: ", df)
# 8.Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?

# df = reviews.loc[(reviews.country == 'Italy')]
# print("Made in Italy: ", df)

# 9. Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from
# Australia or New Zealand.
# head_reviews = reviews.iloc[:1000]
# df = head_reviews.loc[reviews.country.isin(['Australia', 'New Zealand']) & (reviews.points >= 95)]
# print("Made in Australia or New Zealand: ", df)

# What is the median of the points column in the reviews DataFrame?
# median = reviews.describe().median()
# print("Median: ", median)

# What countries are represented in the dataset? (Your answer should not include any duplicates.)
# countries = reviews.country.unique()
# print("Countries: ", countries)

# How often does each country appear in the dataset? Create a Series reviews_per_country mapping countries to the
# count of reviews of wines from that country.
# reviews_per_country = reviews.country.value_counts()
# print(reviews_per_country)

# 4.Create variable `centered_price` containing a version of the `price` column with the mean price subtracted.
# centered_price = reviews.price - reviews.price.mean()
#
# print("Centered Price: ", centered_price)


# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable bargain_wine with the title of
# the wine with the highest points-to-price ratio in the dataset.
# bargain_idx = (reviews.points / reviews.price).idxmax()
# print("IDMAX: ", bargain_idx)
# bargain_wine = reviews.loc[bargain_idx, 'title']
# print("Bargain_wine: \n", bargain_wine)

# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical"
# or "fruity"? Create a Series descriptor_counts counting how many times each of these two words appears in the
# description column in the dataset. (For simplicity, let's ignore the capitalized versions of these words.)
# n_trop = desc.map(lambda des: "tropical" in des).sum()
# Hàm isin chỉ check khớp giá trị
# n_trop = desc.map(lambda desc: "tropical" in desc).sum()
# n_fruity = reviews.description.map(lambda des: "fruity" in des).sum()
#
# s_df = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
# print(s_df)

# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard
# to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars,
# a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.

# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should
# automatically get 3 stars, regardless of points.

# Create a series star_ratings with the number of stars corresponding to each review in the dataset.

def convert_star(points):
    if points > 95:
        return 3
    elif 85 <= points < 95:
        return 2
    else:
        return 1


# star_ratings = reviews.points.map(lambda item: convert_star(item))
star_ratings = reviews.apply(convert_star, axis='columns')
print(star_ratings)
