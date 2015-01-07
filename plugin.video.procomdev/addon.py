import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


class Plugin(object):

    MODE_MAIN = None
    MODE_HUNTITDOWN = 'huntitdown'
    MODE_HUNTITDOWN_MOVIES = 'huntitdown-movies'
    MODE_HUNTITDOWN_TVSHOWS = 'huntitdown-tvshow'

    def screen_main(self):
        # Root folder / First screen
        url = build_url({'mode': self.MODE_HUNTITDOWN })
        li = xbmcgui.ListItem('Hunt it down', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

        xbmcplugin.endOfDirectory(addon_handle)


    def screen_huntitdown(self):
        # Hunt it down
        url = build_url({'mode': self.MODE_HUNTITDOWN_MOVIES })
        li = xbmcgui.ListItem('Movies', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

        url = build_url({'mode': self.MODE_HUNTITDOWN_TVSHOWS })
        li = xbmcgui.ListItem('TV Shows', iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

        xbmcplugin.endOfDirectory(addon_handle)


    MODE_HANDLERS = { 
        MODE_MAIN            : screen_main,
        MODE_HUNTITDOWN      : screen_huntitdown,
    }

    def __init__(self):

        mode = args.get('mode', None)
        if mode is not None:
            mode = mode[0]

        Plugin.MODE_HANDLERS[mode](self)

"""
        if mode is None:
        elif mode[0] == 'huntitdown':
        elif mode[0] == 'folder':
            foldername = args['foldername'][0]
            url = 'http://localhost/some_video.mkv'
            li = xbmcgui.ListItem(foldername + ' Video', iconImage='DefaultVideo.png')
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
            xbmcplugin.endOfDirectory(addon_handle)
"""

Plugin()

