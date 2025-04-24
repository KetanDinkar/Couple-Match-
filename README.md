💘 Couple Match – Fun with Image Processing & Hashing
Welcome to Couple Match — a playful yet insightful project exploring how basic image processing and perceptual hashing can be used to compare faces and find visually similar "matches."
This project isn't about real matchmaking — it’s just a creative way to demonstrate how perceptual hashing and Hamming distance can be used in image comparison. So relax, it's code with a dash of fun!

🧠 What It Does
This local image-based algorithm takes one image (your own) and compares it to a set of other images (sample female faces). Using perceptual hashing, the algorithm finds which image is most visually similar and declares it the "best match" by calculating the smallest Hamming distance between hashes.
The result? A side-by-side image of the matched pair with a "Love Score" based on visual similarity!

🔧 How It Works
Uses the phash (perceptual hash) method from the imagehash library to convert images into hash values.
Normalizes the hash to scale similarity scores between 1 and 10.
Computes the Hamming distance between hashes to determine similarity.
Selects and displays the image pair with the lowest distance (i.e., highest similarity).
Shows both images side by side with the calculated Love Score.

📁 Folder Structure
/me – contains the base image (your image).
/she – contains the images to compare (sample women images).
main.py – the core Python script performing hash computation and matching.


🧩 Applications
While the project is light-hearted, the technique used here has real applications:
Image deduplication
Content similarity detection
Basic facial similarity checking
Educational demos in image processing

📝 Note
This project was created purely for educational and entertainment purposes. It’s not a serious matchmaking tool — just a fun way to explore how perceptual hashing and basic algorithms work in image analysis.


🔗 Check out the demo and insights on LinkedIn:
👉 https://www.linkedin.com/posts/ketan-dinkar-82b465303_imageprocessing-python-computervision-activity-7321125787246489600-YfFn

Have fun exploring love — one pixel at a time! 💻❤️
