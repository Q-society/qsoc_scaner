#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(Fore.CYAN + Style.BRIGHT + """
 ██████╗     ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔═══██╗    ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
██║   ██║    ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
██║   ██║    ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
╚██████╔╝    ███████║╚██████╔╝╚██████╗██║███████╗    ██║      ██║   
 ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝    ╚═╝      ╚═╝   
    """)
    print(Fore.GREEN + "       [+]-------------------------------------------------[+]")
    print(Fore.GREEN + "       [+]         ULTRA-FAST OSINT USERNAME FINDER        [+]")
    print(Fore.GREEN + "       [+]               POWERED BY Q SOCIETY              [+]")
    print(Fore.GREEN + "       [+]-------------------------------------------------[+]")
    print("\n")

def main_menu():
    while True:
        show_banner()
        print(Fore.YELLOW + Style.BRIGHT + "   [ 1 ] " + Fore.WHITE + "Start Tool (OSINT Username Search)")
        print(Fore.YELLOW + Style.BRIGHT + "   [ 2 ] " + Fore.RED + "Exit")
        print("\n")
        
        choice = input(Fore.CYAN + " Q_Soc_Scanner > " + Fore.WHITE)
        
        if choice == "1":
            start_osint_scanner()
            input(Fore.YELLOW + "\nPress [ENTER] to return to the main menu...")
        elif choice == "2":
            print(Fore.RED + "\n[-] Exiting Q Society System... Stay safe! 🛡️\n")
            sys.exit()
        else:
            print(Fore.RED + "\n[-] Invalid option! Please try again.")
            time.sleep(1.5)

# Tek bir saytı yoxlayan funksiya (Thread üçün)
def check_single_site(site_template, username, headers):
    url = "https://" + site_template.format(username)
    display_name = site_template.split(".")[0].capitalize()
    try:
        # Sürət üçün HEAD sorğusu və 3 saniyəlik timeout
        response = requests.head(url, headers=headers, timeout=3.0, allow_redirects=True)
        if response.status_code == 200:
            return display_name, url
    except requests.exceptions.RequestException:
        pass
    return None

def start_osint_scanner():
    show_banner()
    print(Fore.MAGENTA + Style.BRIGHT + "===[ MULTITHREADED SATELLITE ENGINE ]===\n")
    username = input(Fore.YELLOW + "Enter target username: " + Fore.WHITE).strip()
    
    if not username:
        print(Fore.RED + "\n[-] Error: Username cannot be empty!")
        return

    # 200 Database targets
    sites_200 = [
        "github.com/{}", "instagram.com/{}/", "tiktok.com/@{}", "x.com/{}", "youtube.com/@{}",
        "reddit.com/user/{}", "pinterest.com/{}/", "steamcommunity.com/id/{}", "twitch.tv/{}", "soundcloud.com/{}", 
        "medium.com/@{}", "vimeo.com/{}", "behance.net/{}", "dribbble.com/{}", "flickr.com/photos/{}", 
        "disqus.com/by/{}", "imgur.com/user/{}", "patreon.com/{}", "linktr.ee/{}", "gitlab.com/{}", 
        "bitbucket.org/{}", "docker.com/u/{}", "npm+js.com/~{}", "pypi.org/user/{}", "dev.to/{}", 
        "hashnode.com/@{}", "hackerrank.com/{}", "leetcode.com/{}", "codewars.com/users/{}", "tumblr.com/{}", 
        "deviantart.com/{}", "quora.com/profile/{}", "producthunt.com/@{}", "kickstarter.com/profile/{}", "instructables.com/member/{}", 
        "mixcloud.com/{}", "bandcamp.com/{}", "reverbnation.com/{}", "scribd.com/{}", "wattpad.com/user/{}", 
        "goodreads.com/{}", "letterboxd.com/{}", "last.fm/user/{}", "roblox.com/user/{}", "chess.com/member/{}", 
        "lichess.org/@/{}", "crunchyroll.com/user/{}", "myanimelist.net/profile/{}", "tripadvisor.com/Profile/{}", "booking.com/user/{}", 
        "airbnb.com/users/show/{}", "couchsurfing.com/people/{}", "alltrails.com/members/{}", "strava.com/athletes/{}", "fitbit.com/user/{}", 
        "myfitnesspal.com/{}", "mapmyrun.com/user/{}", "garmin.com/{}", "wikipedia.org/wiki/User:{}", "wiktionary.org/wiki/User:{}", 
        "about.me/{}", "keybase.io/{}", "gravatar.com/{}", "angellist.com/{}", "fiverr.com/{}", 
        "freelancer.com/u/{}", "guru.com/freelancers/{}", "slideshare.net/{}", "speakerdeck.com/{}", "prezi.com/user/{}", 
        "issuu.com/{}", "archive.org/details/@{}", "academia.edu/{}", "researchgate.net/profile/{}", "orcid.org/{}", 
        "mendeley.com/profiles/{}", "zotero.org/{}", "source forge.net/u/{}", "launchpad.net/~{}", "bugs.debian.org/{}", 
        "archlinux.org/user/{}", "slack.com/{}", "discord.com/users/{}", "telegram.me/{}", "viber.com/{}", 
        "whatsapp.com/{}", "ebay.com/usr/{}", "amazon.com/shop/{}", "etsy.com/shop/{}", "aliexpress.com/store/{}", 
        "artstation.com/{}", "500px.com/{}", "vsco.co/{}", "smugmug.com/{}", "shutterstock.com/g/{}", 
        "buymeacoffee.com/{}", "ko-fi.com/{}", "kickstarter.com/{}", "indiegogo.com/individuals/{}", "gofundme.com/f/{}", 
        "nytimes.com/{}", "theguardian.com/{}", "reuters.com/{}", "bbc.co.uk/{}", "cnn.com/{}", 
        "techcrunch.com/author/{}", "wired.com/{}", "theverge.com/{}", "engadget.com/{}", "gizmodo.com/{}", 
        "mashable.com/{}", "cnet.com/{}", "zdnet.com/{}", "forbes.com/{}", "bloomberg.com/{}", 
        "imdb.com/user/ur{}", "rottentomatoes.com/user/id/{}", "metacritic.com/user/{}", "tvtime.com/{}", "trakt.tv/users/{}", 
        "playstation.com/{}", "xboxlive.com/{}", "steamcommunity.com/{}", "epicgames.com/{}", "minecraft.net/user/{}"
    ]

    print(Fore.CYAN + f"[*] Launching 50 parallel threads to scan {len(sites_200)} sites simultaneously...")
    print(Fore.GREEN + f"\n{'Platform':<25} | {'Status':<12} | {'Profile Link'}")
    print(Fore.GREEN + "-" * 80)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }

    found_count = 0
    start_time = time.time()

    # Eyni anda 50 fərqli sorğu göndərir (ThreadPoolExecutor)
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_single_site, site, username, headers) for site in sites_200]
        
        for future in as_completed(futures):
            result = future.result()
            if result:
                display_name, url = result
                print(f"{Fore.WHITE}{display_name:<25} | {Fore.GREEN}{'FOUND':<12} {Fore.WHITE}| {url}")
                found_count += 1

    end_time = time.time()
    total_time = round(end_time - start_time, 2)
    print(Fore.CYAN + f"\n[+] Scan completed in {total_time} seconds! Total active accounts found: {found_count}")

if __name__ == "__main__":
    main_menu()
