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
        "n_scraped": "",
        "row_counts": ""
    }
}