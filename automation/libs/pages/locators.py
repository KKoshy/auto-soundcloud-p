class HomePageSelectors:
    COOKIE_DIALOG = "[id='onetrust-policy']"
    REJECT_ALL = 'button[id="onetrust-reject-all-handler"]'
    SIGN_IN = ':nth-match(button[title="Sign in"], 1)'
    CREATE_ACCOUNT = ":nth-match(button[title='Create a SoundCloud account'], 1)"
    FOR_ARTISTS = 'a[href="/artists"]'
    SEARCH_BAR = ":nth-match(input[placeholder='Search for artists, bands, tracks, podcasts'], 1)"
    UPLOAD_YOUR_OWN = "a[href='/upload']:text-is('Upload your own')"
    EXPLORE_TRENDING_PLAYLISTS = "a[href='/home']"
    QR_CODE = "a[href='/download']"
    FIND_OUT_MORE_LINK = "a:text-is('Find out more')"
    TOP_LOGO = "h1:text-is('SoundCloud')"
    FOOTER_LOGO_LINK = "a[aria-label='SoundCloud'][href='/']"


class DiscoverPageSelectors:
    HOME = "a[href='/discover']"
    FEED = "a[href='/feed']"
    LIBRARY = "a[href='/you/library']"
    SEARCH_BAR = "input[placeholder='Search for artists, bands, tracks, podcasts']"
    SIGN_IN = 'button[title="Sign in"]'
    CREATE_ACCOUNT = "button[title='Create a SoundCloud account']"
    UPLOAD = "a[href='/upload']"
    DISCOVER_TRACKS_HEADER = "h1:text-is('Discover Tracks and Playlists')"
    SOUND_CLOUD = ":nth-match(a[href='/'], 2)"
    SELECTION_MODULE_HEADERS = "div h2[data-test-id]"
