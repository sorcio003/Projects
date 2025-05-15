from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import  login_required, current_user
from .models import Note, Wish_List, Color
from . import db
import json
from sqlalchemy import update

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form['note']

        if len(note) < 1:
            flash('Note is too shoort!', category='error')
        else:
            new_note = Note(titolo=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/Account')
def profile():
    return render_template("profile.html", user=current_user)

@views.route('/lista_libri')
def lista_libri():
    return render_template("lista_libri.html", user=current_user)

@views.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        url_cover = request.form['url_cover']
        mobilebg = request.form['mobilebg']
        introbg = request.form['introbg']
        fontcolor = request.form['fontcolor']
        titolo = request.form['titolo']
        autore = request.form['autore']
        genere = request.form['genere']
        trama = request.form['trama']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        valutazione = request.form['valutazione']
        spicy = request.form['spicy']
        lacrime = request.form['lacrime']
        fav_char = request.form['favourite_Charac']
        hated_char = request.form['hated_Charac']
        fav_scene = request.form['favourite_Scene']
        best_phrase = request.form['best_Phrase']

        new_book = Note(
            url_cover = url_cover,
            mobilebg = mobilebg,
            introbg = introbg,
            fontcolor = fontcolor,
            titolo = titolo,
            autore = autore,
            genere = genere,
            trama = trama,
            date_start = date_start,
            date_end = date_end,
            valutazione = valutazione,
            spicy = spicy,
            lacrime = lacrime,
            favourite_Charac = fav_char,
            hated_Charac = hated_char,
            favourite_Scene = fav_scene,
            best_Phrase = best_phrase,
            user_id=current_user.id
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added !!!', category='success')
        return redirect('/lista_libri')
    return render_template('create.html', user = current_user)

@views.route('/info/<int:idx>/<string:name>/edit', methods=['GET','POST'])
def edit(idx, name):
    if request.method == 'POST':
        url_cover = request.form['url_cover']
        titolo = request.form['titolo']
        autore = request.form['autore']
        genere = request.form['genere']
        trama = request.form['trama']
        mobilebg = request.form['mobilebg']
        introbg = request.form['introbg']
        fontcolor = request.form['fontcolor']
        date_start = request.form['date_start']
        date_end = request.form['date_end']
        valutazione = request.form['valutazione']
        spicy = request.form['spicy']
        lacrime = request.form['lacrime']
        fav_char = request.form['favourite_Charac']
        hated_char = request.form['hated_Charac']
        fav_scene = request.form['favourite_Scene']
        best_phrase = request.form['best_Phrase']

        book_update = Note.query.filter_by(id = idx).first()

        book_update.url_cover = url_cover
        book_update.titolo = titolo
        book_update.autore = autore
        book_update.genere = genere
        book_update.trama = trama
        book_update.mobilebg = mobilebg
        book_update.introbg = introbg
        book_update.fontcolor = fontcolor
        book_update.date_start = date_start
        book_update.date_end = date_end
        book_update.valutazione = valutazione
        book_update.spicy = spicy
        book_update.lacrime = lacrime
        book_update.favourite_Charac = fav_char
        book_update.hated_char = hated_char
        book_update.favourite_Scene = fav_scene
        book_update.best_phrase = best_phrase

        db.session.commit()
        flash('Book update !!!', category='success')
        return redirect('/lista_libri')
    book_search = Note.query.filter_by(id = idx).first()
    return render_template('edit.html', book = book_search, user = current_user)

@views.route('/info/<int:idx>/<string:name>')
def info(idx, name):
    book_search = Note.query.filter_by(id = idx).first()
    return render_template('info.html', book = book_search, user = current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return redirect('/lista_libri')

@views.route('/delete-wish-list', methods=['POST'])
def delete_wish_list():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Wish_List.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return redirect('/wish_list')

@views.route('/wish_list', methods=['GET', 'POST'])
def wish_list():
    if request.method == 'POST':
        url_cover = request.form['url_cover']
        titolo = request.form['titolo']
        autore = request.form['autore']
        costo = request.form['costo']

        new_book = Wish_List(
            url_cover = url_cover,
            titolo = titolo,
            autore = autore,
            costo = costo,
            user_id=current_user.id
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Wish List Aggiornata !!!', category='success')
        return redirect('/wish_list')
    return render_template('wish_list.html', user = current_user)