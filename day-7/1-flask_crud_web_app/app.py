from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

DATABASE = "employees.db"

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    employees = conn.execute('SELECT * FROM employees').fetchall()
    conn.close()
    return render_template('home.html', employees=employees)

@app.route('/employee/<int:id>')
def employee_details(id):
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (id,)).fetchone()
    conn.close()
    if employee is None:
        flash('Employee not found!', 'error')
        return redirect(url_for('home'))
    return render_template('details.html', employee=employee)

@app.route('/add', methods=('GET', 'POST'))
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        designation = request.form['designation']
        if not name or not email or not phone or not designation:
            flash('All fields are required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO employees (name, email, phone, designation) VALUES (?, ?, ?, ?)',
                         (name, email, phone, designation))
            conn.commit()
            conn.close()
            flash('Employee added successfully!', 'success')
            if 'save_new' in request.form:
                return redirect(url_for('add_employee'))
            return redirect(url_for('home'))
    return render_template('employee_form.html', action='Add')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_employee(id):
    conn = get_db_connection()
    employee = conn.execute('SELECT * FROM employees WHERE id = ?', (id,)).fetchone()
    conn.close()
    if employee is None:
        flash('Employee not found!', 'error')
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        designation = request.form['designation']
        if not name or not email or not phone or not designation:
            flash('All fields are required!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE employees SET name = ?, email = ?, phone = ?, designation = ? WHERE id = ?',
                         (name, email, phone, designation, id))
            conn.commit()
            conn.close()
            flash('Employee updated successfully!', 'success')
            return redirect(url_for('home'))
    return render_template('employee_form.html', action='Edit', employee=employee)

@app.route('/delete/<int:id>', methods=('POST',))
def delete_employee(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM employees WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('home'))

@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
