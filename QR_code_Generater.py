import qrcode  # Import the qrcode library to generate QR codes

# Define the URL to be encoded in the QR code
website_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Create a QRCode object with specific parameters: version, box size, and border size
qr = qrcode.QRCode(version=1, box_size=5, border=5)

# Add the website link to the QR code data
qr.add_data(website_link)

# Generate the QR code based on the added data
qr.make()

# Create an image of the QR code with specified fill and background colors
img = qr.make_image(fill_color='black', back_color='white')

# Save the generated QR code image to a file
img.save('youtube_qr.png')
