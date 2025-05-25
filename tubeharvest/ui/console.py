"""
Enhanced UI module for TubeHarvest - Beautiful and interactive console interface.
"""

import os
import sys
import time
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    Progress,
    TaskID,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn,
    SpinnerColumn,
)
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.columns import Columns
from rich.rule import Rule
from rich.markdown import Markdown
from rich.tree import Tree
from rich.syntax import Syntax
from rich import box
import inquirer
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

# Initialize Rich console
console = Console()


class TubeHarvestUI:
    """Enhanced UI class for TubeHarvest with rich interactive features."""

    def __init__(self):
        self.console = console
        self.start_time = None
        self.progress = None
        self.current_downloads = {}

    def display_banner(self):
        """Display the enhanced TubeHarvest banner with rich styling."""
        banner_text = """
 ████████╗██╗   ██╗██████╗ ███████╗    ██╗  ██╗ █████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
 ╚══██╔══╝██║   ██║██╔══██╗██╔════╝    ██║  ██║██╔══██╗██╔══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
    ██║   ██║   ██║██████╔╝█████╗      ███████║███████║██████╔╝██║   ██║█████╗  ███████╗   ██║   
    ██║   ██║   ██║██╔══██╗██╔══╝      ██╔══██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ╚════██║   ██║   
    ██║   ╚██████╔╝██████╔╝███████╗    ██║  ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████║   ██║   
    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝   ╚═╝   
        """

        subtitle = "🎬 YouTube Downloader with Superpowers 🎬"
        version = "v2.0 - Enhanced Interactive Console"

        banner_panel = Panel(
            Align.center(
                Text(banner_text, style="bold blue gradient")
                + "\n"
                + Text(subtitle, style="bold green")
                + "\n"
                + Text(version, style="italic cyan")
            ),
            border_style="bright_blue",
            box=box.DOUBLE,
            padding=(1, 2),
        )

        self.console.print(banner_panel)
        self.console.print()

    def show_welcome_info(self):
        """Display welcome information and features."""
        features = [
            "✨ Beautiful interactive console interface",
            "🚀 Fast concurrent downloads",
            "📺 Support for videos and playlists",
            "🎵 Audio/video format options",
            "📊 Real-time progress tracking",
            "📝 Metadata and subtitle support",
            "🎯 Quality selection",
            "💾 Resume interrupted downloads",
        ]

        info_table = Table(box=box.ROUNDED, border_style="green")
        info_table.add_column("🌟 Features", style="cyan", no_wrap=True)

        for feature in features:
            info_table.add_row(feature)

        self.console.print(
            Panel(
                info_table,
                title="[bold green]Welcome to TubeHarvest[/]",
                border_style="green",
            )
        )
        self.console.print()

    def interactive_setup(self) -> Dict[str, Any]:
        """Interactive setup wizard for download options."""
        self.console.print(
            "[bold yellow]📋 Let's configure your download settings![/]\n"
        )

        questions = [
            inquirer.Text(
                "url",
                message="🔗 Enter YouTube URL (video or playlist)",
                validate=lambda _, x: len(x.strip()) > 0,
            ),
            inquirer.Path(
                "output_dir",
                message="📁 Output directory",
                default="downloads",
                path_type=inquirer.Path.DIRECTORY,
            ),
            inquirer.List(
                "format",
                message="📹 Choose output format",
                choices=["mp4", "mp3", "webm", "mkv", "m4a"],
                default="mp4",
            ),
            inquirer.List(
                "quality",
                message="🎯 Select quality",
                choices=["best", "1080p", "720p", "480p", "360p", "240p"],
                default="best",
            ),
            inquirer.List(
                "download_type",
                message="🎬 What to download?",
                choices=[
                    ("Video + Audio (default)", "both"),
                    ("Audio only", "audio"),
                    ("Video only", "video"),
                ],
                default="both",
            ),
            inquirer.Confirm(
                "subtitles", message="📝 Download subtitles?", default=False
            ),
            inquirer.Confirm("metadata", message="📊 Save metadata?", default=False),
            inquirer.Text(
                "filename",
                message="📄 Custom filename (optional, leave empty for auto)",
                default="",
            ),
            inquirer.Text(
                "workers",
                message="⚡ Number of workers for concurrent downloads",
                default="4",
                validate=lambda _, x: x.isdigit() and int(x) > 0,
            ),
        ]

        try:
            answers = inquirer.prompt(questions)
            if answers is None:
                self.console.print("[red]❌ Setup cancelled.[/]")
                sys.exit(0)

            # Process answers
            config = {
                "url": answers["url"].strip(),
                "output_dir": answers["output_dir"],
                "format": answers["format"],
                "quality": (
                    answers["quality"].replace("p", "")
                    if answers["quality"] != "best"
                    else "best"
                ),
                "audio_only": answers["download_type"] == "audio",
                "video_only": answers["download_type"] == "video",
                "subtitles": answers["subtitles"],
                "metadata": answers["metadata"],
                "filename": (
                    answers["filename"].strip() if answers["filename"].strip() else None
                ),
                "workers": int(answers["workers"]),
            }

            return config

        except KeyboardInterrupt:
            self.console.print("\n[red]❌ Setup interrupted by user.[/]")
            sys.exit(0)
        except Exception as e:
            self.console.print(f"[red]❌ Error during setup: {str(e)}[/]")
            sys.exit(1)

    def show_config_summary(self, config: Dict[str, Any]):
        """Display a beautiful summary of the configuration."""
        summary_table = Table(box=box.ROUNDED, border_style="blue")
        summary_table.add_column("Setting", style="cyan", no_wrap=True)
        summary_table.add_column("Value", style="white")

        # Format URL for display (truncate if too long)
        url_display = config["url"]
        if len(url_display) > 60:
            url_display = url_display[:57] + "..."

        summary_table.add_row("🔗 URL", url_display)
        summary_table.add_row("📁 Output Directory", config["output_dir"])
        summary_table.add_row("📹 Format", config["format"].upper())
        summary_table.add_row("🎯 Quality", config["quality"])

        download_type = "Video + Audio"
        if config["audio_only"]:
            download_type = "Audio Only"
        elif config["video_only"]:
            download_type = "Video Only"
        summary_table.add_row("🎬 Type", download_type)

        summary_table.add_row(
            "📝 Subtitles", "✅ Yes" if config["subtitles"] else "❌ No"
        )
        summary_table.add_row(
            "📊 Metadata", "✅ Yes" if config["metadata"] else "❌ No"
        )

        if config["filename"]:
            summary_table.add_row("📄 Custom Filename", config["filename"])

        summary_table.add_row("⚡ Workers", str(config["workers"]))

        panel = Panel(
            summary_table,
            title="[bold blue]📋 Download Configuration[/]",
            border_style="blue",
        )

        self.console.print(panel)
        self.console.print()

    def confirm_download(self) -> bool:
        """Ask user to confirm the download."""
        questions = [
            inquirer.Confirm(
                "proceed",
                message="🚀 Start download with these settings?",
                default=True,
            )
        ]

        try:
            answers = inquirer.prompt(questions)
            return answers["proceed"] if answers else False
        except KeyboardInterrupt:
            return False

    def create_download_progress(self) -> Progress:
        """Create a rich progress display for downloads."""
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=40),
            "[progress.percentage]{task.percentage:>3.1f}%",
            "•",
            DownloadColumn(),
            "•",
            TransferSpeedColumn(),
            "•",
            TimeRemainingColumn(),
            console=self.console,
            expand=True,
        )
        return self.progress

    def start_download_session(self):
        """Start a download session with timing."""
        self.start_time = time.time()
        self.console.print(
            Rule(title="[bold green]🚀 Starting Download Session[/]", style="green")
        )
        self.console.print()

    def add_download_task(
        self, description: str, total: Optional[int] = None
    ) -> TaskID:
        """Add a new download task to the progress display."""
        if self.progress:
            return self.progress.add_task(description, total=total)
        return None

    def update_download_task(self, task_id: TaskID, advance: int = None, **kwargs):
        """Update a download task progress."""
        if self.progress and task_id is not None:
            if advance:
                self.progress.update(task_id, advance=advance, **kwargs)
            else:
                self.progress.update(task_id, **kwargs)

    def complete_download_task(self, task_id: TaskID):
        """Mark a download task as completed."""
        if self.progress and task_id is not None:
            self.progress.update(task_id, completed=True)

    def show_download_stats(
        self, total_downloads: int, failed_downloads: int, total_size: str = "Unknown"
    ):
        """Display download statistics."""
        elapsed_time = time.time() - self.start_time if self.start_time else 0
        elapsed_str = f"{elapsed_time:.1f}s"

        stats_table = Table(box=box.ROUNDED, border_style="green")
        stats_table.add_column("Statistic", style="cyan")
        stats_table.add_column("Value", style="white")

        stats_table.add_row("✅ Successful Downloads", str(total_downloads))
        stats_table.add_row("❌ Failed Downloads", str(failed_downloads))
        stats_table.add_row("📊 Total Size", total_size)
        stats_table.add_row("⏱️ Total Time", elapsed_str)

        success_rate = (
            (total_downloads / (total_downloads + failed_downloads) * 100)
            if (total_downloads + failed_downloads) > 0
            else 0
        )
        stats_table.add_row("📈 Success Rate", f"{success_rate:.1f}%")

        panel = Panel(
            stats_table,
            title="[bold green]📊 Download Complete[/]",
            border_style="green",
        )

        self.console.print(Rule(style="green"))
        self.console.print(panel)

    def show_success(self, message: str):
        """Display a success message."""
        self.console.print(f"[green]✅ {message}[/]")

    def show_error(self, message: str):
        """Display an error message."""
        self.console.print(f"[red]❌ {message}[/]")

    def show_warning(self, message: str):
        """Display a warning message."""
        self.console.print(f"[yellow]⚠️ {message}[/]")

    def show_info(self, message: str):
        """Display an info message."""
        self.console.print(f"[cyan]ℹ️ {message}[/]")

    def show_video_info(self, video_info: Dict[str, Any]):
        """Display beautiful video information."""
        info_table = Table(box=box.ROUNDED, border_style="blue")
        info_table.add_column("Property", style="cyan", no_wrap=True)
        info_table.add_column("Value", style="white")

        title = video_info.get("title", "Unknown")
        if len(title) > 60:
            title = title[:57] + "..."
        info_table.add_row("🎬 Title", title)

        uploader = video_info.get("uploader", "Unknown")
        info_table.add_row("👤 Uploader", uploader)

        duration = video_info.get("duration")
        if duration:
            mins, secs = divmod(duration, 60)
            info_table.add_row("⏰ Duration", f"{int(mins):02d}:{int(secs):02d}")

        view_count = video_info.get("view_count")
        if view_count:
            info_table.add_row("👀 Views", f"{view_count:,}")

        upload_date = video_info.get("upload_date")
        if upload_date:
            # Convert YYYYMMDD to readable format
            try:
                date_obj = datetime.strptime(upload_date, "%Y%m%d")
                info_table.add_row("📅 Upload Date", date_obj.strftime("%B %d, %Y"))
            except:
                info_table.add_row("📅 Upload Date", upload_date)

        panel = Panel(
            info_table, title="[bold blue]🎬 Video Information[/]", border_style="blue"
        )

        self.console.print(panel)
        self.console.print()

    def ask_retry(self, error_message: str) -> bool:
        """Ask user if they want to retry after an error."""
        self.show_error(error_message)

        questions = [
            inquirer.Confirm(
                "retry", message="🔄 Would you like to retry?", default=True
            )
        ]

        try:
            answers = inquirer.prompt(questions)
            return answers["retry"] if answers else False
        except KeyboardInterrupt:
            return False

    def goodbye_message(self):
        """Display a goodbye message."""
        goodbye_panel = Panel(
            Align.center(
                Text("Thank you for using TubeHarvest! 🎬\n", style="bold green")
                + Text("Happy downloading! ✨", style="cyan")
            ),
            border_style="green",
            box=box.DOUBLE,
        )

        self.console.print(goodbye_panel)


# Global UI instance
ui = TubeHarvestUI()
