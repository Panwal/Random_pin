from flask import request, render_template, make_respone
from datetime import current_app as dt
from flask import db, pin
from random import randint
from flask import Flask



def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = 10**(n-1)-1
    return randint(range_start, range_end)

@app.route('/api/generate/', methods=['GET'])
def generate_pin():
    """generate pin."""

   new_pin = Number(
        digit=random_with_N_digits(15)
    )
    # Adds new User record to database
    db.session.add(new_pin)
    # Commits all changes
    db.session.commit()  
    return make_response({'pin': new_pin.digit, 'serial': 
    f'0{new_pin.id}', 'message': 'Pin generated sucesfully!'})  

@app.route('/api/<serial>')
def validate_pin(pin, serial):
    """Validate pin"""
    pin = int(pin)
    serial = int(serial)
    db_pin = Pin.query.filter_by(digit=pin, id=serial).first()
    if db_pin:
        return make_response({'message': 'valid Pin'})
    return make_response({'message': 'Pin doest not exists ...!'}), 404
