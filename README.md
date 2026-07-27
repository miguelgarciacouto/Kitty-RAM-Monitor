 # Kitty Tab RAM Monitor                                                                                                                                
        
A lightweight extension for the [Kitty Terminal](https://github.com/kovidgoyal/kitty) that allows you to check the RAM usage from each used tab currently open the terminal!                                                                                                                                        
                                                                                                                                                        
## Usage                                                                                                                                                

A lot of Linux users use the terminal to open GUI apps, servers, build tools, allowing you to have live logs, for example. Keeping track of system resources consumption usually requires opening a separate system monitor (such as 'htop', 'KDE System Monitor' etc)                                                  
## How to install it                                                                                                                                        
1. Clone this repository or copy `tab_bar.py` into your kitty config directory:                                                                             
```bash                                                                                                                                                 
cp tab_bar.py ~/.config/kitty/tab_bar.py                                                                                                                
```

2. Ensure that psutil is installed on your Python environment                                                                                           

3. Enable the custom tab bar rendering in '~/.config/kitty/kitty.conf'                                                                                      
```                                                                                                                                                 
tab_bar_style custom                                                                                                                                    
# add this to the bottom of your conf file                                                                                                              
```                                                                                                                                                     
4. Restart Kitty to apply the changes                                                                                                                        
