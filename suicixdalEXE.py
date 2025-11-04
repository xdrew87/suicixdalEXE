import os
import subprocess
import random 
import instaloader
import requests
import json
import time
import phonenumbers
import platform
import sys
import shutil
import stat
import traceback
import socket
import time
import argparse
import re
from phonenumbers import parse, is_valid_number, carrier, geocoder, timezone, PhoneNumberFormat, phonenumberutil
from termcolor import colored
from datetime import datetime

# Constants for color codes
Wh = "\033[97m"  # White color
Gr = "\033[32m"  # Green color
Ye = "\033[33m"  # Yellow color
Re = "\033[31m"  # Red color
Cy = "\033[36m"  # Cyan color
Mg = "\033[35m"  # Magenta color
Bld = "\033[1m"  # Bold text

VERSION = "v2.0"

# Decorator to mark functions as menu options
def is_option(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"{Re}An error occurred: {e}{Wh}")
            traceback.print_exc()
        input(f"\n{Wh}{Bld}Press Enter to return to the main menu...{Wh}")
    return wrapper

# Clear terminal screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Loading animation for long-running actions
def loading_animation(message, duration=2):
    spinner = ['|', '/', '-', '\\']
    print(f"{Ye}{message}", end='', flush=True)
    for i in range(duration * 8):
        print(f"\b{spinner[i % 4]}", end='', flush=True)
        time.sleep(0.125)
    print(f"\b{Gr}✓{Wh}")

# Stylized ASCII banner with color gradient
def print_banner():
    banner_lines = [                                                                                                
        f"{Mg}  ██████╗ ██╗   ██╗ ██╗ ██████╗ ██╗██████╗  █████╗ ██╗     {Wh}██╗    ██╗",
        f"{Mg} ██╔════╝ ██║   ██║ ██║██╔════╝ ██║██╔══██╗██╔══██╗██║     {Wh}██║    ██║",
        f"{Cy} ██║  ███╗██║   ██║ ██║██║  ███╗██║██║  ██║███████║██║     {Wh}██║ █╗ ██║",
        f"{Cy} ██║   ██║██║   ██║ ██║██║   ██║██║██║  ██║██║  ██║██║     {Wh}██║███╗██║",
        f"{Ye} ╚██████╔╝╚██████╔╝ ██║╚██████╔╝██║██████╔╝██║  ██║███████╗{Wh}╚███╔███╔╝",
        f"{Ye}  ╚═════╝  ╚═════╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝{Wh} ╚══╝╚══╝ ",
        f"{Wh}{Bld}                                   {Gr}Suicidal Multi-Tool {VERSION}{Wh}\n"
    ]                                                                                                               
    print('\n'.join(banner_lines))

