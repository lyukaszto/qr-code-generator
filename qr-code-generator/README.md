# QR Code Generator

This project is a QR code generator that supports multiple users. It allows users to create and save QR codes based on the data they provide. The application manages user accounts and sessions, ensuring that each user can generate QR codes independently.

## Project Structure

```
qr-code-generator
├── src
│   ├── main.py               # Entry point of the application
│   ├── qr_generator.py       # QR code generation logic
│   ├── user_management.py     # User account management
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Project dependencies
├── .gitignore                # Files to ignore in Git
└── README.md                 # Project documentation
```

## Features

- User registration and authentication
- QR code generation based on user input
- Saving generated QR codes to specified file paths
- User-friendly interface for managing QR code generation

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd qr-code-generator
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## Usage Guidelines

- Register a new user by providing a username and password.
- Authenticate using your credentials to access the QR code generation features.
- Input the data you want to encode into a QR code and specify the file path to save it.

## Dependencies

This project requires the following Python packages:

- `qrcode`: For generating QR codes.
- `Flask`: For creating the web application interface.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.