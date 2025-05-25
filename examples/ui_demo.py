#!/usr/bin/env python3
"""
TubeHarvest UI Demo
Demonstrates the beautiful console interface without downloading.
"""

import sys
import os
import time

# Add the parent directory to the Python path so we can import tubeharvest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tubeharvest.ui.console import ui

def demo_banner():
    """Demo the banner display."""
    ui.display_banner()
    time.sleep(2)

def demo_welcome():
    """Demo the welcome information."""
    ui.show_welcome_info()
    time.sleep(3)

def demo_messages():
    """Demo various message types."""
    ui.console.print("\n[bold yellow]📢 Message Types Demo[/]\n")
    
    ui.show_success("This is a success message!")
    time.sleep(1)
    
    ui.show_info("This is an info message!")
    time.sleep(1)
    
    ui.show_warning("This is a warning message!")
    time.sleep(1)
    
    ui.show_error("This is an error message!")
    time.sleep(2)

def demo_video_info():
    """Demo video information display."""
    ui.console.print("\n[bold yellow]🎬 Video Info Demo[/]\n")
    
    # Mock video info
    mock_video_info = {
        'title': 'Amazing YouTube Video - Full HD Quality',
        'uploader': 'TechChannel',
        'duration': 1245,  # 20:45
        'view_count': 1234567,
        'upload_date': '20231215'
    }
    
    ui.show_video_info(mock_video_info)
    time.sleep(3)

def demo_config_summary():
    """Demo configuration summary."""
    ui.console.print("\n[bold yellow]⚙️ Configuration Demo[/]\n")
    
    mock_config = {
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'output_dir': 'downloads',
        'format': 'mp4',
        'quality': '1080',
        'audio_only': False,
        'video_only': False,
        'subtitles': True,
        'metadata': True,
        'filename': 'my_video',
        'workers': 4
    }
    
    ui.show_config_summary(mock_config)
    time.sleep(3)

def demo_progress():
    """Demo progress tracking."""
    ui.console.print("\n[bold yellow]📊 Progress Demo[/]\n")
    
    ui.start_download_session()
    
    with ui.create_download_progress() as progress:
        # Simulate multiple downloads
        tasks = [
            ui.add_download_task("🎬 Video 1 - Introduction", total=100),
            ui.add_download_task("🎬 Video 2 - Tutorial", total=100),
            ui.add_download_task("🎬 Video 3 - Advanced Tips", total=100)
        ]
        
        # Simulate progress
        for i in range(101):
            for task_id in tasks:
                ui.update_download_task(task_id, completed=i)
            time.sleep(0.02)
    
    time.sleep(1)

def demo_stats():
    """Demo download statistics."""
    ui.console.print("\n[bold yellow]📈 Statistics Demo[/]\n")
    
    ui.show_download_stats(
        total_downloads=3,
        failed_downloads=0,
        total_size="156.7 MB"
    )
    time.sleep(3)

def main():
    """Run the complete demo."""
    try:
        ui.console.print("[bold green]🎭 TubeHarvest UI Demo Starting...[/]\n")
        time.sleep(1)
        
        demo_banner()
        demo_welcome()
        demo_messages()
        demo_video_info()
        demo_config_summary()
        demo_progress()
        demo_stats()
        
        ui.goodbye_message()
        
    except KeyboardInterrupt:
        ui.console.print("\n[yellow]Demo interrupted by user.[/]")
    except Exception as e:
        ui.console.print(f"\n[red]Demo error: {e}[/]")

if __name__ == "__main__":
    main() 