# 💰 Royal Traders - Python Trading App

**Royal Traders** is a client-server trading application developed in Python. It provides users with a secure and interactive interface to sign up, log in, view investment plans, and execute buy/sell operations. The app integrates live market data scraping, user account management, and database storage with MySQL.

---

## 📌 Features

- 🔐 **Login & Sign-Up System**
  - Secure user registration and login interface using Tkinter.
  - Credentials and user data are stored in a MySQL database.

- 🏠 **Homepage Navigation**
  - Investment Plans
  - Profile Information
  - Buy/Sell Operations

- 📊 **Investment Plans**
  - Real-time market data scraped from financial websites.
  - Displayed in a user-friendly format within the GUI.

- 👤 **User Profile**
  - View personal details and investment history retrieved from the database.

- 💹 **Buy/Sell Functionality**
  - Enter desired investment plan and amount.
  - Updates transaction records and user profile.

---

## 🛠️ Technologies & Libraries Used

- **Frontend:**
  - `Tkinter` – GUI creation
  - `PIL` – Image handling
  - `tkinter.messagebox` – Pop-up dialogs

- **Backend:**
  - `mysql-connector-python` – Communication with MySQL
  - `socket` – Client-server communication
  - `pickle` – Object serialization for data exchange

- **Web Data Fetching:**
  - `requests` – HTTP requests for real-time data
  - `bs4` (BeautifulSoup) – HTML parsing and web scraping

- **Others:**
  - `datetime` – Date and time operations
  - `random` – Generating mock data (optional)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/royal-traders.git
cd royal-traders
