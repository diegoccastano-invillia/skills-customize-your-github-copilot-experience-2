import argparse
import csv
import json
import sys
from urllib.error import URLError
from urllib.request import urlopen


def fetch_posts(api_url):
    """Fetch and decode a JSON list from the API URL."""
    raise NotImplementedError("Implement the API request and JSON decoding")


def normalize_posts(payload):
    """Validate API posts and return records with a word_count field."""
    raise NotImplementedError("Implement record validation and normalization")


def save_posts(posts, output_path):
    """Write normalized posts to a CSV file."""
    raise NotImplementedError("Implement CSV export")


def print_report(posts):
    """Print the record count, distinct users, and average word count."""
    raise NotImplementedError("Implement the pipeline summary")


def main():
    parser = argparse.ArgumentParser(description="Download and summarize API posts")
    parser.add_argument(
        "--url",
        default="https://jsonplaceholder.typicode.com/posts",
        help="URL that returns a JSON list of posts",
    )
    parser.add_argument("--output", default="posts.csv", help="Output CSV path")
    args = parser.parse_args()

    try:
        posts = normalize_posts(fetch_posts(args.url))
        save_posts(posts, args.output)
        print_report(posts)
        print(f"CSV saved to {args.output}")
    except (OSError, URLError, TimeoutError, json.JSONDecodeError, ValueError) as error:
        print(f"Pipeline failed: {error}", file=sys.stderr)
        return 1
    except NotImplementedError as error:
        print(f"Starter code is incomplete: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())