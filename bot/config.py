#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os

try:
    from utils.dataIO import fileIO
except ModuleNotFoundError:
    from bot.utils.dataIO import fileIO

false_strings = ["false", "False", "f", "F", "0", "", "n", "N", "no", "No", "NO", "FALSE"]

CONFIG_JSON = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.json"))

if fileIO(CONFIG_JSON, "check"):
    config = fileIO(CONFIG_JSON, "load")
else:
    config = {
        "Twitter": {
            "consumer_key": os.environ.get("CONSUMER_KEY", ac2nSOzNnmc5UNaEHzsl2HrVw),
            "consumer_secret": os.environ.get("CONSUMER_SECRET", fqLGVmYW66FPjB0XVfq3btuFbQPHMioNjXEOwTFsBG3Kq2JWoz),
            "access_token": os.environ.get("ACCESS_TOKEN", 1029416311112302594-y61cX4y16AyhbZQvfLRR6sMmbk7wZf),
            "access_token_secret": os.environ.get("ACCESS_TOKEN_SECRET", AMTrl8t5bER3u6RXPnCiuGvHIBs8gkPxuO5Tki7Z7Spoc ),
        },
        "Discord": [
            {
                "IncludeReplyToUser": False
                if os.environ.get("INCLUDE_REPLY_TO_USER", None) in false_strings
                else True,
                "IncludeRetweet": False
                if os.environ.get("INCLUDE_RETWEET", None) in false_strings
                else True,
                "IncludeUserReply": False
                if os.environ.get("INCLUDE_USER_REPLY", None) in false_strings
                else True,
                "webhook_urls": os.environ.get("WEBHOOK_URL", "").replace(" ", "").split(","),
                "twitter_ids": os.environ.get("TWITTER_ID", "").replace(" ", "").split(","),
                "custom_message": os.environ.get("CUSTOM_MESSAGE", None),
                "keyword_sets": [
                    keyword_set.split("+")
                    for keyword_set in os.environ.get("KEYWORDS", "").replace(" ", "").split(",")
                ],
            }
        ],
    }

if __name__ == "__main__":
    print(config)
