from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import  login_required, current_user
from .models import Note, Wish_List, Theme, User
from . import db
import json
from sqlalchemy import update, asc
from collections import Counter
from datetime import datetime

views = Blueprint('views', __name__)

def jinja2_zip(*args):
    return zip(*args)

def theme_set():
    theme = Theme.query.filter_by(user_id=current_user.id).first()
    if not theme:
        theme = theme = Theme.query.filter_by(id=1).first()
    return theme

def add_opacity_to_hex(hex_color, opacity):
    hex_color = hex_color.lstrip('#')  # Rimuove il carattere '#' se presente
    rgba = f"rgba({int(hex_color[0:2], 16)}, {int(hex_color[2:4], 16)}, {int(hex_color[4:6], 16)}, {opacity})"
    return rgba

def rgba_to_hex(rgba_color):
    rgba_values = rgba_color.replace("rgba(", "").replace(")", "").split(",")
    rgb = [int(value) for value in rgba_values[:3]]  # Estrai i valori RGB
    hex_values = [hex(value).split('x')[-1].zfill(2) for value in rgb]  # Converti i valori RGB in esadecimali
    hex_code = '#' + ''.join(hex_values)  # Concatena i valori esadecimali
    return hex_code

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    theme = theme_set()
    n_libri = len(current_user.notes)
    generi_libri = [note.genere for note in current_user.notes]
    generi_contati = Counter(generi_libri)  # Contiamo le occorrenze di ciascun genere
    genere_piu_comune = generi_contati.most_common(1)  # Troviamo il genere più comune
    if genere_piu_comune:
        genere_piu_comune = genere_piu_comune[0][0]  # Estraiamo il genere più comune dalla tupla
    else:
        genere_piu_comune = None

    if request.method == 'POST':
        form_id = request.form.get('form_id')  # Ottieni l'ID del form
        url_cover = request.form.get('url_cover')
        titolo = request.form.get('titolo')
        autore = request.form.get('autore')
        costo = request.form.get('costo')
        trama = request.form.get('trama')
        voto = request.form.get('voto')
        tipo = request.form.get('type')
        attori = request.form.get('attori')
        character = request.form.get('character')
        preview = request.form.get('preview')
        foto = request.form.get('Fotoattori')
        attori = attori.split(',')
        foto = foto.split(',')
        character = character.split(',')

        if costo == "Prezzo non disponibile":
            costo = "None"
        return render_template("search_info.html",user=current_user, theme=theme,preview=preview, trama=trama, titolo=titolo,character=character,attori=attori, foto=foto, autore=autore, costo=costo, url_cover=url_cover, voto=voto, tipo=tipo)

    return render_template("home.html", user=current_user, theme=theme, genere=genere_piu_comune)

@views.route('/add_to_wishlist', methods=['GET', 'POST'])
def add_to_wishlist():
    theme = theme_set()
    if request.method == 'POST':
        url_cover = request.form.get('url_cover')
        titolo = request.form.get('titolo')
        autore = request.form.get('autore')
        costo = request.form.get('costo')
        tipo = request.form.get('tipo')
        voto = request.form.get('voto')

        if tipo == "film" or tipo == "serieTv":
            costo = voto

        nuovo_libro = Wish_List(
            url_cover=url_cover,
            titolo=titolo,
            autore=autore,
            costo=costo,
            tipo = tipo,
            user_id=current_user.id
            )

        db.session.add(nuovo_libro)
        db.session.commit()

        flash('Wish List updated !!!', category='success')

        return redirect(url_for('views.home'))
    return render_template("search_result.html", user=current_user, theme=theme)


