import qr_image;

# Path to the uploaded file
file_path = "Channel Guide.pdf"

# Create a QR code for the document
qr = qr_image.QRCode(
    version=1,
    error_correction=qr_image.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Set the URL for the document (assuming it can be accessed via URL)
qr.add_data(file_path)
qr.make(fit=True)

# Create an image from the QR Code
qr_image = qr.make_image(fill="black", back_color="white")

# Display the QR code
qr_image.show()
