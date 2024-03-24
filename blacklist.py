import tldextract


blackList = [
    "24aktuelles.com",
    "12minutos.com",
    "24aktuelles.com",
    "actualite.co",
    "theasociatedpress.com",
    "thebreakingnews.co",
    "BreakingNews247.net",
    "BreakingNews365.net",
    "cbs-news.us",
    "cbsnews.us",
    "channel22news.com",
    "Channel24news.com",
    "cnoticias.net",
    "en-bref.fr",
    "nachrichten.de.com",
    "net-infosnews.com",
    "noticias-frescas.com",
    "notizzia.com",
    "routers.news",
    "americasfreedomfighters.com"
]

def checkIfBlacklisted (link) :
    isBlackListed = 0
    
    linkDomain = tldextract.extract(link).domain

    for site in blackList:
        blackedDomain = (tldextract.extract(site)).domain
        if blackedDomain == linkDomain :
            isBlackListed = 1
            return isBlackListed

    return isBlackListed
