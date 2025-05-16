"""Allows the server to be run as a module using 'python -m mcp_server_tts'."""

import asyncio
from .server import main

if __name__ == "__main__":
    # Run the async main function using asyncio's event loop
    asyncio.run(main()) 