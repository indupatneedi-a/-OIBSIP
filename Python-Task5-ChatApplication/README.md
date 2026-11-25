# 💬 Chat Application

**OIBSIP / Python-Task5-ChatApplication**

A real-time, two-way chat application built with Python sockets and threading. One server relays messages between connected clients, and every message carries a timestamp. Built as part of the **Oasis Infobyte Student Internship Program (OIBSIP)**, Python Programming Track, **Task 5 (Beginner Tier)**.

---

## 📌 Objective

Build a messaging application in Python where two users can chat in real time. The project shows how a **client-server architecture** works: a central server accepts connections and passes each message on to the other connected clients.

---

## ✨ Features

- 🖥️ **Server script:** listens for incoming client connections
- 👤 **Client script:** connects to the server using a chosen name
- 🔄 **Real-time, two-way messaging:** both users can send and receive at the same time
- 🕒 **Timestamps:** every message is shown as `[HH:MM] Name: message`, for example `[14:35] Alice: Hello`
- 🔔 **Join and leave notices:** the other client is told when someone joins or disconnects
- 🚪 **Graceful exit:** type `/quit` to leave the chat cleanly
- 🛡️ **Error handling:** a friendly message if the client starts before the server
- 🏠 **Runs on localhost:** both scripts work on a single machine

---

## 🛠️ Tech Stack

| Item | Details |
|------|---------|
| Language | Python 3 |
| Modules | `socket`, `threading`, `datetime` (all built into Python) |
| External libraries | None needed |
| Interface | Command line |

---

## 📋 Requirements

- Python 3.6 or higher
- No extra packages to install, so there is no `requirements.txt` for this task

---

##LINK: https://lnkd.in/p/d-K65_mC

## 📁 Project Structure

```
OIBSIP/
└── Python-Task5-ChatApplication/
    ├── server.py        # Chat server
    ├── client.py        # Chat client
    ├── README.md        # Project documentation
    └── screenshots/     # Screenshots of the chat working
```

---

## 🚀 How to Run (on your own computer)

You need **three terminal windows**: one for the server and one for each client.

1. **Clone the repository:**

   ```
   git clone https://github.com/indupatneedi-a/OIBSIP.git
   cd OIBSIP/Python-Task5-ChatApplication
   ```

2. **Terminal 1: start the server first:**

   ```
   python server.py
   ```

   You will see: `Server listening on 127.0.0.1:5555`

3. **Terminal 2: start the first client:**

   ```
   python client.py
   ```

   Enter a name, for example `Alice`.

4. **Terminal 3: start the second client:**

   ```
   python client.py
   ```

   Enter another name, for example `Bob`.

5. **Chat!** Type a message in either client and press Enter. The other client sees it instantly.

6. Type `/quit` to leave. The other client is told that you left.

### Sample Chat

**Alice's window:**
```
Connected! Type a message and press Enter. Type /quit to leave.
[14:35] Bob joined the chat.
Hello Bob!
[14:35] Bob: Hi Alice! How are you?
I'm good, thanks!
[14:36] Bob left the chat.
```

**Bob's window:**
```
Connected! Type a message and press Enter. Type /quit to leave.
[14:35] Alice: Hello Bob!
Hi Alice! How are you?
[14:35] Alice: I'm good, thanks!
/quit
You left the chat.
---


##screenshots
<img width="1840" height="790" alt="02_imports_and_settings" src="https://github.com/user-attachments/assets/e65e1c6c-d8f6-43a0-8d73-b08604ddcc6a" />
<img width="1840" height="790" alt="05_start_server_output_proof" src="https://github.com/user-attachments/assets/ba003dc2-2aca-4649-88d3-e11971c9c4c9" />


