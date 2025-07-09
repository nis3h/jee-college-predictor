from predict_colleges import predict_colleges

# Try with sample data
result = predict_colleges(
    rank=10000,
    category="OBC-NCL",
    gender="female",
    preferred_branch="Computer"
)

print(result.head(10))