# Updated IP lookup function with additional info
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target: {Gr}")
    print(f'\n{Ye}{"═"*12} {Bld}{Gr}IP ADDRESS INFORMATION{Wh} {Ye}{"═"*12}{Wh}')
    loading_animation("Fetching IP info...")
    req_api = requests.get(f"http://ipwho.is/{ip}")  # API IPWHOIS.IS
    ip_data = json.loads(req_api.text)
    time.sleep(2)
    
    print(f"{Wh}\n IP target       :{Gr}", ip)
    print(f"{Wh} Type IP         :{Gr}", ip_data["type"])
    print(f"{Wh} Country         :{Gr}", ip_data["country"])
    print(f"{Wh} Country Code    :{Gr}", ip_data["country_code"])
    print(f"{Wh} City            :{Gr}", ip_data["city"])
    print(f"{Wh} Continent       :{Gr}", ip_data["continent"])
    print(f"{Wh} Continent Code  :{Gr}", ip_data["continent_code"])
    print(f"{Wh} Region          :{Gr}", ip_data["region"])
    print(f"{Wh} Region Code     :{Gr}", ip_data["region_code"])
    print(f"{Wh} Latitude        :{Gr}", ip_data["latitude"])
    print(f"{Wh} Longitude       :{Gr}", ip_data["longitude"])
    
    lat = ip_data.get('latitude')
    lon = ip_data.get('longitude')
    if lat and lon:
        print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    
    print(f"{Wh} EU              :{Gr}", ip_data.get("is_eu", "N/A"))
    print(f"{Wh} Postal          :{Gr}", ip_data.get("postal", "N/A"))
    print(f"{Wh} Calling Code    :{Gr}", ip_data.get("calling_code", "N/A"))
    print(f"{Wh} Capital         :{Gr}", ip_data.get("capital", "N/A"))
    print(f"{Wh} Borders         :{Gr}", ip_data.get("borders", "N/A"))
    print(f"{Wh} Country Flag    :{Gr}", ip_data.get("flag", {}).get("emoji", "N/A"))
    print(f"{Wh} ASN             :{Gr}", ip_data.get("connection", {}).get("asn", "N/A"))
    print(f"{Wh} ORG             :{Gr}", ip_data.get("connection", {}).get("org", "N/A"))
    print(f"{Wh} ISP             :{Gr}", ip_data.get("connection", {}).get("isp", "N/A"))
    print(f"{Wh} Domain          :{Gr}", ip_data.get("connection", {}).get("domain", "N/A"))
    print(f"{Wh} ID              :{Gr}", ip_data.get("timezone", {}).get("id", "N/A"))
    print(f"{Wh} ABBR            :{Gr}", ip_data.get("timezone", {}).get("abbr", "N/A"))
    print(f"{Wh} DST             :{Gr}", ip_data.get("timezone", {}).get("is_dst", "N/A"))
    print(f"{Wh} Offset          :{Gr}", ip_data.get("timezone", {}).get("offset", "N/A"))
    print(f"{Wh} UTC             :{Gr}", ip_data.get("timezone", {}).get("utc", "N/A"))
    print(f"{Wh} Current Time    :{Gr}", ip_data.get("timezone", {}).get("current_time", "N/A"))

