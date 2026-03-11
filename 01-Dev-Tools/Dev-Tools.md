# Dev Tools

* jq, yq, xq
  * Install in Windows (using PowerShell)
    * `winget install jqlang.jq`
    * Install Python if not already
        * `winget install Python.Python.3`
    * `pip install yq`
    * Add installed Python Scripts location to PATH
      * `setx PATH "$env:PATH;$env:APPDATA\Python\Python313\Scripts"`
        * This adds location `C:\Users\Shaun\AppData\Roaming\Python\Python313\Scripts`
      * Usually there is a limit of 1024 characters in PATH that can be from PowerShell. If so, add manually by Windows Explorer user environment prompt.
        * `C:\Users\Shaun\AppData\Roaming\Python\Python313\Scripts`