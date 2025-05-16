# TTS MCP Server (Kokoro)

A Model Context Protocol server that provides Text-to-Speech (TTS) capabilities using the Kokoro model.

### Available Tools

- `synthesize_speech` - Generates speech audio from text.
  - Required arguments:
    - `text` (string): The text to synthesize.
  - Optional arguments:
    - `voice` (string): The voice to use (e.g., 'af_heart'). Defaults might vary.
    - `lang_code` (string): The language code (e.g., 'a'). Defaults might vary.

## Installation

### Using uv (recommended)

```bash
# TBD - Need actual package name
uvx mcp-server-tts 
```

### Using PIP

```bash
# TBD - Need actual package name
pip install mcp-server-tts
```

After installation, you can run it as a script using:

```bash
python -m mcp_server_tts
```

## Configuration

*(Add configuration examples for Claude, Zed, VS Code similar to the time server, using `python -m mcp_server_tts`)*

## Example Interactions

```json
{
  "name": "synthesize_speech",
  "arguments": {
    "text": "Hello world, this is a test.",
    "voice": "af_heart"
  }
}
```
Response:
```json
{
  "audio_format": "wav",
  "audio_data_base64": "UklGRi...BASE64_ENCODED_WAV_DATA..."
}
```

## Development

*(Add development/debugging instructions)*

## License

*(Specify License)* 