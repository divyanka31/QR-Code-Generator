import qrcode
from urllib.parse import urlencode, quote


def generate_upi_qr():
    print("\n=== UPI Payment QR Generator ===")

    upi_id = input("Enter your UPI ID: ").strip()
    payee_name = input("Enter payee name: ").strip()

    # Basic input validation
    if (
        not upi_id
        or not payee_name
        or upi_id.count("@") != 1
        or any(ch.isspace() for ch in upi_id)
    ):
        print("Please enter a valid UPI ID and payee name.")
        return

    # No amount is included, so the payer can enter one
    # in a compatible UPI app.
    payment_details = {
        "pa": upi_id,
        "pn": payee_name,
        "cu": "INR",
    }

    payment_uri = "upi://pay?" + urlencode(
        payment_details, quote_via=quote
    )

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(payment_uri)
    qr.make(fit=True)

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    filename = "upi_payment_qr.png"
    image.save(filename)

    print("\nQR code generated successfully!")
    print(f"Saved as: {filename}")
    print("Scan it with a compatible UPI app to test.")
    print("Always verify the recipient before paying.")


if __name__ == "__main__":
    generate_upi_qr()
