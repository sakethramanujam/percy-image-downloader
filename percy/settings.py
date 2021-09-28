STATS_URL = "https://mars.nasa.gov/rss/api/?feed=raw_images&category=mars2020&feedtype=json&latest=true"

RESOLUTIONS = {
    "full": "full_res",
    "large": "large",
    "medium": "medium",
    "small": "small"
}

IMAGE_FORMATS = {
    "full": "png",
    "large": "jpg",
    "medium": "jpg",
    "small": "jpg"
}

METADATA_TEMPLATE = {
    "images": {
        "full": {"last_updated": "", "current_counts": "", },
        "large": {"last_updated": "", "current_counts": ""},
        "medium": {"last_updated": "", "current_counts": ""},
        "small": {"last_updated": "", "current_counts": ""}
    },
    "metadata": {
        "last_updated": "",
        "n_pages": "",
        "n_rows": ""
    }
}

CAMERAS_DICT = {
            "NAVCAM_LEFT": "Navigation Camera - Left",
            "NAVCAM_RIGHT": "Navigation Camera - Right",
            "FRONT_HAZCAM_LEFT_A|FRONT_HAZCAM_LEFT_B": "Front Hazcam - Left",
            "FRONT_HAZCAM_RIGHT_A|FRONT_HAZCAM_RIGHT_B": "Front Hazcam - Right",
            "REAR_HAZCAM_LEFT": "Rear Hazcam - Left",
            "REAR_HAZCAM_RIGHT": "Rear Hazcam - Right",
            "MCZ_LEFT": "Mastcam-Z - Left" ,
            "MCZ_RIGHT": "Mastcam-Z - Right",
            "SKYCAM": "MEDA SkyCam",
            "SHERLOC_WATSON": "SHERLOC - WATSON",
            "SHERLOC_ACI": "SHERLOC - Context Imager",
            "SUPERCAM_RMI": "SuperCam Remote Micro Imager",
            "EDL_PUCAM1": "Parachute Up-Look Camera A",
            "EDL_PUCAM2": "Parachute Up-Look Camera B",
            "EDL_DDCAM": "Descent Stage Down-Look Camera",
            "EDL_RUCAM": "Rover Up-Look Camera",
            "EDL_RDCAM": "Rover Down-Look Camera",
            "LCAM": "Lander Vision System Camera",
            "HELI_NAV": "Navigation Camera",
            "HELI_RTE": "Color Camera" 
}

CAMERA_CODES = CAMERAS_DICT.keys()
CAMERA_NAMES = CAMERAS_DICT.values()