# Function to track phone numbers
@is_option
def phoneGW():
    User_phone = input(
        f"\n{Wh}Enter phone number (e.g., +6281xxxxxxxxx): {Gr}"
    )
    default_region = "ID"  # Default country is Indonesia
    try:
        parsed_number = parse(User_phone, default_region)
        region_code = geocoder.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number_flag = is_valid_number(parsed_number)
        is_possible_number_flag = phonenumbers.is_possible_number(parsed_number) # This function is not in the phonenumbers module directly
        formatted_number = phonenumbers.format_number(parsed_number, PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing( # This function is not in the phonenumbers module directly
            parsed_number, default_region, with_formatting=True 
        )
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n{Ye}{'═'*8} {Bld}{Gr}PHONE NUMBER INFORMATION{Wh} {Ye}{'═'*8}{Wh}")
        print(f"\n{Wh}Location             :{Gr} {location}")
        print(f"{Wh}Region Code          :{Gr} {region_code}")
        print(f"{Wh}Timezone             :{Gr} {timezoneF}")
        print(f"{Wh}Operator             :{Gr} {jenis_provider}")
        print(f"{Wh}Valid number         :{Gr} {is_valid_number_flag}")
        print(f"{Wh}Possible number      :{Gr} {is_possible_number_flag}")
        print(f"{Wh}International format :{Gr} {formatted_number}")
        print(f"{Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f"{Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f"{Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, PhoneNumberFormat.E164)}")
        print(f"{Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f"{Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumberutil.PhoneNumberType.MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumberutil.PhoneNumberType.FIXED_LINE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line number")
        elif number_type == phonenumberutil.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line or mobile number")
        elif number_type == phonenumberutil.PhoneNumberType.TOLL_FREE:
            print(f"{Wh}Type                 :{Gr} This is a toll-free number")
        elif number_type == phonenumberutil.PhoneNumberType.PREMIUM_RATE:
            print(f"{Wh}Type                 :{Gr} This is a premium-rate number")
        elif number_type == phonenumberutil.PhoneNumberType.SHARED_COST:
            print(f"{Wh}Type                 :{Gr} This is a shared-cost number")
        elif number_type == phonenumberutil.PhoneNumberType.VOIP:
            print(f"{Wh}Type                 :{Gr} This is a VOIP number")
        elif number_type == phonenumberutil.PhoneNumberType.UNKNOWN:
            print(f"{Wh}Type                 :{Gr} Unknown number type")
    except phonenumberutil.NumberParseException:
        print(f"{Re}Invalid phone number format.{Wh}")

# Function to track usernames across platforms
@is_option
def TrackLu():
    username = input(f"{Wh}\n Enter the username to track: {Gr}")
    results = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.youtube.com/@{}", "name": "YouTube"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.reddit.com/user/{}", "name": "Reddit"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"},
        {"url": "https://vimeo.com/{}", "name": "Vimeo"},
        {"url": "https://soundcloud.com/{}", "name": "SoundCloud"},
        {"url": "https://www.twitch.tv/{}", "name": "Twitch"},
        {"url": "https://open.spotify.com/user/{}", "name": "Spotify"},
        {"url": "https://steamcommunity.com/id/{}", "name": "Steam"},
        {"url": "https://www.patreon.com/{}", "name": "Patreon"},
        {"url": "https://gitlab.com/{}", "name": "GitLab"},
        {"url": "https://{}.tumblr.com", "name": "Tumblr"},
        {"url": "https://dev.to/{}", "name": "Dev.to"},
        {"url": "https://medium.com/@{}", "name": "Medium"},
        {"url": "https://www.behance.net/{}", "name": "Behance"},
    ]

    print(f"\n{Ye}{'═'*14} {Bld}{Gr}USERNAME INFORMATION{Wh} {Ye}{'═'*14}{Wh}")
    loading_animation("Checking platforms...")

    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=True)
            if response.status_code == 200:
                print(f"{Wh}{site['name']:<12}: {Gr}{url}")
            else:
                print(f"{Wh}{site['name']:<12}: {Re}Not Found")
        except requests.RequestException:
            print(f"{Wh}{site['name']:<12}: {Re}Error Checking")

# Show public IP function
@is_option
def showIP():
    loading_animation("Fetching public IP...")
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    print(f"\n{Ye}{'═'*8} {Bld}{Gr}PUBLIC IP INFORMATION{Wh} {Ye}{'═'*8}{Wh}")
    print(f"{Wh}Your Public IP Address: {Gr}{ip_data['ip']}{Wh}")

# Ip Pinger function
@is_option
def ip_pinger():
    ip = input(f"{Wh}Enter IP address to ping: {Gr}")
    ping_command = ['ping', '-c', '1', ip] if platform.system().lower() != 'windows' else ['ping', '-n', '1', ip]
    try:
        while True:
            response = subprocess.run(ping_command, capture_output=True, text=True)
            if "TTL=" in response.stdout or "ttl=" in response.stdout:
                print(f"{Gr}Ping to {ip} successful.{Wh}")
            else:
                print(f"{Re}Ping to {ip} Slammed by Frosted C2.{Wh}")
            num = random.randint(1, 9)
            if os.name == "nt":  # Only change color on Windows
                os.system(f'color {num}')
            time.sleep(1)
            print(f"{Wh}{'-'*50}")
    except KeyboardInterrupt:
        print(f"\n{Re}Ping interrupted. Returning to main menu...{Wh}")
        main_menu()

def visible_length(text):
    """Calculate the visible length of a string, ignoring ANSI escape sequences."""
    ansi_escape = re.compile(r'\x1b\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]')
    return len(ansi_escape.sub('', text))

# Paping Tool function
@is_option
def Paping_Tool():
    ip = input("Enter IP address to ping with interval: ")
    port = input("Enter port to ping (default 443): ")
    if not port.isdigit():
        port = "443"  # Default port if none provided
    interval = input("Enter interval in seconds (default 1): ")
    if not interval.isdigit():
        interval = "1"  # Default interval if none provided

    try:
        while True:  # Infinite loop for continuous pinging
            # Get the current time and format it
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Clear the line using ANSI escape codes
            sys.stdout.write("\033[2K\033[0G")  # Clear the entire line and move the cursor to the start
            sys.stdout.flush()

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Reduced timeout to speed up the pinging
            result = sock.connect_ex((ip, int(port)))

            # Construct the result message
            if result == 0:
                result_message = f"[{current_time}] {colored('Connection to ' + ip + ':' + port + ' successful!', 'green')}"
            else:
                result_message = f"[{current_time}] {colored('Connection to ' + ip + ':' + port + ' offline.', 'red')}"

            # Display the result message
            sys.stdout.write("\033[2K\033[0G")
            sys.stdout.write(result_message)
            sys.stdout.flush()
            print(f"{Wh}", end='\r')

            sock.close()
            time.sleep(float(interval))  # Pause between pings
    except KeyboardInterrupt:
        print(colored("\nPaping interrupted. Returning to main menu...", "yellow"))
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))

