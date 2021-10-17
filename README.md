# Setup databases

```
python3 setup.py
```

# Run application

```
python3 app.py
```

# Docker Deployment

```
sudo docker build -t pydev .
sudo docker run -dp 8888:8888 pydev
```

# Tests

```
python3 -m pytest
```

# GraphQL

```
mutation CreateReview {
  createReview(
    book_id: 2,
    rating: 2
    review:"Some Description") {
    review {
      id
      book_id
      rating
      review
      created_at
    }
    success
    errors
  }
}
```

# Microservice architecture

![acrhitecture](https://user-images.githubusercontent.com/22059171/136710809-e4a1a63f-e324-4efd-9ad9-4744ddb165f1.png)
