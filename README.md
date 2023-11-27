
### Description of Key Components

- `main.py`: The starting point of the application, orchestrating the prediction bot's operations.
- `config.py`: Contains configuration variables such as API keys and contract addresses.
- `requirements.txt`: Lists all the necessary Python packages for the project.
- `.gitignore`: Defines files and directories to be ignored by version control.
- `README.md`: Offers a detailed explanation of the project, setup instructions, and usage guide.

#### Modules Directory

- `common`: Houses modules for functions that are shared across different platforms, like price fetching and wallet interactions.
- `platforms`: Contains platform-specific modules, such as those for PancakeSwap and Dogebets.
- `prediction.py`: Implements the prediction logic of the bot.
- `round_monitor.py`: Monitors and interacts with the betting rounds on the platforms.

#### Tests Directory

- Includes test scripts for each module, ensuring functionality and reliability.