# Function to look up information about a ZIP code
@is_option
def zipcode_lookup():
    zipcode = input(f"{Wh}Enter a ZIP code: {Gr}")
    try:
        response = requests.get(f"http://api.zippopotam.us/us/{zipcode}")
        if response.status_code == 200:
            data = response.json()
            print(f"\n{Ye}{'═'*8} {Bld}{Gr}ZIP CODE INFORMATION{Wh} {Ye}{'═'*8}{Wh}")
            print(f"{Wh}ZIP Code        :{Gr} {zipcode}")
            print(f"{Wh}Country         :{Gr} {data.get('country', 'N/A')}")
            print(f"{Wh}State           :{Gr} {data.get('places', [{}])[0].get('state', 'N/A')}")
            print(f"{Wh}City            :{Gr} {data.get('places', [{}])[0].get('place name', 'N/A')}")
            print(f"{Wh}Latitude        :{Gr} {data.get('places', [{}])[0].get('latitude', 'N/A')}")
            print(f"{Wh}Longitude       :{Gr} {data.get('places', [{}])[0].get('longitude', 'N/A')}")
        else:
            print(f"{Re}Invalid ZIP code or data not found.{Wh}")
    except Exception as e:
        print(f"{Re}An error occurred: {e}{Wh}")

# Function to perform OSINT email lookup using Have I Been Pwned API
@is_option
def email_lookup():
    email = input(f"{Wh}Enter an email address: {Gr}")
    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "User-Agent": "OSINT-Tool",
        "hibp-api-key": "your_hibp_api_key"  # Replace with your Have I Been Pwned API key
    }
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print(f"\n{Ye}{'═'*8} {Bld}{Gr}EMAIL BREACH INFORMATION{Wh} {Ye}{'═'*8}{Wh}")
            for breach in breaches:
                print(f"{Wh}Breach Name      :{Gr} {breach['Name']}")
                print(f"{Wh}Domain           :{Gr} {breach['Domain']}")
                print(f"{Wh}Breach Date      :{Gr} {breach['BreachDate']}")
                print(f"{Wh}Data Compromised :{Gr} {', '.join(breach['DataClasses'])}")
                print(f"{Wh}Description      :{Gr} {breach['Description']}\n")
        elif response.status_code == 404:
            print(f"{Gr}No breaches found for this email address.{Wh}")
        else:
            print(f"{Re}Error: Unable to fetch data. Status code: {response.status_code}{Wh}")
    except Exception as e:
        print(f"{Re}An error occurred: {e}{Wh}")