@views.route('/Account')
def profile():
    theme = theme_set()
    n_libri = len(current_user.notes)
    generi_libri = [note.genere for note in current_user.notes]
    generi_contati = Counter(generi_libri)  # Contiamo le occorrenze di ciascun genere
    genere_piu_comune = generi_contati.most_common(1)  # Troviamo il genere più comune
    if genere_piu_comune:
        genere_piu_comune = genere_piu_comune[0][0]  # Estraiamo il genere più comune dalla tupla
    else:
        genere_piu_comune = None

    tempo_lettura = []

    media = 0

    for note in current_user.notes:
        if not note.date_start:
            note.date_start = datetime.now().strftime("%d/%m/%Y")  # Salva la data di oggi se manca la data di inizio
        if not note.date_end:
            note.date_end = note.date_start  # Copia la data di inizio se manca la data di fine

        data_inizio_dt = datetime.strptime(note.date_start, "%d/%m/%Y")
        data_fine_dt = datetime.strptime(note.date_end, "%d/%m/%Y")

        # Calcola la differenza tra le due date
        differenza = data_fine_dt - data_inizio_dt

        # Converte la differenza in ore
        differenza_in_ore = differenza.total_seconds() / 3600

        tempo_lettura.append(int(differenza_in_ore))

        media += differenza_in_ore

    if media != 0:
        tempo_medio = int((media / len(tempo_lettura)) / 24 )
    else:
        tempo_medio = 0
    generi_libri_no_dup = list(dict.fromkeys(generi_libri))
    numero_generi = list(generi_contati.values())

    return render_template("profile.html", user=current_user, theme=theme, n_libri=n_libri, genere_più_comune=genere_piu_comune, tempo_medio=tempo_medio, tempo_lettura=tempo_lettura, generi_libri=generi_libri_no_dup, conteggio_generi=numero_generi)
@views.route('/lista_libri')
def lista_libri():
    theme = theme_set()
    book_search = Note.query.filter_by(user_id=current_user.id).order_by(asc(Note.titolo)).all()
    return render_template("lista_libri.html", user=current_user,theme=theme, book = book_search)

@views.route('/ohana_review')
def ohana_review():
    theme = theme_set()

    book_search = Note.query.filter_by(user_id=5).order_by(asc(Note.titolo)).all()
    return render_template("ohana_review.html", user=current_user,theme=theme, book = book_search)

@views.route('/create', methods=['GET', 'POST'])
def create():
    theme = theme_set()
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
        review = request.form['review']
        tipo = request.form['tipo']
        

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
            user_id=current_user.id,
            review = review,
            tipo = tipo
        )
        db.session.add(new_book)
        db.session.commit()
        flash('Book added !!!', category='success')
        return redirect('/lista_libri')
    return render_template('create.html', user = current_user, theme=theme)

@views.route('/info/<int:idx>/<string:name>/edit', methods=['GET','POST'])
def edit(idx, name):
    theme = theme_set()
    book_update = Note.query.filter_by(id = idx).first()
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
        review = request.form['review']
        tipo = request.form['tipo']

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
        book_update.best_Phrase = best_phrase
        book_update.review = review
        book_update.tipo = tipo

        db.session.commit()
        flash('Book update !!!', category='success')
        return redirect('/lista_libri')
    return render_template('edit.html', user = current_user, theme=theme, book = book_update)

@views.route('/info/<int:idx>/<string:name>')
def info(idx, name):
    theme = theme_set()
    book_search = Note.query.filter_by(id = idx).first()
    return render_template('info.html', book = book_search, user = current_user, theme=theme)

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
    theme = theme_set()
    wish_list_notes = Wish_List.query.filter_by(user_id=current_user.id).order_by(asc(Wish_List.titolo)).all()
    if request.method == 'POST':
        url_cover = request.form['url_cover']
        titolo = request.form['titolo']
        autore = request.form['autore']
        costo = request.form['costo']
        tipo = request.form['tipo']

        new_book = Wish_List(
            url_cover = url_cover,
            titolo = titolo,
            autore = autore,
            costo = costo,
            tipo = tipo,
            user_id=current_user.id
        )
        db.session.add(new_book)
        db.session.commit()

        flash('Wish List Aggiornata !!!', category='success')
        return redirect('/wish_list')
    return render_template('wish_list.html', user = current_user,theme=theme, wish_list_notes = wish_list_notes)

