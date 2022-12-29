from tornado import web
from sqlalchemy.orm import sessionmaker
from models import MusicLibrary
from db import engine


class Index(web.RequestHandler):

    def get(self):
        session = sessionmaker(bind=engine)()
        songs = session.query(MusicLibrary).all()
        self.render('templates/index.html', songs=songs)


class AddSong(web.RequestHandler):

    def get(self):
        self.render('templates/add_songs.html')

    def post(self):
        session = sessionmaker(bind=engine)()
        session.add(
            MusicLibrary(
                name=self.get_body_argument('name'),
                artist=self.get_body_argument('artist'),
                duration=self.get_body_argument('duration')))
        session.commit()
        self.redirect('/')


class DeleteSong(web.RequestHandler):

    def post(self):
        session = sessionmaker(bind=engine)()
        song_id = self.get_body_argument('song_id')
        song = session.query(MusicLibrary).filter_by(id=song_id).one()
        session.delete(song)
        session.commit()
        self.redirect('/')


class EditSong(web.RequestHandler):

    def get(self, param):
        session = sessionmaker(bind=engine)()
        song = session.query(MusicLibrary).filter_by(id=param)
        self.render('templates/edit_song.html', song=song)

    def post(self, param):
        session = sessionmaker(bind=engine)()
        name = self.get_body_argument('name')
        artist = self.get_body_argument('artist')
        duration = self.get_body_argument('duration')
        session.query(MusicLibrary).filter_by(id=param).update({
            MusicLibrary.name: name,
            MusicLibrary.artist: artist,
            MusicLibrary.duration: duration
        })
        session.commit()
        self.redirect('/')



