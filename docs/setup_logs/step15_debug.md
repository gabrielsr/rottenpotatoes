Ref.: https://code.visualstudio.com/docs/python/tutorial-flask


Instsall Edge DevTools

# Create launch.json
Create Flask Launch

```Python
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "vscode-edge-devtools.debug",
            "request": "launch",
            "name": "Launch Microsoft Edge and open the Edge DevTools",
            "url": "http://127.0.0.1:5000",
            "webRoot": "${workspaceFolder}"
        },
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app/webapp",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        },
    ],
    "compounds": [
        {
            "name": "Flask and Edge",
            "configurations": [
                "Python: Flask",
                "Launch Microsoft Edge and open the Edge DevTools"
            ]
        }
    ]
}
```


# Run

Crtl+Shift + D and F5
Open MS Edge Tools Menu and Launch 