import backoff
import logging
import httpx

HEALTH_CHECK_ENDPOINT = "/"
LIST_LEAGUES_ENDPOINT = "/v0/leagues/"
LIST_PLAYERS_ENDPOINT = "/v0/players/"
LIST_PERFORMANCES_ENDPOINT = "/v0/performances/"
LIST_TEAMS_ENDPOINT = "/v0/teams/"
LIST_WEEKS_ENDPOINT = "/v0/weeks/"
GET_COUNTS_ENDPOINT = "/v0/counts/"

logger = logging.getLogger(__name__) 

@backoff.on_exception(
    wait_gen=backoff.expo, 
    exception=(httpx.RequestError, httpx.HTTPStatusError),  
    max_time=5,  
    jitter=backoff.random_jitter  
)
