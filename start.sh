#!/bin/bash

echo "Starting Adrian Hsu's Personal Website..."
echo ""

cd "$(dirname "$0")"

# Setup backend venv with uv
echo "Setting up Python virtual environment with uv..."
cd backend
if [ ! -d ".venv" ]; then
    uv venv .venv
fi
source .venv/bin/activate
uv pip install -r requirements.txt --quiet

# Start Flask backend in background
echo "Starting Flask backend on http://localhost:5001..."
.venv/bin/python app.py &
BACKEND_PID=$!

# Wait for backend to start
sleep 2

# Start frontend server
cd ../frontend
echo "Starting frontend on http://localhost:8080..."
echo ""
echo "==================================="
echo "Website is running!"
echo "Open http://localhost:8080 in your browser"
echo "Press Ctrl+C to stop all servers"
echo "==================================="
echo ""

python3 -m http.server 8080 &
FRONTEND_PID=$!

# Handle cleanup on exit
cleanup() {
    echo ""
    echo "Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Wait for both processes
wait
