from deepface import DeepFace
im1 = "/Users/saintmantis/Downloads/IMG-20221123-WA0003.jpg"
im2 = "/Users/saintmantis/Downloads/IMG-20221025-WA0010.jpg"
result = DeepFace.verify(im1, im2)
print("Is verified: ", result["verified"])