import os
import sys
import subprocess
from pytube import YouTube
import instaloader
import yt_dlp as youtube_dl

# Check dependencies
REQUIRED_PACKAGES = [
    'pytube', 'instaloader', 'youtube-dl', 'requests',
    'yt-dlp', 'moviepy', 'selenium'
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def install_dependencies():
    for package in REQUIRED_PACKAGES:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

class SocialMediaDownloader:
    def __init__(self):
        self.platforms = {
            1: "YouTube",
            2: "Facebook",
            3: "Twitter",
            4: "Instagram",
            5: "TikTok"
        }
        
        self.content_types = {
            1: "Audio",
            2: "Video",
            3: "Story",
            4: "Post",
            5: "Reels"
        }

    def show_menu(self):
        clear_screen()
        print("""
        █▀ █▀▀ █▀█ █░█ █▀▀ █▀▀ ▀█▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █▀▀ ▀█▀
        ▄█ ██▄ █▀▄ ▀▄▀ ██▄ █▄▄ ░█░   █░▀░█ █▄█ █▄▀ ██▄ █▄▄ ░█░
        """)
        print("Supported Platforms:")
        for key, value in self.platforms.items():
            print(f"{key}. {value}")
        
        platform = int(input("\nChoose platform (1-5): "))
        if platform not in self.platforms:
            print("Invalid choice!")
            return
            
        print("\nContent Types:")
        for key, value in self.content_types.items():
            print(f"{key}. {value}")
            
        content_type = int(input("\nChoose content type (1-5): "))
        url = input("\nEnter URL: ")
        
        self.download_content(platform, content_type, url)

    def download_content(self, platform, content_type, url):
        platform_name = self.platforms[platform]
        content_type_name = self.content_types[content_type]
        
        print(f"\nDownloading {content_type_name} from {platform_name}...")
        
        try:
            if platform == 1:  # YouTube
                self.download_youtube(url, content_type)
            elif platform == 2:  # Facebook
                self.download_facebook(url, content_type)
            elif platform == 3:  # Twitter
                self.download_twitter(url, content_type)
            elif platform == 4:  # Instagram
                self.download_instagram(url, content_type)
            elif platform == 5:  # TikTok
                self.download_tiktok(url, content_type)
                
            print("\nDownload completed successfully!")
        except Exception as e:
            print(f"Error: {str(e)}")

    # YouTube Downloader
    def download_youtube(self, url, content_type):
        yt = YouTube(url)
        if content_type == 1:  # Audio
            stream = yt.streams.filter(only_audio=True).first()
        else:  # Video
            stream = yt.streams.get_highest_resolution()
        stream.download()

    # Instagram Downloader
    def download_instagram(self, url, content_type):
        loader = instaloader.Instaloader()
        shortcode = url.split("/")[-2]
        
        if content_type == 3:  # Story
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_storyitem(post, target=f"ig_{shortcode}")
        else:  # Post/Reels
            post = instaloader.Post.from_shortcode(loader.context, shortcode)
            loader.download_post(post, target=f"ig_{shortcode}")

    # TikTok Downloader (requires additional setup)
    def download_tiktok(self, url, content_type):
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    # Facebook Downloader (requires API access)
    def download_facebook(self, url, content_type):
        # Requires facebook-sdk and access token
        print("Facebook download requires API access and approval")
        
    # Twitter Downloader (requires API keys)
    def download_twitter(self, url, content_type):
        # Requires tweepy and API credentials
        print("Twitter download requires developer API access")

if __name__ == "__main__":
    install_dependencies()
    downloader = SocialMediaDownloader()
    downloader.show_menu()
