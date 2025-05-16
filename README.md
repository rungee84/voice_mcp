# Interactive Voice MCP Server (Kokoro TTS + NeMo ASR)

A Model Context Protocol server that provides Text-to-Speech (TTS) capabilities using Kokoro and Speech-to-Text (STT) capabilities using NVIDIA NeMo Parakeet models, enabling interactive voice dialogues.

### Available Tools

- `interactive_voice_dialog` - Synthesizes text to speech, plays it, then listens for user speech input and returns the transcription.
  - Required arguments:
    - `text_to_speak` (string): The text for the assistant to speak.
  - Optional arguments:
    - `voice` (string): The voice to use for TTS (e.g., 'af_heart'). Defaults to 'af_heart'.

## Installation

### Prerequisites

Some of the underlying TTS models require `espeak-ng` to be installed on your system.

**Windows Installation:**
1. Go to [espeak-ng releases](https://github.com/espeak-ng/espeak-ng/releases).
2. Click on "Latest release".
3. Download the appropriate `*.msi` file (e.g. `espeak-ng-20191129-b702b03-x64.msi`).
4. Run the downloaded installer.

### Local Development Installation

To allow Claude Desktop to launch this server using `python -m mcp_server_tts`, you need to install it as a Python module. Installing in "editable" mode (`-e`) is recommended for development, as it means changes to the source code are reflected immediately without needing to reinstall.

Navigate to the directory containing the `pyproject.toml` file (the root of this server project) and run:
```bash
pip install -e .
```

After installation, you can run it as a script using:

```bash
python -m mcp_server_tts.server # Assuming the main module is still server.py within mcp_server_tts
# Or, if you create a new package structure:
# python -m mcp_interactive_voice_server
```

## Configuration

To use this server with Claude Desktop, you need to add it to your `claude_desktop_config.json` file.
The location of this file is typically: `C:\Users\<YourUsername>\AppData\Roaming\Claude\claude_desktop_config.json`

Add the following entry under the `mcpServers` object in your `claude_desktop_config.json`:

```json
    "tts": {
      "command": "python",
      "args": ["-m", "mcp_server_tts"]
    }
```

For example, your `mcpServers` section might look like this:
```json
{
  // ... other configurations ...
  "mcpServers": {
    // ... other servers ...
    "tts": {
      "command": "python",
      "args": ["-m", "mcp_server_tts"]
    }
    // ... other servers ...
  }
  // ... other configurations ...
}
```
