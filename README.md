# README.md

## KomfiBot - Discord Image Generation Bot

Welcome to KomfiBot, a Discord Image Generation Bot based on the ComfyUI repository. This guide will walk you through the installation process and configuration for your own usage.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [watchdog](https://pypi.org/project/watchdog/)

### Installation Steps

1. **Install ComfyUI**

    Clone or download the ComfyUI repository:

    ```bash
    git clone https://github.com/comfyanonymous/ComfyUI.git
    ```

2. **Discord Developer**

    - [Create a Discord App](https://discord.com/developers/applications).
    - Gather the Bot Token.

3. **Set Intents**

    Set the [Privileged Intents](https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents) for your Discord Bot.

4. **Configuration Files**

    - `my_discord_bot.py`: Set the path to your Discord bot script.
    - `.env`: Create this file and add your Discord Bot Token:

        ```env
        DISCORD_TOKEN=your_bot_token
        ```

    - `workflow_api.json`: Define the locations and settings for your workflow.

5. **Files**

    - `workflow_api.json`
    - `.env`
    - `bot_api.py`
    - `bot.py`

### Configuration

1. **Define:**

    - Checkpoint file location
    - Workflow file location
    - Output folder location
    - Number of images per batch
    - ComfyUI enque script location
    - Discord App token to .env file

2. **Bot Configuration**

    Update the following variables in `my_discord_bot.py`:

    ```python
    BOT_SCRIPT_LOCATION = '/path/to/ComfyUI/bot_api.py'
    folder_path = '/path/to/ComfyUI/output/'
    ```

3. **Workflow Configuration**

    Update settings in `workflow_api.json`:

    ```json
    {
        "checkpoint_location": "/path/to/checkpoint",
        "workflow_location": "/path/to/workflow",
        "output_folder_location": "/path/to/output/folder",
        "num_images_per_batch": 4,
        "comfyui_enque_script_location": "/path/to/ComfyUI/bot_enque.py"
    }
    ```

### Todo/Planned Updates

- Move every user config variable to the json object.
- Clean up code and modularize it a bit.
- Flesh out this readme with more details.
- Introduce actual workflow configuration methodology.

### Additional Resources

- [ComfyUI API Guide](https://medium.com/@yushantripleseven/comfyui-using-the-api-261293aa055a)
- [ComfyUI Example Script](https://raw.githubusercontent.com/comfyanonymous/ComfyUI/master/script_examples/basic_api_example.py)
- [Discord Developer Portal](https://discord.com/developers/docs/topics/gateway#gateway-intents)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/latest/)
- [Discord.js Guide](https://discordjs.guide/creating-your-bot/slash-commands.html#individual-command-files)

For more advanced features, explore [ComfyUI Websockets API](https://medium.com/@yushantripleseven/comfyui-websockets-api-part-1-618175802d5a).

Feel free to reach out for any assistance!

---
