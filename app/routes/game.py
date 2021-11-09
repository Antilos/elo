from flask import Blueprint, request, render_template, flash, redirect, url_for

from app.forms import ResultForm
from app.models import User
from app import db

bp = Blueprint('game', __name__, url_prefix='/game')

def getNewElo(r1, r2, s1, s2, k):
    e = 1 / (1+pow(10, (r2-r1)/400))

    return r1+k*(s1-e), r2+k*(s2-e)

@bp.route('/result', methods=['GET', 'POST'])
def result():
    form = ResultForm()
    if form.validate_on_submit():
        print("FORM VALID")
        player1 = User.query.filter_by(username=form.player1.data).first()
        player2 = User.query.filter_by(username=form.player2.data).first()
        if player1 is None or player2 is None:
            flash('Invalid username.')
            return redirect(url_for('game.result'))

        r1, r2 = getNewElo(player1.elo, player2.elo, form.player1Score.data, form.player2Score.data, 32)
        
        player1.elo = r1
        player2.elo = r2
        
        db.session().commit()
        flash("Elo updated")

        #redirect user to the page they were logging in from
        return redirect(url_for('index'))
    
    print("NOPE")
    flash("FORM NOT VALIDATED")
    #if method was GET, render result template
    return render_template('game/result.html', title='Game Result', form=form)