import cv2
import pytesseract
import time
import requests
import re
import firebase_admin
from firebase_admin import credentials,firestore

cred = credentials.Certificate("parking-slot-booker-firebase-adminsdk-wxj30-668cad7aa0.json")
firebase_admin.initialize_app(cred)

# Set up the camera
camera = cv2.VideoCapture(0)  # 0 for the default camera

# Set up Tesseract OCR
# Path to your Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set up the URL
url = "https://example.com"  # Replace with the desired URL
db = firestore.client()
while True:
    # Capture frame from the camera
    
    ret, frame = camera.read()
    

    # Convert the frame to grayscale for better OCR results
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale frame
    text: str = pytesseract.image_to_string(gray)

    # Print the extracted text
    
    text = text.upper()  # Convert to uppercase
    text = text.strip()  # Remove leading and trailing whitespace characters
 
    text = re.sub(r'[^A-Z0-9]', '', text)  # Remove non-alphanumeric characters
    text = text[:9]
    print("Extracted Text:", text)

    # Send a request to the URL with the extracted text
    # Replace "text" with the desired parameter name for the text
    if text != "" and len(text) > 6:
    # Construct the document reference
        doc_ref = db.collection('bookings').document(text)

    # Get the document
        result = doc_ref.get()
        result = result.to_dict()

    # Process the response as needed
        if result is None:
            print("No such document!")
        else:
            vehicleId = result.get("vehicleId")
            print(vehicleId)
        

    # Display the captured frame
    cv2.imshow("Camera", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
