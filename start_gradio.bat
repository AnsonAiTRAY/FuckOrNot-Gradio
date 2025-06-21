@echo off
echo Starting Gradio Image Rater...
echo.
echo Checking dependencies...
python -c "import gradio" 2>nul
if errorlevel 1 (
    echo Installing Gradio...
    python -m pip install gradio Pillow
    if errorlevel 1 (
        echo Failed to install dependencies!
        echo Please run manually: pip install gradio Pillow
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
)

echo Starting application...
echo Browser will open automatically at: http://localhost:7860
echo Press Ctrl+C to stop the application
echo.

python run_gradio.py

if errorlevel 1 (
    echo.
    echo Application failed to start!
    echo Possible causes:
    echo   1. Python version too old (need 3.8+)
    echo   2. Port 7860 is occupied
    echo   3. Network connection issues
    echo   4. Dependency conflicts
    echo.
    echo Solutions:
    echo   1. Update Python version
    echo   2. Restart computer
    echo   3. Check firewall settings
    echo   4. Reinstall dependencies
    echo.
)

pause