@is_option
def ip_blacklist():
    ip_address = input(f"{Wh}Enter an IP address to check: {Gr}")
    try:
        response = requests.get(f"https://api.abuseipdb.com/api/v2/check/{ip_address}", headers={
            "Key": "y0abd9a9cc14fc6e48b3d1bdb92ebc0c54181bc2ff5ddb8f2a0a05eedc721d2f4bf98fba4ea553ddc",  # Replace with your AbuseIPDB API key
            "Accept": "application/json"
        })
        if response.status_code == 200:
            data = response.json()
            print(f"\n{Ye}{'═'*8} {Bld}{Gr}IP BLACKLIST CHECK{Wh} {Ye}{'═'*8}{Wh}")
            print(f"{Wh}IP Address      :{Gr} {ip_address}")
            print(f"{Wh}Is Blacklisted? :{Gr} {'Yes' if data['data']['is_blacklisted'] else 'No'}")
            print(f"{Wh}Abuse Confidence:{Gr} {data['data']['abuse_confidence_score']}")
        else:
            print(f"{Re}Error: Unable to fetch data. Status code: {response.status_code}{Wh}")
    except Exception as e:
        print(f"{Re}An error occurred: {e}{Wh}")

# Safeguards against brute-forcing
def prevent_brute_force():
    print(f"{Re}This script is not intended for brute-forcing or malicious activities.{Wh}")
    print(f"{Re}Please use it responsibly and adhere to ethical guidelines.{Wh}")

def print_footer():
    print(f"\n{Wh}{Bld}{'-'*60}")
    print(f"{Cy}  Need help? Select option 99 for help.  |  {Ye}Version: {VERSION}{Wh}")
    print(f"{Wh}{Bld}{'-'*60}{Wh}")

def print_help():
    print(f"\n{Ye}{'═'*10} {Bld}{Gr}HELP & INFO{Wh} {Ye}{'═'*10}{Wh}")
    print(f"{Wh}This tool provides various OSINT and network utilities.")
    print(f"{Wh}Options:")
    print(f"{Gr} 1{Wh}: Track an IP address and get geolocation info.")
    print(f"{Cy} 2{Wh}: Lookup phone number details.")
    print(f"{Ye} 3{Wh}: Track a username across social platforms.")
    print(f"{Mg} 4{Wh}: Show your public IP address.")
    print(f"{Ye} 5{Wh}: Check if an email has been in a breach.")
    print(f"{Re} 6{Wh}: Ping an IP address.")
    print(f"{Re} 7{Wh}: TCP ping (paping) a host:port.")
    print(f"{Re} 8{Wh}: Lookup US ZIP code info.")
    print(f"{Re}00{Wh}: Exit the tool.")
    print(f"{Cy}99{Wh}: Show this help message.")
    print(f"\n{Wh}For best results, use responsibly and ethically.\n")

# Security check at startup
def security_check():
    # Warn if running as root/admin
    if os.name == "posix":
        if os.geteuid() == 0:
            print(f"{Re}Warning: Running as root is not recommended!{Wh}")
    elif os.name == "nt":
        try:
            import ctypes
            if ctypes.windll.shell32.IsUserAnAdmin():
                print(f"{Re}Warning: Running as Administrator is not recommended!{Wh}")
        except Exception:
            pass

    # Check for suspicious environment variables or processes
    suspicious_env = ["LD_PRELOAD", "LD_LIBRARY_PATH", "DYLD_INSERT_LIBRARIES"]
    for var in suspicious_env:
        if var in os.environ:
            print(f"{Re}Warning: Suspicious environment variable detected: {var}{Wh}")

    # Check for common hacking tools/processes (very basic)
    suspicious_procs = ["tcpdump", "wireshark", "ettercap", "nmap"]
    try:
        proc_list = subprocess.check_output("ps aux" if os.name != "nt" else "tasklist", shell=True).decode().lower()
        for proc in suspicious_procs:
            if proc in proc_list:
                print(f"{Re}Warning: Suspicious process detected: {proc}{Wh}")
    except Exception:
        pass

