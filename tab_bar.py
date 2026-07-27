# ~/.config/kitty/tab_bar.py

import psutil
from kitty.fast_data_types import Screen, get_boss
from kitty.tab_bar import DrawData, ExtraData, TabBarData, draw_title

def get_process_memory(pid: int) -> str: 
    try:
        parent = psutil.Process(pid)
        total_mem = parent.memory_info().rss

        for child in parent.children(recursive=True):
            try:
                total_mem += child.memory_info().rss
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # convert bytes to megabytes
        mem_mb = total_mem / (1024 * 1024)

        # convert megabytes to gigabytes
        if mem_mb >= 1024:
            return f"{mem_mb / 1024:.1f}gb"
        return f"{int(mem_mb)}mb"
    except Exception:
        return "?"

def draw_tab(
        draw_data: DrawData,
        screen: Screen, 
        tab: TabBarData,
        before: int,
        max_title_length: int, 
        index: int, 
        is_last: bool,
        extra_data: ExtraData,
) -> int: # this function is called by kitty whenever a new tab is opened

    if extra_data.for_layout:
        return draw_title(draw_data, screen, tab, index)
    
    # draw standard tab title first
    end_point = draw_title(draw_data, screen, tab, index)

    # get process memory usage
    mem_str = ""
    try: 
        boss = get_boss()
        if boss:
            tab_obj = boss.tab_for_id(tab.tab_id)
            if tab_obj and tab_obj.active_window and tab_obj.active_window.child:
                pid = tab_obj.active_window.child.pid
                mem_usage = get_process_memory(pid)
                mem_str = f"[{mem_usage}]"
    except Exception as e:
        mem_str = " [ERR]"

    screen.draw(mem_str)

    return screen.cursor.x
