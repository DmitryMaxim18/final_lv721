from tornado import web, ioloop
from tornado_library_muz import Index, AddSong, DeleteSong, EditSong

if __name__ == '__main__':
    app = web.Application([
        ('/', Index),
        ('/add_song/', AddSong),
        ('/delete_song/', DeleteSong),
        (r"/edit_song/(\d+)/", EditSong)

    ], debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()
