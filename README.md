# Dependency  
- `discord.py`  
- `twspace_dl`  

# Installation  
1. Create a file that contains your login cookie ***(netscape format)*** for X, name it `cookie.co`.  ([useful chrome extension](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm))  
2. Create a file named `discord.auth`.  
   ```
   <your discord bot token>
   <twitter url> <displayName> <channelID>
   <twitter url> <displayName> <channelID>
   ...
   ```
3. `XNotifier.py` will send a message to `<channelID>` if `<twitter url>` turns on Space.  
4. Run `python XNotifier.py`  
