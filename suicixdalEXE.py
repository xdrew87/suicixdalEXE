import os
import subprocess
import random 
import requests
import json
import time
import phonenumbers
import platform
import sys
from phonenumbers import (
    parse,
    is_valid_number,
    carrier,
    geocoder,
    timezone,
    PhoneNumberFormat
)

# Constants for color codes
Wh = "\033[97m"  # White color
Gr = "\033[32m"  # Green color
Ye = "\033[33m"  # Yellow color
Re = "\033[31m"  # Red color
Cy = "\033[36m"  # Cyan color
Mg = "\033[35m"  # Magenta color
Bld = "\033[1m"  # Bold text

# Decorator to mark functions as menu options
def is_option(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        input(f"\n{Wh}{Bld}Press Enter to return to the main menu...{Wh}")
    return wrapper

# Clear terminal screen
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

# Clone GitHub repository for ZPhisher
def install_zphisher():
    clear_screen()
    print(f"{Mg}Installing ZPhisher...{Wh}")
    time.sleep(2)

    tools_directory = "./suicixdalEXE/Tools"
    
    # Check if the tools directory exists, if not create it
    if not os.path.exists(tools_directory):
        print(f"{Wh}Creating Tools directory...{Gr}")
        os.makedirs(tools_directory)

    # Change to the Tools directory
    os.chdir(tools_directory)

    # Remove existing zphisher directory if it exists
    if os.path.exists("zphisher"):
        print(f"{Wh}Removing existing ZPhisher directory...{Gr}")
        subprocess.run(["rm", "-rf", "zphisher"], check=True)

    # Clone the ZPhisher repository
    print(f"{Wh}Cloning ZPhisher repository...{Gr}")
    subprocess.run(["git", "clone", "https://github.com/htr-tech/zphisher"], check=True)

    # Change to the zphisher directory
    os.chdir("zphisher")

    # Run the ZPhisher script
    print(f"{Wh}Running ZPhisher...{Gr}")
    subprocess.run(["bash", "zphisher.sh"], check=True)

# Updated IP lookup function with additional info
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target: {Gr}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}============= {Gr}IP ADDRESS INFORMATION {Wh}=============')
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
    
    # Convert lat and lon to integer for map link
    lat = int(ip_data['latitude'])
    lon = int(ip_data['longitude'])
    print(f"{Wh} Maps            :{Gr}", f"https://www.google.com/maps/@{lat},{lon},8z")
    
    print(f"{Wh} EU              :{Gr}", ip_data["is_eu"])
    print(f"{Wh} Postal          :{Gr}", ip_data["postal"])
    print(f"{Wh} Calling Code    :{Gr}", ip_data["calling_code"])
    print(f"{Wh} Capital         :{Gr}", ip_data["capital"])
    print(f"{Wh} Borders         :{Gr}", ip_data["borders"])
    print(f"{Wh} Country Flag    :{Gr}", ip_data["flag"]["emoji"])
    print(f"{Wh} ASN             :{Gr}", ip_data["connection"]["asn"])
    print(f"{Wh} ORG             :{Gr}", ip_data["connection"]["org"])
    print(f"{Wh} ISP             :{Gr}", ip_data["connection"]["isp"])
    print(f"{Wh} Domain          :{Gr}", ip_data["connection"]["domain"])
    print(f"{Wh} ID              :{Gr}", ip_data["timezone"]["id"])
    print(f"{Wh} ABBR            :{Gr}", ip_data["timezone"]["abbr"])
    print(f"{Wh} DST             :{Gr}", ip_data["timezone"]["is_dst"])
    print(f"{Wh} Offset          :{Gr}", ip_data["timezone"]["offset"])
    print(f"{Wh} UTC             :{Gr}", ip_data["timezone"]["utc"])
    print(f"{Wh} Current Time    :{Gr}", ip_data["timezone"]["current_time"])