@views.route('/custom',  methods=['GET', 'POST'])
def custom():
    theme = theme_set()
    load_light = rgba_to_hex(theme.theme_light_primary_loading)
    load_dark = rgba_to_hex(theme.theme_dark_primary_loading)

    if request.method == 'POST':
        theme_light_primary = request.form.get('theme_light_primary')
        theme_light_primary_loading = request.form.get('theme_light_primary_loading')
        theme_light_secondary = request.form.get('theme_light_secondary')
        theme_light_accent = request.form.get('theme_light_accent')
        theme_light_font_color = request.form.get('theme_light_font_color')
        theme_light_extra = request.form.get('theme_light_extra')
        theme_light_font_color_hover = request.form.get('theme_light_font_color_hover')
        theme_dark_primary = request.form.get('theme_dark_primary')
        theme_dark_primary_loading = request.form.get('theme_dark_primary_loading')
        theme_dark_secondary = request.form.get('theme_dark_secondary')
        theme_dark_accent = request.form.get('theme_dark_accent')
        theme_dark_font_color = request.form.get('theme_dark_font_color')
        theme_dark_extra = request.form.get('theme_dark_extra')
        theme_dark_font_color_hover = request.form.get('theme_dark_font_color_hover')

        theme_light_primary_loading = add_opacity_to_hex(theme_light_primary_loading, 0.4)
        theme_dark_primary_loading = add_opacity_to_hex(theme_dark_primary_loading, 0.4)

        if theme.id == 1:
            new_theme = Theme(
                theme_light_primary = theme_light_primary,
                theme_light_primary_loading = theme_light_primary_loading,
                theme_light_secondary = theme_light_secondary,
                theme_light_accent = theme_light_accent,
                theme_light_font_color = theme_light_font_color,
                theme_light_extra = theme_light_extra,
                theme_light_font_color_hover = theme_light_font_color_hover,
                theme_dark_primary = theme_dark_primary,
                theme_dark_primary_loading = theme_dark_primary_loading,
                theme_dark_secondary = theme_dark_secondary,
                theme_dark_accent = theme_dark_accent,
                theme_dark_font_color = theme_dark_font_color,
                theme_dark_extra = theme_dark_extra,
                theme_dark_font_color_hover = theme_dark_font_color_hover,
                user_id = current_user.id
            )

            db.session.add(new_theme)

        else:
            theme.theme_light_primary = theme_light_primary
            theme.theme_light_primary_loading = theme_light_primary_loading
            theme.theme_light_secondary = theme_light_secondary
            theme.theme_light_accent = theme_light_accent
            theme.theme_light_font_color = theme_light_font_color
            theme.theme_light_extra = theme_light_extra
            theme.theme_light_font_color_hover = theme_light_font_color_hover
            theme.theme_dark_primary = theme_dark_primary
            theme.theme_dark_primary_loading = theme_dark_primary_loading
            theme.theme_dark_secondary = theme_dark_secondary
            theme.theme_dark_accent = theme_dark_accent
            theme.theme_dark_font_color = theme_dark_font_color
            theme.theme_dark_extra = theme_dark_extra
            theme.theme_dark_font_color_hover = theme_dark_font_color_hover

        db.session.commit()
        flash('Theme updated !!!', category='success')
        return redirect('/Account')
    return render_template('personalizzazione.html', user=current_user, theme=theme, load_light=load_light, load_dark=load_dark)

@views.route('/preview')
def preview():
    Theme = theme_set()
    theme = {
        'theme_light_primary' : request.args.get('theme_light_primary', Theme.theme_light_primary),
        'theme_light_primary_loading': request.args.get('theme_light_primary_loading', Theme.theme_light_primary_loading),
        'theme_light_secondary': request.args.get('theme_light_secondary', Theme.theme_light_secondary),
        'theme_light_accent': request.args.get('theme_light_accent', Theme.theme_light_accent),
        'theme_light_font_color': request.args.get('theme_light_font_color', Theme.theme_light_font_color),
        'theme_light_extra': request.args.get('theme_light_extra', Theme.theme_light_extra),
        'theme_light_font_color_hover': request.args.get('theme_light_font_color_hover', Theme.theme_light_font_color_hover),
        'theme_dark_primary': request.args.get('theme_dark_primary', Theme.theme_dark_primary),
        'theme_dark_primary_loading': request.args.get('theme_dark_primary_loading', Theme.theme_dark_primary_loading),
        'theme_dark_secondary': request.args.get('theme_dark_secondary', Theme.theme_dark_secondary),
        'theme_dark_accent': request.args.get('theme_dark_accent', Theme.theme_dark_accent),
        'theme_dark_font_color': request.args.get('theme_dark_font_color', Theme.theme_dark_font_color),
        'theme_dark_extra': request.args.get('theme_dark_extra', Theme.theme_dark_extra),
        'theme_dark_font_color_hover': request.args.get('theme_dark_font_color_hover', Theme.theme_dark_font_color_hover)
    }
    return render_template('preview.html',user=current_user, theme=theme)
