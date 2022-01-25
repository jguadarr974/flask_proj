import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    """A dummy doctring."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    
    def pub1(self):
        """A dummy docstring."""
        print("")
        
    def pub2(self):
        """A dummy docstring."""
        print("")
        
@app.route("/edit", )
def home1():
        """A dummy docstring."""
        todo_list = Todo.query.all()
        return render_template("base.html", todo_list=todo_list)
    
@app.route("/")
def list1():
        """A dummy docstring."""
        todo_list = Todo.query.all()
        return render_template("list.html", todo_list=todo_list)
    
@app.route("/add", methods=["POST"])
def add():
        """A dummy docstring."""
        title = request.form.get("title")
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("home1"))
    
@app.route("/update/<int:todo_id>")
def update(todo_id):
        """A dummy docstring."""
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for("home1"))
    
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home1'))

@app.route('/home')
def home():
    todo_list = Todo.query.all()
    return render_template('list.html', todo_list = todo_list)

@app.route('/clear/<int:todo_id>')
def clear(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.clear(todo)
    db.session.commit()
    return redirect(url_for('home1'))

        
if __name__ == "__main__":
        db.create_all()
        port = int(os.environ.get('PORT', 5000))
        app.run(port=port, debug=True) #deleted host= '0.0.0.0'
        
        app.run(debug=True) 
        