# Function to track phone numbers
@is_option
def phoneGW():
    User_phone = input(
        f"\n{Wh}Enter phone number (e.g., +6281xxxxxxxxx): {Gr}"
    )
    default_region = "ID"  # Default country is Indonesia
    try:
        parsed_number = phonenumbers.parse(User_phone, default_region)
        region_code = phonenumbers.region_code_for_number(parsed_number)
        jenis_provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        is_valid_number_flag = phonenumbers.is_valid_number(parsed_number)
        is_possible_number_flag = phonenumbers.is_possible_number(parsed_number)
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(
            parsed_number, default_region, with_formatting=True
        )
        number_type = phonenumbers.number_type(parsed_number)
        timezone1 = timezone.time_zones_for_number(parsed_number)
        timezoneF = ', '.join(timezone1)

        print(f"\n{Wh}========== {Gr}PHONE NUMBER INFORMATION {Wh}==========")
        print(f"\n{Wh}Location             :{Gr} {location}")
        print(f"{Wh}Region Code          :{Gr} {region_code}")
        print(f"{Wh}Timezone             :{Gr} {timezoneF}")
        print(f"{Wh}Operator             :{Gr} {jenis_provider}")
        print(f"{Wh}Valid number         :{Gr} {is_valid_number_flag}")
        print(f"{Wh}Possible number      :{Gr} {is_possible_number_flag}")
        print(f"{Wh}International format :{Gr} {formatted_number}")
        print(f"{Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
        print(f"{Wh}Original number      :{Gr} {parsed_number.national_number}")
        print(f"{Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
        print(f"{Wh}Country code         :{Gr} {parsed_number.country_code}")
        print(f"{Wh}Local number         :{Gr} {parsed_number.national_number}")
        if number_type == phonenumbers.PhoneNumberType.MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a mobile number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line number")
        elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE:
            print(f"{Wh}Type                 :{Gr} This is a fixed-line or mobile number")
        elif number_type == phonenumbers.PhoneNumberType.TOLL_FREE:
            print(f"{Wh}Type                 :{Gr} This is a toll-free number")
        elif number_type == phonenumbers.PhoneNumberType.PREMIUM_RATE:
            print(f"{Wh}Type                 :{Gr} This is a premium-rate number")
        elif number_type == phonenumbers.PhoneNumberType.SHARED_COST:
            print(f"{Wh}Type                 :{Gr} This is a shared-cost number")
        elif number_type == phonenumbers.PhoneNumberType.VOIP:
            print(f"{Wh}Type                 :{Gr} This is a VOIP number")
        elif number_type == phonenumbers.PhoneNumberType.UNKNOWN:
            print(f"{Wh}Type                 :{Gr} Unknown number type")
    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{Re}Invalid phone number format.{Wh}")

# Function to track usernames across platforms
@is_option
def TrackLu():
    username = input(f"{Wh}\n Enter the username to track: {Gr}")
    results = {}

    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
    ]
    for site in social_media:
        url = site['url'].format(username)
        response = requests.get(url)
        if response.status_code == 200:
            results[site['name']] = url
        else:
            results[site['name']] = f"{Wh}Not Found{Re}"

    print(f"\n{Wh}==================== {Gr}Username Information {Wh}====================")
    for platform, link in results.items():
        print(f"{Wh}{platform}: {Gr}{link}")

# Show public IP function
@is_option
def showIP():
    response = requests.get('https://api.ipify.org?format=json')
    ip_data = response.json()
    print(f"\n{Wh}Your Public IP Address: {Gr}{ip_data['ip']}{Wh}")

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
    except KeyboardInterrupt:
        print(f"\n{Re}Ping interrupted. Returning to main menu...{Wh}")
        main_menu()

# Main menu with improved formatting
def main_menu():
    while True:
        clear_screen()
        print(f"""
        {Mg}===============================================
        ============ {Gr}{Bld}Suicidal Multi-Tool{Wh} =============
        ===============================================
        {Gr}{Bld}1. {Wh}Track an IP{Gr}
        {Cy}{Bld}2. {Wh}Phone Number Lookup{Gr}
        {Ye}{Bld}3. {Wh}Track a Username{Gr}
        {Mg}{Bld}4. {Wh}Show Public IP{Gr}
        {Gr}{Bld}5. {Wh}ZPhisher Installation{Gr}
        {Re}{Bld}6. {Wh}Ip pinger{Gr}
        {Re}{Bld}7. {Wh}Exit{Gr}
        {Wh}===============================================
        """)
        choice = input(f"{Wh}{Bld}Select an option: {Gr}")
        
        if choice == "1":
            IP_Track()
        elif choice == "2":
            phoneGW()
        elif choice == "3":
            TrackLu()
        elif choice == "4":
            showIP()
        elif choice == "5":
            install_zphisher()  # Call the function to install ZPhisher
        elif choice == "6":
            ip_pinger()
        elif choice == "7":
            print(f"{Wh}This tool was made by @mlag or xdrew87 Goodbye!{Wh}")
            sys.exit()
        else:
            print(f"{Re}Invalid option. Please try again.{Wh}")

# Initialize and start
if __name__ == "__main__":
    clear_screen()
    main_menu()
