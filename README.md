# 🧨 Tuny-bot: The Ultimate Unity Discord Bot

Welcome to Tuny-bot, the powerful and feature-rich Discord bot created as part of a school project. Tuny-bot is designed to enhance your Discord server experience with a wide range of functionalities and commands.

## Key Features of Tuny-bot

Tuny-bot offers an extensive set of features to cater to your needs. While some features are still under development, the bot provides an impressive array of capabilities that include:

- **Interactive Commands**: Engage with Tuny-bot through interactive and user-friendly commands, making it easy to navigate and interact with the bot's functionalities.

- **Discord Integration**: Seamlessly integrate Tuny-bot into your Discord server, enabling it to interact with users, channels, and server events.

- **Customization**: Tailor Tuny-bot to your liking by configuring various settings and preferences. Personalize your bot's behavior and appearance to suit your server's unique style.

- **Fun and Entertainment**: Enjoy an assortment of fun features, including mini-games, trivia, and random generators. Tuny-bot ensures there's never a dull moment in your Discord server.

## 🛠️ Building Tuny-bot from Source

If you're interested in exploring the inner workings of Tuny-bot and building it from source, follow the steps below:

1. Clone the Tuny-bot repository to your local machine:
    ```
    git clone https://github.com/Arktic-py/TuniBot.git
    cd Tunibot
    ```

    Alternatively, you can download the bot as a zip file and extract it to your desired location.

2. Install the required dependencies using Python's package manager, pip:
    ```
    python -m pip install -r requirements.txt
    ```

    Please note that Tuny-bot requires Python 3.8 or a later version.

3. Configuration Setup:
    Create a `.env` file in the project directory and populate it with the necessary environment variables. See the `.env` section below for details.

4. Run Tuny-bot:
    Launch the main file, `bot.py`, to start Tuny-bot:
    ```
    python bot.py
    ```

    Tuny-bot is now up and running, ready to bring excitement and functionality to your Discord server!

## .env Configuration

Create a `.env` file in the project directory and add the following environment variables:

TOKEN=your_discord_bot_token_here
CHAT_API_ID=your_chat_api_id_here
CHAT_API_KEY=your_chat_api_key_here
FOX_API_URL=http://randomfox.ca/floof/