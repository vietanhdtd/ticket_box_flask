from flask import Blueprint, render_template, redirect , url_for, flash
from components.events.forms.forms import CreateEventForm, EditEventForm
from components.events.forms.forms import PurchaseForm
from models.ticketbox import Event, Purchase, db
from flask_login import current_user


events_blueprint = Blueprint('events', __name__, template_folder='templates')

@events_blueprint.route('/<int:user_id>/create', methods = ['POST', 'GET'])
def create(user_id):
    form = CreateEventForm()
    if form.validate_on_submit():
        new_event = Event(user_id = user_id,
                        title = form.title.data,
                        location = form.location.data,
                        description = form.description.data,
                        image_url = form.image_url.data,
                        starting_date = form.starting_date.data.strftime('%v'))
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('events.feeds'))
    return render_template('create.html', form = form)

@events_blueprint.route('/<int:event_id>/delete')
def delete(event_id):
    Event.query.filter_by(id = event_id).delete()
    db.session.commit()
    return redirect(url_for('events.feeds'))

@events_blueprint.route('/<int:event_id>')
def viewMore(event_id):
    event = Event.query.filter_by( id = event_id).first()
    return render_template('event.html', event = event)

@events_blueprint.route('/<int:event_id>/purchase', methods = ['POST', 'GET'])
def purchase(event_id):
    purchase = PurchaseForm()
    if purchase.validate_on_submit():
        new_purchase = Purchase(event_id = event_id,
                                user_id = current_user.get_id(),
                                quantity = purchase.quantity.data,
                                payment_method = purchase.payment_method.data
                                )
        db.session.add(new_purchase)
        db.session.commit()
        return redirect(url_for('events.feeds'))
    return render_template('purchase.html', purchase = purchase)

@events_blueprint.route('/<int:event_id>/edit', methods = ['POST', 'GET'])
def editEvent(event_id):
    event = Event.query.get(event_id)
    form = EditEventForm(obj=event)
    # if current_user.is_anonymous:
    #     flash("You Have to Login First")
    #     return redirect(url_for('events.feeds'))
    # if event.user_id != current_user.get_id():
    #     flash("You can not edit this post")
    #     return redirect(url_for('events.feeds'))
    if form.validate_on_submit():
        event.title = form.title.data,
        event.location = form.location.data,
        event.description = form.description.data,
        event.image_url = form.image_url.data,
        event.starting_date = form.starting_date.data,
        event.price = form.price.data
        db.session.commit()
        return redirect(url_for('events.feeds'))
    return render_template('create.html',form = form)

@events_blueprint.route('/feeds')
def feeds():
    events = Event.query.all()
    return render_template('feeds.html', events = events)


