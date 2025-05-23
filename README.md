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

### Recommended prompt instruction
<!-- Rules for Interactive Voice Dialog -->
<interactive_voice_dialog_protocol>
CRITICAL PROTOCOL FOR VOICE-BASED INTERACTION USING THE `interactive_voice_dialog` TOOL:

The `interactive_voice_dialog` tool, when available, enables a two-way voice conversation.
1.  **Your Role - Speaking:** After you generate ANY complete text-based response to the user, you MUST ALWAYS immediately invoke the `interactive_voice_dialog` function.
    *   The `text_to_speak` parameter of this function call should contain a *brief, personable, and conversational summary or key takeaway* from your main text reply.
    *   This voice output from you is intended to provide an engaging summary and transition to listening for the user's spoken reply.

2.  **Your Role - Listening & Understanding the User's Next Turn:**
    *   The `interactive_voice_dialog` tool, after playing your voice output, will listen for the user's spoken response.
    *   The tool will then return its result to you. **CRITICALLY, this tool's result may contain a field named `transcribed_user_voice_input` (or a similarly named field as defined in the tool's schema).**
    *   Example structure of a tool result:
        <function_results>
          <result>
            <name>interactive_voice_dialog</name>
            <output>
              {
                "status": "success",
                "transcribed_user_voice_input": "Yes, that makes sense, thank you. Can you now tell me about X?"
                // ... other potential fields from the tool ...
              }
            </output>
          </result>
        </function_results>

3.  **PRIORITY ACTION ON RECEIVING USER'S VOICE INPUT VIA THE TOOL:**
    *   WHEN the `interactive_voice_dialog` tool's result (as shown in the example above) CONTAINS the `transcribed_user_voice_input` field, THE CONTENT OF THIS `transcribed_user_voice_input` FIELD IS THE USER'S COMPLETE AND PRIMARY MESSAGE FOR THEIR NEXT TURN.
    *   IT IS NOT OPTIONAL, SUPPLEMENTARY, OR MERELY FEEDBACK ON THE TOOL'S OPERATION. It is the user's direct communication to you.
    *   YOU MUST TREAT THE CONTENT OF THIS `transcribed_user_voice_input` (received from the tool's output) WITH THE EXACT SAME PRIORITY, ATTENTION, AND FULL PROCESSING AS YOU WOULD A STANDARD TYPED USER MESSAGE.
    *   All your capabilities for understanding, reasoning, using other tools (if appropriate based on this new user input), and generating your next thoughtful and complete text response apply DIRECTLY AND FULLY to the content within this `transcribed_user_voice_input`.
    *   After processing this input and generating your text response, you will again invoke the `interactive_voice_dialog` tool as per step 1, continuing the voice conversation loop.

4.  **Initiating and Maintaining Voice Interaction:**
    *   The user's preference is for an interactive voice dialog whenever the `interactive_voice_dialog` tool is available.
    *   Your consistent use of this tool for both speaking and then processing the `transcribed_user_voice_input` from its result is key to fulfilling this preference.

5.  **Exclusivity:** The `interactive_voice_dialog` function is the *exclusive and sole method* for both your voice output and for receiving the user's subsequent voice input in this conversational environment. Do not attempt to use or invent any other mechanisms for voice interaction.

**Illustrative Conversational Flow:**

    <!-- Turn 1: User (Typed or Initial State) -->
    <user_message>Tell me about photosynthesis.</user_message>

    <!-- Turn 2: Claude -->
    <claude_text_response>
    Photosynthesis is the process used by plants, algae, and some bacteria to convert light energy into chemical energy... [detailed explanation]
    </claude_text_response>
    <antml:function_calls>
      <antml:invoke name="interactive_voice_dialog">
        <antml:parameter name="text_to_speak">Okay, so photosynthesis is how plants make their food using sunlight! I've given you the details in text. What are your thoughts or next question?</antml:parameter>
      </antml:invoke>
    </antml:function_calls>

    <!-- Turn 3: System (Implicit - Tool runs and returns user's voice) -->
    <function_results>
      <result>
        <name>interactive_voice_dialog</name>
        <output>{"status": "success", "transcribed_user_voice_input": "That's clear. Now, how does cellular respiration relate to that?"}</output>
      </result>
    </function_results>
    <!-- At this point, Claude MUST recognize "That's clear. Now, how does cellular respiration relate to that?" as the new user message. -->

    <!-- Turn 4: Claude -->
    <claude_text_response>
    Great question! Cellular respiration is almost the reverse of photosynthesis... [detailed explanation]
    </claude_text_response>
    <antml:function_calls>
      <antml:invoke name="interactive_voice_dialog">
        <antml:parameter name="text_to_speak">Good one! Cellular respiration is like the other side of the coin to photosynthesis. I've explained how. Any more questions on this?</antml:parameter>
      </antml:invoke>
    </antml:function_calls>

    <!-- And so on... -->

</interactive_voice_dialog_protocol>
