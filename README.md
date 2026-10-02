# Replay Attack Simulation — Python Socket Programming

A simple educational cybersecurity project that demonstrates a **Replay Attack** using Python TCP socket programming.

This project was created for a cybersecurity assignment and runs entirely on the local computer using `127.0.0.1`.

---

## 📌 Project Overview

A Replay Attack occurs when an attacker captures a legitimate message and later sends the same message again.

In this project, the attacker is simulated by reusing a previously valid message:

```text
ACCESS|student01|NETWORK_LAB
```

The server accepts the message during normal communication.

The attacker then sends the exact same message again.

Because the demonstration server does not implement replay protection such as timestamps, nonces, or sequence numbers, it accepts the replayed message again.

---

## 🎯 Learning Objectives

This project demonstrates:

* TCP client-server communication
* Python socket programming
* Normal client-server communication
* The basic concept of a Replay Attack
* Why replay attacks can occur
* The security weakness caused by missing freshness validation
* Basic replay-attack prevention techniques

---

## 🗂️ Project Structure

```text
replay-attack-demo/
│
├── server.py
├── client.py
├── attack.py
└── README.md
```

### `server.py`

Runs the TCP server and processes incoming requests.

### `client.py`

Acts as the legitimate client and communicates with the server.

### `attack.py`

Simulates an attacker replaying a previously captured valid message.

### `README.md`

Contains project documentation and instructions.

---

## ⚙️ Requirements

* Python 3.x
* A computer running Windows, Linux, or macOS
* No external Python packages are required

Check your Python installation:

```bash
python --version
```

---

## 🌐 Network Configuration

The application uses localhost:

```text
HOST = 127.0.0.1
PORT = 5000
```

This means the demonstration takes place entirely on the local computer.

No external network or third-party system is required.

---

# 🚀 How to Run

## Step 1 — Start the Server

Open Terminal 1 and run:

```bash
python server.py
```

Expected output:

```text
===================================
       REPLAY ATTACK LAB
===================================
[SERVER] Listening on 127.0.0.1:5000
[SERVER] Waiting for clients...
```

---

## Step 2 — Start the Normal Client

Open Terminal 2:

```bash
python client.py
```

Enter the following message:

```text
ACCESS|student01|NETWORK_LAB
```

The server should respond:

```text
ACCESS GRANTED
```

This demonstrates normal client-server communication.

When finished, type:

```text
exit
```

---

# 🔁 Step 3 — Run the Replay Attack

Open Terminal 3:

```bash
python attack.py
```

The attack program contains a previously captured valid message:

```text
ACCESS|student01|NETWORK_LAB
```

It sends this exact message to the server again.

The server responds:

```text
ACCESS GRANTED
```

This demonstrates the Replay Attack.

---

# 🔍 How the Attack Works

Normal communication:

```text
LEGITIMATE CLIENT
       |
       | ACCESS|student01|NETWORK_LAB
       ↓
     SERVER
       |
       | ACCESS GRANTED
       ↓
     CLIENT
```

After the message has been captured, the attacker reuses it:

```text
ATTACKER
       |
       | ACCESS|student01|NETWORK_LAB
       ↓
     SERVER
       |
       | ACCESS GRANTED
       ↓
   ATTACKER
```

The important point is that the attacker sends the **same previously valid message**.

---

# ⚠️ Why Does the Attack Work?

The demonstration server does not check whether a request is fresh.

It does not use:

* Nonces
* Timestamps
* Sequence numbers
* Unique request IDs
* Replay detection

Therefore, the server cannot distinguish between:

```text
New legitimate request
```

and:

```text
Previously valid request being replayed
```

---

# 🛡️ How Can Replay Attacks Be Prevented?

Several security mechanisms can reduce or prevent replay attacks.

## 1. Nonce

A unique random value can be included with each request.

The server rejects a nonce that has already been used.

## 2. Timestamp

A timestamp can be included in the request.

The server rejects requests that are outside an acceptable time window.

## 3. Sequence Number

Requests can contain increasing sequence numbers.

Old or repeated sequence numbers can be rejected.

## 4. Unique Request ID

Each request can have a unique identifier.

The server can keep track of recently processed IDs.

## 5. Cryptographic Authentication

MACs or digital signatures can authenticate messages. In practice, authentication should be combined with freshness mechanisms such as nonces or sequence numbers to prevent valid messages from simply being reused.

---

# 🔐 Security Property

The demonstration focuses on the protection of **message freshness** and preventing the unauthorized reuse of a previously valid request.

Depending on the real application, replaying a message could also lead to unauthorized repeated actions or affect the integrity of operations.

---

# 🎓 Educational Scope

This project is designed for educational use.

The attack is demonstrated only against a locally running application:

```text
127.0.0.1
```

The `attack.py` program simulates the attacker already having a captured message. It does not perform network sniffing or interception of other users' traffic.

---

# 📹 Assignment Demonstration

The video demonstration follows these steps:

1. Explain what a Replay Attack is.
2. Explain the project architecture.
3. Explain `server.py`.
4. Explain `client.py`.
5. Explain `attack.py`.
6. Start the server.
7. Demonstrate normal client-server communication.
8. Stop/disconnect the normal client.
9. Run the attack program.
10. Show that the previously valid message is accepted again.
11. Explain why the replay works.
12. Explain the affected security property.
13. Explain prevention techniques.
14. Conclude the demonstration.

---

# 📚 Example Message

The legitimate request used in this demonstration is:

```text
ACCESS|student01|NETWORK_LAB
```

The attacker reuses the exact same request:

```text
ACCESS|student01|NETWORK_LAB
```

No modification is necessary for the replay.

---

# 👨‍💻 Technologies Used

* Python 3
* TCP/IP
* Python `socket` module
* Localhost networking

---

# ⚠️ Disclaimer

This project is intended for cybersecurity education and authorized laboratory environments.

The demonstration should only be performed against systems that you own or have explicit permission to test.

---

## Author

**Cybersecurity Assignment — Replay Attack Simulation**

Built for educational purposes using Python socket programming.
