# SMTP Client Programming Assignment
## CPSC 471-02, Summer 2025

### Student Information
- **Names:** Aidan Williams, Brandon Cobb, Joshua Germing

### Project Description
This project implements an SMTP client that can send emails through mail servers. It consists of two parts:
- **Part A:** Basic SMTP client implementation
- **Part B:** Enhanced SMTP client with TLS/SSL support for Gmail

### Files Included
1. `mail_client.py` - Part A: Basic SMTP client
2. `mail_client_tls.py` - Part B: SMTP client with TLS/SSL for Gmail
3. `README.md` - This documentation file
4. Screenshots of successful email delivery

### How to Execute

#### Part A - Basic SMTP Client
```bash
python3 mail_client.py
```

**Note:** You need to modify the following variables in the code:
- `mailserver`: Set to your preferred mail server
- Email addresses in MAIL FROM and RCPT TO commands

#### Part B - Gmail with TLS/SSL
```bash
python3 mail_client_tls.py
```

**Before running, update these variables in the code:**
- `GMAIL_USERNAME`: Your Gmail address
- `GMAIL_PASSWORD`: Your Gmail App Password (16 characters)
- `RECIPIENT_EMAIL`: Recipient's email address
- We did not want to include our own emails and passwords for security purposes.

### Expected Output
Both programs will display the SMTP protocol conversation, showing:
- Server responses (220, 250, 354, etc.)
- Authentication process (Part B only)
- Confirmation of successful email delivery