@is_option
def instagram_lookup():
    """
    Fetches public information for an Instagram profile using Instaloader.
    """
    username = input(f"{Wh}\nEnter Instagram username to look up: {Gr}")
    if not username:
        print(f"{Re}Username cannot be empty.{Wh}")
        return

    print(f'\n{Ye}{"═"*10} {Bld}{Gr}INSTAGRAM PROFILE INFORMATION{Wh} {Ye}{"═"*10}{Wh}')
    loading_animation(f"Fetching profile for @{username}...")

    try:
        # Create an instance of Instaloader
        L = instaloader.Instaloader()
        
        # Retrieve profile
        profile = instaloader.Profile.from_username(L.context, username)

        print(f"\n{Wh}Username      :{Gr} {profile.username}")
        print(f"{Wh}Full Name     :{Gr} {profile.full_name}")
        print(f"{Wh}User ID       :{Gr} {profile.userid}")
        print(f"{Wh}Followers     :{Gr} {profile.followers}")
        print(f"{Wh}Following     :{Gr} {profile.followees}")
        print(f"{Wh}Posts         :{Gr} {profile.mediacount}")
        print(f"{Wh}Private       :{Gr} {'Yes' if profile.is_private else 'No'}")
        print(f"{Wh}Verified      :{Gr} {'Yes' if profile.is_verified else 'No'}")
        print(f"{Wh}Biography     :{Gr} {profile.biography.replace('\n', ' ')}")
        if profile.external_url:
            print(f"{Wh}External URL  :{Gr} {profile.external_url}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Re}Profile @{username} does not exist.{Wh}")
    except Exception as e:
        print(f"{Re}An error occurred: {e}{Wh}")

# Main menu with improved formatting
def main_menu():
    while True:
        clear_screen()
        print_banner()                                                                                              
        menu_layout = f"""
{Mg}╔═══════════════════════════════════╦═════════════════════════════════════╗
║{Bld}            NETWORK TOOLS            {Mg}║{Bld}             OSINT TOOLS              {Mg}║
╠═══════════════════════════════════╬═════════════════════════════════════╣
║ {Gr}1) {Wh}IP Tracker                      {Mg}║ {Cy}2) {Wh}Phone Number Lookup             {Mg}║
║ {Gr}4) {Wh}Show Public IP                  {Mg}║ {Cy}3) {Wh}Username Tracker                {Mg}║
║ {Gr}6) {Wh}IP Pinger                       {Mg}║ {Cy}5) {Wh}Email Breach Check              {Mg}║
║ {Gr}7) {Wh}Paping Tool (TCP Ping)          {Mg}║ {Cy}8) {Wh}ZIP Code Lookup                 {Mg}║
║ {Gr}9) {Wh}IP Blacklist Check              {Mg}║ {Cy}10) {Wh}Instagram Profile Lookup       {Mg}║
╚═══════════════════════════════════╩═════════════════════════════════════╝
{Mg}╔═════════════════════════════════════════════════════════════════════════╗
║ {Cy}99) {Wh}Help                           {Mg}║ {Re}00) {Wh}Exit                           {Mg}║
╚═════════════════════════════════════════════════════════════════════════╝
"""
        print(menu_layout)
        choice = input(f"{Wh}{Bld}└──> Select an option: {Gr}")
        if choice == "1":
            IP_Track()
        elif choice == "2":
            phoneGW()
        elif choice == "3":
            TrackLu()
        elif choice == "4":
            showIP()
        elif choice == "5":
            email_lookup()
        elif choice == "6":
            ip_pinger()
        elif choice == "7":
            Paping_Tool()
        elif choice == "8":
            zipcode_lookup()
        elif choice == "9":
            ip_blacklist()
        elif choice == "10":
            instagram_lookup()
        elif choice == "99":
            print_help()
            input(f"{Wh}{Bld}Press Enter to return to the main menu...{Wh}")
        elif choice == "00":
            print(f"{Wh}Thank you for using this tool. Goodbye!{Wh}")
            sys.exit()
        else:
            print(f"{Re}Invalid option. Please try again.{Wh}")


# Initialize and start
if __name__ == "__main__":
    security_check()
    clear_screen()
    print_banner()
    main_menu()
