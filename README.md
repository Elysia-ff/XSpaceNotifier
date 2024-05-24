# Dependency  
- `discord.py`  
- `twspace_dl`  

# Installation  
1. Open `XNotifier.py`  
2. Replace `USER_URL` and `USER_NAME` with what you want.  
3. Create a file that contains your login cookie ***(netscape format)*** for X, name it `cookie.co`.  ([useful chrome extension](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm))  
4. Create a file named `discord.auth`.  
   ```
   <your discord bot token>
   <twitter url> <displayName> <channelID>
   <twitter url> <displayName> <channelID>
   ...
   ```
5. `XNotifier.py` will send a message to `<channelID>` if `<twitter url>` turns on Space.  
6. Run `python XNotifier.py`  
