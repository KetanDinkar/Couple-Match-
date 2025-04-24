import glob
import imagehash
from PIL import Image

def normalize_hash_value(hash_int):
    # Normalize hash value to be between 1 and 10
    return (hash_int / (2**64 - 1)) * (10 - 1) + 1

my_hash = 0
highest_love_score = float('inf')  # Start with a very large value
selected = None

# File paths
me = glob.glob(r'C:\programs\python\finding her\me\*.jpg')
she = glob.glob(r'C:\programs\python\finding her\she\*.jpg')

# Compute the average hash for "me"
for m_path in me:
    m_image = Image.open(m_path)  # Open image for getting size later
    image_hash_me = int(str(imagehash.phash(m_image)), 16)
    normalized_hash_me = normalize_hash_value(image_hash_me)
    print(f"\nHash for {m_path}: {image_hash_me} : {normalized_hash_me}")

    # Compare "me" hash with each "she" image
    for s_path in she:
        s_image = Image.open(s_path)  # Open image for getting size later
        her_hash = int(str(imagehash.phash(s_image)), 16)
        normalized_hash_she = normalize_hash_value(her_hash)
        print(f"\nHash for {s_path}: {her_hash} : {normalized_hash_she}")

        # Calculate absolute difference in normalized hash values
        distance = abs(normalized_hash_me - normalized_hash_she)

        # Select the image with the smallest difference (lowest Hamming distance)
        if 0 <= distance <= 3 and distance < highest_love_score:
            highest_love_score = distance
            selected = s_path
            print("Love Score:", highest_love_score)

            # Create a new image with both images side by side
            couple = Image.new('RGB', (m_image.width + s_image.width, m_image.height))
            couple.paste(m_image, (0, 0))  # Paste "me" image
            couple.paste(s_image, (m_image.width, 0))  # Paste "she" image next to it
            couple.show()

