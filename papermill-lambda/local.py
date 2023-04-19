"""
local testing
"""
import json
from lambda_function import lambda_handler

def main():
    """
    Main function
    """
    path = './papermill-lambda/events/event02.json'
    with open(path, 'r', encoding='utf-8') as f:
        event = json.load(f)
    lambda_handler(event, None)

if __name__ == '__main__':
    main()
