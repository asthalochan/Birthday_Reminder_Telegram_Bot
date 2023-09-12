# Telegram Birthday Reminder Bot

## Overview

This repository contains a Telegram Bot that serves as a Birthday Reminder. The bot is built using Python and utilizes the Telegram Bot API. It allows users to store and receive birthday reminders for themselves and their friends.

## Features

- **Birthday Storage:** Users can send their name and birthday date to the bot, which will store this information in its SQLite3 database.

- **Automatic Reminders:** The bot automatically sends birthday reminder messages to users on their specified birthdays.

- **AWS Deployment:** The bot has been successfully deployed on the AWS cloud for testing and usage.

## Getting Started

### Prerequisites

To run this bot, you will need:

- Python 3.x
- A Telegram Bot Father token (you can obtain this by creating a bot on Telegram Bot Father)

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/asthalochan/Birthday_reminder_Telegram_bot.git
   ```

2. Install the required Python packages.

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Obtain a Telegram Bot Father token by creating a new bot on Telegram.

2. Create a `.env` file in the project directory and add your Bot Father token as follows:

   ```env
   TELEGRAM_API_TOKEN=your_token_here
   ```

### Usage

1. Run the bot by executing the following command:

   ```bash
   python bot.py
   ```

2. Start a conversation with the bot on Telegram, and you can use the following commands:

   - `/start`: Start the bot and get instructions.
   - `/new`: Set your birthday.
   - `/list_birthdays`: List all stored birthdays.
   - `/delete`: Delete your birthday.
   - `/dev`: Get developers Detail.

3. The bot will automatically send birthday reminders to users on their specified birthdays.

## Deployment

This bot has been deployed on the AWS cloud for testing and usage. You can follow a similar deployment process to make it accessible to a wider audience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Telegram Bot API for making it easy to create Telegram bots.
- Special thanks to the AWS cloud for providing a reliable hosting environment for testing.

---

Feel free to modify and expand upon this README to provide more details about your project, such as the project structure, additional setup steps, and usage examples.
